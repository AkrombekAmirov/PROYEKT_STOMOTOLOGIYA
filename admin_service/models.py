from pydantic import BaseModel


class User(BaseModel):
    role: str
    first_name: str
    last_name: str
    username: str
    password: str
    address: str
    phone_number: str
