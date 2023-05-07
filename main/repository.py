from key_value_cache.adapters.inmemory import InMemoryKeyValueCache
from key_value_cache.adapters.redis import RedisKeyValueCache
from patient_repository import PatientRepository
from user_repository import UserRepository
from file_repository import FileService
from .config import (
    engine
    # TOKEN_CACHE_URL,
    # ATTEMPT_CACHE_URL
)

file_repository = FileService(engine=engine)
user_repository = UserRepository(engine=engine)
# token_cache = RedisKeyValueCache(TOKEN_CACHE_URL)
patient_repository = PatientRepository(engine=engine)
