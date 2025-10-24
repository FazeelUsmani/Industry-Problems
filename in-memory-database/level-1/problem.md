# Level 1 – Basic Operations

## Overview
Your task is to implement a simplified version of an in-memory database.
This is Level 1 of 4. Complete this level to unlock Level 2.

## Requirements
Implement an in-memory database that supports basic record manipulation:
- A record is accessed by a unique key (string)
- Each record contains multiple fields (string → string)

## Required Methods

| Method | Description |
|--------|-------------|
| `set(self, key: str, field: str, value: str) -> None` | Insert or update a field-value pair inside the record for key |
| `get(self, key: str, field: str) -> Optional[str]` | Return the value of a field in a record, or None if missing |
| `delete(self, key: str, field: str) -> bool` | Remove the field from the record. Return True if it existed and was removed, otherwise False |

## Example

```python
set("A", "B", "E")
set("A", "C", "F")
get("A", "B")         # → "E"
get("A", "D")         # → None
delete("A", "B")      # → True
delete("A", "D")      # → False
```

## State Evolution

```
set(A,B,E) → {"A": {"B": "E"}}
set(A,C,F) → {"A": {"B": "E", "C": "F"}}
```
