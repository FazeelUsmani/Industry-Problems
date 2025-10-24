# Level 4 – Backup and Restore

## Overview
Support backups (saving snapshots) and restores (rolling back state).
This is the final level, building on all previous levels.

## Behavior
- A backup records the database state at a given timestamp
- For each field, it stores remaining TTL (expires_at − timestamp)
- On restore, TTLs are recalculated relative to the new restore time
- Time always moves forward: restored items should expire after restore time

## Required Methods

| Method | Description |
|--------|-------------|
| `backup(self, timestamp)` | Save a snapshot of the alive records at this time. Return the number of non-empty (alive) records |
| `restore(self, timestamp, timestamp_to_restore)` | Restore from the latest backup whose time ≤ timestamp_to_restore. Recompute TTLs relative to timestamp |

## Example

```python
set_at_with_ttl("A","B","C",1,10)  # expires at 11
backup(3)
set_at("A","D","E",4)
backup(5)
delete_at("A","B",8)
backup(9)
restore(10,7)
backup(11)
scan_at("A",15)
scan_at("A",16)
```

### Step-by-step

| Operation | State / Output |
|-----------|----------------|
| `set_at_with_ttl("A","B","C",1,10)` | {"A":{"B":"C"}} expires at 11 |
| `backup(3)` | returns 1 |
| `set_at("A","D","E",4)` | {"A":{"B":"C","D":"E"}} |
| `backup(5)` | returns 1 |
| `delete_at("A","B",8)` | returns True |
| `backup(9)` | returns 1 |
| `restore(10,7)` | restores snapshot from t=5; TTL recalculated; B expires at 16 |
| `backup(11)` | returns 1 |
| `scan_at("A",15)` | → ["B(C)", "D(E)"] |
| `scan_at("A",16)` | → ["D(E)"] |

## Note
All methods from Levels 1, 2, and 3 must still work.
