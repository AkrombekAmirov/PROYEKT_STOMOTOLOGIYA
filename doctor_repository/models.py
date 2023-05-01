from pydantic import BaseModel
from typing import List


class TreatmentHistory(BaseModel):
    treatmentteeth: int
    tooth_id: List[int] = []
    complaint_id: List[str] = []
    treatment_id: str
    filling_id: str
    cleaning_agent_id: str
    extraction_id: str
