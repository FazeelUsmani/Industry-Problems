class CloudStorage:
    def __init__(self):
         self._files = {}

    # --- Level 1 ---
    def add_file(self, name: str, size: int) -> bool:
        if name in self._files:
            return False
        self._files[name] = size
        return True

    def copy_file(self, name_from: str, name_to: str) -> bool:
        if name_from not in self._files or name_to in self._files:
            return False
        self._files[name_to] = self._files[name_from]
        return True

    def get_file_size(self, name: str):
        return self._files.get(name, None)

    # --- Level 2 ---
    def find_file(self, prefix: str, suffix: str) -> list[str]:
        """
        Return ["<name>(<size>)", ...] for files whose names start with `prefix`
        and end with `suffix`, sorted by:
          1) size descending
          2) name lexicographically (for ties)
        """
        matches = [
            (name, size)
            for name, size in self._files.items()
            if name.startswith(prefix) and name.endswith(suffix)
        ]
        # size desc, name asc
        matches.sort(key=lambda x: (-x[1], x[0]))
        return [f"{name}({size})" for name, size in matches]
