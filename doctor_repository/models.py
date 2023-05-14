from pydantic import BaseModel
from typing import List


class TreatmentHistory(BaseModel):
    treatmentteeth: int
    tooth_id: List[int] = []
    complaint_id: List[str] = []
    treatment_id: List[str] = []
    filling_id: List[str] = []
    cleaning_agent_id: List[str] = []
    extraction_id: List[str] = []


class Update_Price(BaseModel):
    treatmentteeth_id: int
    price: str
    doctor_description: str
