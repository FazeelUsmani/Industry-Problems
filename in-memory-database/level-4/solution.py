from typing import Dict, List, Optional, Tuple

AliveVal = Tuple[str, Optional[int]]  # (value, expires_at) where None = no TTL

class InMemoryDB:
    def __init__(self):
        # data[key][field] = (value, expires_at)
        self.data: Dict[str, Dict[str, AliveVal]] = {}
        self._backups: List[Tuple[int, Dict[str, Dict[str, Tuple[str, Optional[int]]]]]] = []

    # ---------- Level 1 ----------
    def set(self, key: str, field: str, value: str) -> None:
        self.data.setdefault(key, {})[field] = (value, None)

    def get(self, key: str, field: str) -> Optional[str]:
        rec = self.data.get(key)
        if not rec or field not in rec:
            return None
        return rec[field][0]

    def delete(self, key: str, field: str) -> bool:
        rec = self.data.get(key)
        if not rec or field not in rec:
            return False
        del rec[field]
        return True

    # ---------- Level 2 ----------
    def _format_scan(self, items: Dict[str, str]) -> List[str]:
        return [f"{f}({items[f]})" for f in sorted(items)]

    def scan(self, key: str) -> List[str]:
        rec = self.data.get(key)
        if not rec:
            return []
        return self._format_scan({f: v for f, (v, _) in rec.items()})

    def scan_by_prefix(self, key: str, prefix: str) -> List[str]:
        rec = self.data.get(key)
        if not rec:
            return []
        subset = {f: v for f, (v, _) in rec.items() if f.startswith(prefix)}
        return self._format_scan(subset)

    # ---------- Level 3 helpers ----------
    @staticmethod
    def _alive(exp_at: Optional[int], t: int) -> bool:
        """Alive during interval [start, exp_at); exp_at=None means no expiry."""
        return exp_at is None or t < exp_at

    def _alive_fields(self, key: str, t: int) -> Dict[str, str]:
        rec = self.data.get(key)
        if not rec:
            return {}
        return {f: v for f, (v, exp) in rec.items() if self._alive(exp, t)}

    def _record_alive(self, key: str, t: int) -> bool:
        return bool(self._alive_fields(key, t))

    # ---------- Level 3 write APIs ----------
    def set_at(self, key: str, field: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, {})[field] = (value, None)

    def set_at_with_ttl(
        self, key: str, field: str, value: str, timestamp: int, ttl: int
    ) -> None:
        expires_at = timestamp + ttl
        self.data.setdefault(key, {})[field] = (value, expires_at)

    def delete_at(self, key: str, field: str, timestamp: int) -> bool:
        if not self._record_alive(key, timestamp):
            return False
        rec = self.data[key]
        val = rec.get(field)
        if val is None:
            return False
        if not self._alive(val[1], timestamp):
            return False
        del rec[field]
        return True

    # ---------- Level 3 read APIs ----------
    def get_at(self, key: str, field: str, timestamp: int) -> Optional[str]:
        rec = self.data.get(key)
        if not rec or field not in rec:
            return None
        value, exp = rec[field]
        return value if self._alive(exp, timestamp) else None

    def scan_at(self, key: str, timestamp: int) -> List[str]:
        return self._format_scan(self._alive_fields(key, timestamp))

    def scan_by_prefix_at(self, key: str, prefix: str, timestamp: int) -> List[str]:
        alive = self._alive_fields(key, timestamp)
        return self._format_scan({f: v for f, v in alive.items() if f.startswith(prefix)})

    # ---------- Level 4 ----------
    def backup(self, timestamp: int) -> int:
        """
        Save DB state at `timestamp`, storing remaining TTL (not absolute expiry).
        Returns number of non-empty (has at least one alive field) records.
        """
        snapshot: Dict[str, Dict[str, Tuple[str, Optional[int]]]] = {}
        for key, rec in self.data.items():
            fields: Dict[str, Tuple[str, Optional[int]]] = {}
            for f, (v, exp) in rec.items():
                if self._alive(exp, timestamp):
                    rem_ttl = None if exp is None else (exp - timestamp)
                    # rem_ttl must be >0 if not None due to _alive check
                    fields[f] = (v, rem_ttl)
            if fields:
                snapshot[key] = fields
        self._backups.append((timestamp, snapshot))
        return len(snapshot)

    def restore(self, timestamp: int, timestamp_to_restore: int) -> None:
        """
        Restore from the latest backup with backup_time <= timestamp_to_restore.
        Recalculate expirations so remaining TTL at backup becomes relative
        to the *restore* `timestamp`.
        """
        # Find latest backup <= timestamp_to_restore
        chosen: Optional[Dict[str, Dict[str, Tuple[str, Optional[int]]]]] = None
        chosen_time = -1
        for t, snap in self._backups:
            if t <= timestamp_to_restore and t > chosen_time:
                chosen_time, chosen = t, snap
        # Problem statement guarantees existence
        new_data: Dict[str, Dict[str, AliveVal]] = {}
        for key, rec in (chosen or {}).items():
            rebuilt: Dict[str, AliveVal] = {}
            for f, (v, rem_ttl) in rec.items():
                exp = None if rem_ttl is None else (timestamp + rem_ttl)
                rebuilt[f] = (v, exp)
            if rebuilt:
                new_data[key] = rebuilt
        self.data = new_data
