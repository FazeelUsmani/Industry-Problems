from typing import Dict, List, Optional, Tuple

AliveVal = Tuple[str, Optional[int]]   # (value, expires_at) where None = no TTL

class InMemoryDB:
    def __init__(self):
        # data[key][field] = (value, expires_at)
        self.data: Dict[str, Dict[str, AliveVal]] = {}

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
    # same as set(), but happening at a timestamp (no TTL)
    def set_at(self, key: str, field: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, {})[field] = (value, None)

    # set with TTL; value is available on [timestamp, timestamp+ttl)
    def set_at_with_ttl(
        self, key: str, field: str, value: str, timestamp: int, ttl: int
    ) -> None:
        expires_at = timestamp + ttl
        self.data.setdefault(key, {})[field] = (value, expires_at)

    # delete scoped to a timestamp
    def delete_at(self, key: str, field: str, timestamp: int) -> bool:
        # if the record has no alive fields at time t, it "doesn't exist"
        if not self._record_alive(key, timestamp):
            return False
        rec = self.data[key]
        val = rec.get(field)
        if val is None:
            return False
        # if the target field is already expired at t, it's effectively absent
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
