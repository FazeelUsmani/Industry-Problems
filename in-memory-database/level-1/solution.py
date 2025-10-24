class InMemoryDB:
    def __init__(self):
        self.data = {}

    def set(self, key: str, field: str, value: str) -> None:
        if key not in self.data:
            self.data[key] = {}
        self.data[key][field] = value

    def get(self, key: str, field: str):
        return self.data.get(key, {}).get(field)

    def delete(self, key: str, field: str) -> bool:
        if key in self.data and field in self.data[key]:
            del self.data[key][field]
            return True
        return False
