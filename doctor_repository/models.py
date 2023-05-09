from pydantic import BaseModel
from typing import List


class TreatmentHistory(BaseModel):
    treatmentteeth: int
    tooth_id: List[int] = []
    complaint_id: List[str] = []
    treatment_id: List[str] = []
    treatment_num: int
    filling_id: List[str] = []
    filling_num: int
    cleaning_agent_id: List[str] = []
    cleaning_agent: int
    extraction_id: List[str] = []
    extraction_num: int


class Update_Price(BaseModel):
    treatmentteeth_id: int
    price: str
