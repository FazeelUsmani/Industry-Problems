# Level 2 – Filtering and Display

## Overview
Extend the database to support listing and filtering fields in a record.
This builds on Level 1. Complete this level to unlock Level 3.

## Required Methods

| Method | Description |
|--------|-------------|
| `scan(self, key: str) -> list[str]` | Return a list of "field(value)" strings for all fields in key, sorted lexicographically |
| `scan_by_prefix(self, key: str, prefix: str) -> list[str]` | Same as scan, but include only fields whose names start with prefix |

## Example

```python
set("A", "BC", "E")
set("A", "BD", "F")
set("A", "C",  "G")

scan_by_prefix("A", "B")  # → ["BC(E)", "BD(F)"]
scan("A")                 # → ["BC(E)", "BD(F)", "C(G)"]
scan_by_prefix("B", "B")  # → []
```

## Note
All Level 1 methods (set, get, delete) must still work.
