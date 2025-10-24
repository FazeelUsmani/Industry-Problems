from typing import List, Optional

class InMemoryDB:
    def __init__(self):
        self.data: dict[str, dict[str, str]] = {}

    # ----- Level 1 -----
    def set(self, key: str, field: str, value: str) -> None:
        self.data.setdefault(key, {})[field] = value

    def get(self, key: str, field: str) -> Optional[str]:
        return self.data.get(key, {}).get(field)

    def delete(self, key: str, field: str) -> bool:
        rec = self.data.get(key)
        if rec is None or field not in rec:
            return False
        del rec[field]
        return True

    # ----- Level 2 -----
    def _format_scan(self, items: dict[str, str]) -> List[str]:
        # fields must be sorted lexicographically; output "field(value)"
        return [f"{f}({items[f]})" for f in sorted(items)]

    def scan(self, key: str) -> List[str]:
        rec = self.data.get(key)
        if not rec:
            return []
        return self._format_scan(rec)

    def scan_by_prefix(self, key: str, prefix: str) -> List[str]:
        rec = self.data.get(key)
        if not rec:
            return []
        subset = {f: v for f, v in rec.items() if f.startswith(prefix)}
        return self._format_scan(subset)
