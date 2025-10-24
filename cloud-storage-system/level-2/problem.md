# Level 2 — File Search by Prefix and Suffix

## Overview
Extend the cloud storage system to support searching for files by matching prefixes and suffixes.
This builds on Level 1. Complete this level to unlock Level 3.

## New Requirement

Add support for retrieving file names by searching directories via prefixes and suffixes.

## Required Method

| Method | Description |
|--------|-------------|
| `find_file(self, prefix: str, suffix: str) -> list[str]` | Search for files with names starting with `prefix` and ending with `suffix`. Returns a list of strings in the format `["<name_1>(<size_1>)", "<name_2>(<size_2>)", ...]`. Results should be sorted in descending order of file sizes or, in case of ties, lexicographically. Returns an empty list if no files match. |

## Sorting Rules

1. Sort by size in descending order (largest first)
2. In case of size ties, sort lexicographically by name (ascending)

## Example

```python
add_file("/root/dir/another_dir/file.mp3", 10)
add_file("/root/file.mp3", 5)
add_file("/root/music/file.mp3", 7)
copy_file("/root/music/file.mp3", "/root/dir/file.mp3")

find_file("/root", ".mp3")
# → ["/root/dir/another_dir/file.mp3(10)",
#    "/root/dir/file.mp3(7)",
#    "/root/music/file.mp3(7)",
#    "/root/file.mp3(5)"]

find_file("/root", ".file.txt")  # → []
find_file("/dir", "file.mp3")     # → []
```

## Note
All Level 1 methods (add_file, copy_file, get_file_size) must still work.
