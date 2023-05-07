from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

algorithm = environ.get("ALGORITHM")
secret_key = environ.get("SECRET_KEY")
# TOKEN_CACHE_URL = environ.get("TOKEN_CACHE_URL")
# ATTEMPT_CACHE_URL = environ.get("ATTEMPT_CACHE_URL")
expire_time = environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")

engine = create_engine(environ.get("DATABASE_URL"))
