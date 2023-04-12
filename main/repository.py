from key_value_cache.adapters.inmemory import InMemoryKeyValueCache
from key_value_cache.adapters.redis import RedisKeyValueCache
from patient_repository import PatientRepository
from user_repository import UserRepository
from .config import (
    engine,
    TOKEN_CACHE_URL,
    ATTEMPT_CACHE_URL
)

user_repository = UserRepository(engine=engine)
patient_repository = PatientRepository(engine=engine)
token_cache = RedisKeyValueCache(TOKEN_CACHE_URL)
