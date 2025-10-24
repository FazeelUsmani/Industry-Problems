class CloudStorage:
    def __init__(self):
        # name -> (size, owner)
        self._files: dict[str, tuple[int, str]] = {}
        # user -> capacity and used bytes
        self._capacity: dict[str, int] = {}
        self._used: dict[str, int] = {}

    # ---------- Level 1 ----------
    def add_file(self, name: str, size: int) -> bool:
        if name in self._files:
            return False
        self._files[name] = (size, "admin")  # admin has unlimited capacity
        return True

    def copy_file(self, name_from: str, name_to: str) -> bool:
        if name_from not in self._files or name_to in self._files:
            return False
        size, owner = self._files[name_from]
        if owner != "admin":
            # ensure the owner's quota can accommodate the copy
            if self._used.get(owner, 0) + size > self._capacity.get(owner, 0):
                return False
            self._used[owner] = self._used.get(owner, 0) + size
        self._files[name_to] = (size, owner)  # ownership preserved
        return True

    def get_file_size(self, name: str):
        info = self._files.get(name)
        return None if info is None else info[0]

    # ---------- Level 2 ----------
    def find_file(self, prefix: str, suffix: str) -> list[str]:
        matches = [
            (name, size)
            for name, (size, _owner) in self._files.items()
            if name.startswith(prefix) and name.endswith(suffix)
        ]
        matches.sort(key=lambda x: (-x[1], x[0]))  # size desc, name asc
        return [f"{n}({s})" for n, s in matches]

    # ---------- Level 3 ----------
    def add_user(self, user_id: str, capacity: int) -> bool:
        if user_id in self._capacity:
            return False
        self._capacity[user_id] = capacity
        self._used[user_id] = 0
        return True

    def add_file_by(self, user_id: str, name: str, size: int) -> int | None:
        if user_id not in self._capacity:
            return None
        if name in self._files:
            return None
        if self._used[user_id] + size > self._capacity[user_id]:
            return None
        self._files[name] = (size, user_id)
        self._used[user_id] += size
        return self._capacity[user_id] - self._used[user_id]

    def update_capacity(self, user_id: str, capacity: int) -> int | None:
        if user_id not in self._capacity:
            return None
        self._capacity[user_id] = capacity

        files = [(n, sz) for n, (sz, owner) in self._files.items() if owner == user_id]
        total = sum(sz for _, sz in files)
        if total <= capacity:
            self._used[user_id] = total
            return 0

        files.sort(key=lambda x: (-x[1], x[0]))
        removed = 0
        for n, sz in files:
            if total <= capacity:
                break
            del self._files[n]
            total -= sz
            removed += 1

        self._used[user_id] = total
        return removed

    # ---------- Level 4 ----------
    def compress_file(self, user_id: str, name: str) -> int | None:
        if user_id not in self._capacity:
            return None
        info = self._files.get(name)
        if info is None:
            return None
        size, owner = info
        if owner != user_id:
            return None
        new_name = f"{name}.COMPRESSED"
        if new_name in self._files:
            return None

        new_size = size // 2
        delta = new_size - size
        self._files.pop(name)
        self._files[new_name] = (new_size, user_id)
        self._used[user_id] = self._used.get(user_id, 0) + delta
        return self._capacity[user_id] - self._used[user_id]

    def decompress_file(self, user_id: str, name: str) -> int | None:
        if user_id not in self._capacity:
            return None
        info = self._files.get(name)
        if info is None:
            return None
        size, owner = info
        if owner != user_id:
            return None
        if not name.endswith(".COMPRESSED"):
            return None

        base_name = name[:-len(".COMPRESSED")]
        if base_name in self._files:
            return None

        new_size = size * 2
        needed = new_size - size
        if self._used[user_id] + needed > self._capacity[user_id]:
            return None

        self._files.pop(name)
        self._files[base_name] = (new_size, user_id)
        self._used[user_id] += needed
        return self._capacity[user_id] - self._used[user_id]
