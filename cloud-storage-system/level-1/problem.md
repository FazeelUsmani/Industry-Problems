# Level 1 — Basic File Operations

## Overview
Implement a simple cloud storage system that supports adding files, copying files, and retrieving file information.
This is Level 1 of 4. Complete this level to unlock Level 2.

## Requirements

The cloud storage system should support operations to add files, copy files, and get files stored on the system.

**Note:** This system should be in-memory; you do not need to work with the real filesystem.

## Required Methods

| Method | Description |
|--------|-------------|
| `add_file(self, name: str, size: int) -> bool` | Add a new file `name` to the storage. `size` is the amount of memory required in bytes. Returns `True` if the file was added successfully or `False` if a file with the same name already exists. |
| `copy_file(self, name_from: str, name_to: str) -> bool` | Copy the file at `name_from` to `name_to`. Fails if `name_from` doesn't exist or `name_to` already exists. Returns `True` if successful, `False` otherwise. |
| `get_file_size(self, name: str) -> int \| None` | Return the size of the file `name` if it exists, or `None` otherwise. |

## Example

```python
add_file("/dir1/dir2/file.txt", 10)         # → True
copy_file("/not-existing.file", "/dir1/file.txt")  # → False
copy_file("/dir1/dir2/file.txt", "/dir1/file.txt")  # → True
add_file("/dir1/file.txt", 15)               # → False
copy_file("/dir1/file.txt", "/dir1/dir2/file.txt")  # → False
get_file_size("/dir1/file.txt")              # → 10
get_file_size("/not-existing.file")          # → None
```
