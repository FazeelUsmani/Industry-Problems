class CloudStorage:
    def __init__(self):
        self._files = {}

    def add_file(self, name: str, size: int) -> bool:
        """
        Add a new file `name` of `size` bytes.
        Fails if a file with the same name already exists.
        """
        if name in self._files:
            return False
        self._files[name] = size
        return True

    def copy_file(self, name_from: str, name_to: str) -> bool:
        """
        Copy file at `name_from` to `name_to`.
        Fails if source doesn't exist or destination already exists.
        """
        if name_from not in self._files:
            return False
        if name_to in self._files:
            return False
        self._files[name_to] = self._files[name_from]
        return True

    def get_file_size(self, name: str):
        """
        Return size of file `name` if it exists, else None.
        """
        return self._files.get(name, None)
