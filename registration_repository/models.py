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
    complaint_id: List[str] = []
    # treatment_id: str
    # filling_id: str
    # cleaning_agent_id: str
    # extraction_id: str


class UpdateTreatmentHistory(BaseModel):
    tooth_id: List[int] = []
    complaint_id: List[str] = []
    treatment_id: List[str] = []
    filling_id: List[str] = []
    cleaning_agent_id: List[str] = []
    extraction_id: List[str] = []


class Create_Object(BaseModel):
    table_name: str
    name: str
    price: str
