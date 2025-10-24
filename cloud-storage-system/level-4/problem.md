# Level 4 — File Compression and Decompression

## Overview
Add support for compressing and decompressing files, with size reduction and ownership tracking.
This is the final level, building on all previous levels.

## New Requirements

Implement support for file compression that reduces file size and maintains user capacity limits.

## Required Methods

| Method | Description |
|--------|-------------|
| `compress_file(self, user_id: str, name: str) -> int \| None` | Compress the file `name` if it belongs to `user_id`. The compressed file replaces the original with name `<name>.COMPRESSED` and size equal to half of the original. Returns remaining capacity if successful, `None` otherwise. |
| `decompress_file(self, user_id: str, name: str) -> int \| None` | Revert compression of file `name` (which ends with `.COMPRESSED`) if it belongs to `user_id`. Fails if it would exceed capacity or if decompressed version already exists. Returns remaining capacity if successful, `None` otherwise. |

## Compression Rules

- Compressed file size = original size / 2
- All file sizes are guaranteed to be even (no fractional calculations)
- Compressed files are named `<original_name>.COMPRESSED`
- `name` parameter for `compress_file` never points to an already compressed file
- Compressed files cannot be added via `add_file` (file names only contain lowercase letters)
- `copy_file` preserves the `.COMPRESSED` suffix

## Decompression Rules

- Decompressed file size = compressed size × 2
- `name` parameter for `decompress_file` always ends with `.COMPRESSED`
- Fails if decompression would exceed user's capacity limit
- Fails if decompressed version of the file already exists

## Example

```python
add_user("user1", 1000)
add_user("user2", 5000)
add_file_by("user1", "/dir/file.mp4", 500)
compress_file("user2", "/dir/file.mp4")      # → None (not owner)
compress_file("user3", "/dir/file.mp4")      # → None (user doesn't exist)
compress_file("user1", "/folder/non_existing_file")  # → None
compress_file("user1", "/dir/file.mp4")      # → 750 (500 freed, 250 used)
get_file_size("/dir/file.mp4.COMPRESSED")    # → 250
get_file_size("/dir/file.mp4")               # → None (replaced)
copy_file("/dir/file.mp4.COMPRESSED", "/file.mp4.COMPRESSED")  # → True
add_file_by("user1", "/dir/file.mp4", 500)  # → 250
decompress_file("user1", "/dir/file.mp4.COMPRESSED")  # → None (original exists)
update_capacity("user1", 2000)               # → 0
decompress_file("user2", "/dir/file.mp4.COMPRESSED")  # → None (not owner)
decompress_file("user3", "/dir/file.mp4.COMPRESSED")  # → None (user doesn't exist)
decompress_file("user1", "/dir/file.mp4.COMPRESSED")  # → 1250
decompress_file("user1", "/file.mp4.COMPRESSED")      # → 750
```

## Note
All methods from Levels 1, 2, and 3 must still work.
