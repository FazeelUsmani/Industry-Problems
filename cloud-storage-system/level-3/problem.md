# Level 3 — User Management with Capacity Limits

## Overview
Add support for different users with individual storage capacity limits.
All users share a common filesystem, but each has their own storage quota.
This builds on Levels 1 & 2. Complete this level to unlock Level 4.

## New Requirements

Implement support for different users sending queries to the system. Each user has an individual storage capacity limit.

## Required Methods

| Method | Description |
|--------|-------------|
| `add_user(self, user_id: str, capacity: int) -> bool` | Add a new user to the system with `capacity` as their storage limit in bytes. The total size of all files owned by `user_id` cannot exceed `capacity`. Returns `True` if successfully created, `False` if user already exists. |
| `add_file_by(self, user_id: str, name: str, size: int) -> int \| None` | Same as `add_file` from Level 1, but the file is owned by `user_id`. Cannot add if it exceeds user's capacity. Returns remaining storage capacity if successful, `None` otherwise. |
| `update_capacity(self, user_id: str, capacity: int) -> int \| None` | Change the maximum storage capacity for `user_id`. If total file size exceeds new capacity, remove largest files (lexicographically for ties) until under capacity. Returns number of removed files, or `None` if user doesn't exist. |

## Important Notes

- All queries calling `add_file` from Level 1 are run by user "admin" with unlimited storage capacity
- The `copy_file` operation preserves ownership of the original file
- When reducing capacity, files are removed in order: largest size first, then lexicographically for ties

## Example

```python
add_user("user1", 125)          # → True
add_user("user1", 100)          # → False (already exists)
add_user("user2", 100)          # → True
add_file_by("user1", "/dir/file.big", 50)    # → 75
add_file_by("user1", "/file.med", 30)        # → 45
add_file_by("user2", "/file.med", 40)        # → 60
copy_file("/file.med", "/dir/another/another/file.med")  # → True (preserves ownership)
copy_file("/file.med", "/dir/another/file.med")          # → True
add_file_by("user1", "/dir/file.small", 10)  # → 35
add_file_by("user1", "/dir/file.small", 5)   # → None (already exists)
add_file_by("user1", "/my_folder/file.huge", 100)  # → None (exceeds capacity)
add_file_by("user3", "/my_folder/file.huge", 100)  # → None (user doesn't exist)
update_capacity("user1", 300)   # → 0 (no files removed)
update_capacity("user1", 50)    # → 2 (removes largest files)
update_capacity("user2", 1000)  # → 0
```

## Note
All Level 1 and Level 2 methods must still work.
