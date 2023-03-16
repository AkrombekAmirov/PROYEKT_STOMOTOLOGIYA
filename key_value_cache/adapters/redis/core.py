from key_value_cache.domain import KeyValueCache
from json import dumps, loads
from redis import Redis


class RedisKeyValueCache(KeyValueCache):
    def __init__(self, URL):
        self.redis: Redis = Redis.from_url(URL)

    def get(self, key: str) -> str:
        return loads(self.redis.get(key).decode())

    def set(self, key: str, value=None, ex=24 * 3600) -> None:
        self.redis.set(key, dumps(value), ex=ex)

    def expire(self, key: str, ex=0) -> None:
        self.redis.expire(key, time=ex)

    def exists(self, key: str) -> bool:
        return bool(self.redis.exists(key))
