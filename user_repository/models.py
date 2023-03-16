from sqlmodel import SQLModel, Field
from datetime import datetime


class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    role: str
    first_name: str
    last_name: str
    username: str
    password: str
    address: str
    phone_number: str
    created_date: datetime = Field(default=datetime.now().strftime("%Y-%m-%d"), index=True)
