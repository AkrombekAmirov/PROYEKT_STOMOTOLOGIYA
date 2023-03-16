from pydantic import BaseModel
from typing import List, Dict


class PatientsCreate(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str


# class TreatmentRecords(BaseModel):
#     records: List[Dict[int, int]]
class TreatmentRecords(BaseModel):
    complaint_id: int
    tooth_id: int
