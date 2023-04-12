from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

TOKEN_CACHE_URL = environ.get("TOKEN_CACHE_URL")
ATTEMPT_CACHE_URL = environ.get("ATTEMPT_CACHE_URL")

engine = create_engine(environ.get("DATABASE_URL"))
