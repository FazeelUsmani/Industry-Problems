# Level 3 – TTL (Time-To-Live)

## Overview
Add timestamps and TTL (lifespan) support for fields.
Each set, get, and delete now has timestamped variants.
This builds on Levels 1 & 2. Complete this level to unlock Level 4.

## Requirements
- A field with TTL `x` created at time `t` is alive during `[t, t+x)`
- Timestamps strictly increase; time never goes backward
- The system must remain backward-compatible: previous methods still work

## Required Methods

| Method | Description |
|--------|-------------|
| `set_at(self, key, field, value, timestamp)` | Same as set, but occurring at a specific time |
| `set_at_with_ttl(self, key, field, value, timestamp, ttl)` | Insert a field that expires at timestamp + ttl |
| `get_at(self, key, field, timestamp)` | Return the value only if the field is alive at that time |
| `delete_at(self, key, field, timestamp)` | Delete only if the field and key exist at that time |
| `scan_at(self, key, timestamp)` | Return all alive fields for that record |
| `scan_by_prefix_at(self, key, prefix, timestamp)` | Same as above, but filtered by prefix |

## Example 1

```python
set_at_with_ttl("A","BC","E",1,9)     # expires 10
set_at_with_ttl("A","BC","E",5,10)    # new expiry 15
set_at("A","BD","F",5)

scan_by_prefix_at("A","B",14)  # → ["BC(E)","BD(F)"]
scan_by_prefix_at("A","B",15)  # → ["BD(F)"]
```

## Example 2

```python
set_at("A","B","C",1)
set_at_with_ttl("X","Y","Z",2,15)
get_at("X","Y",3)   # → "Z"
set_at_with_ttl("A","D","E",4,10)
scan_at("A",13)     # → ["B(C)","D(E)"]
scan_at("X",16)     # → ["Y(Z)"]
scan_at("X",17)     # → []  (expired)
delete_at("X","Y",20)  # → False
```

## Note
All Level 1 and Level 2 methods must still work.
