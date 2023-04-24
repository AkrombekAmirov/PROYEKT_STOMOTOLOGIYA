from pydantic import BaseModel
from typing import List


class PatientsCreate(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str


class TreatmentHistory(BaseModel):
    treatmentteeth: int
    tooth_id: List[int] = []
    complaint_id: str
    treatment_id: str
    filling_id: str
    cleaning_agent_id: str
    extraction_id: str

class Create_Object(BaseModel):
    table_name: str
    name: str
    price: str
