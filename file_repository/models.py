from sqlmodel import SQLModel, Field
from datetime import datetime


class FileChunk(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    file_id: str
    chunk: bytes


class FileRepository(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    patient_id: int
    content_type: str
    file_id: str
    date: str = Field(default=datetime.now().strftime("%Y-%m-%d"))
