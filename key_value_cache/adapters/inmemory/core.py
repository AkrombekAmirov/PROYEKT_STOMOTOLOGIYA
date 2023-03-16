from key_value_cache.domain import KeyValueCache


class InMemoryKeyValueCache(KeyValueCache):
    def __init__(self):
        self.data = dict()

    def get(self, key: str) -> str:
        return self.data[key]

    def set(self, key: str, value: str = '', ex=24 * 3600) -> None:
        self.data[key] = value

    def expire(self, key: str, ex=0) -> None:
        del self.data[key]

    def exists(self, key: str) -> bool:
        return key in self.data
