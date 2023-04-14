from pydantic import BaseModel


class TreatmentHistory(BaseModel):
    treatmentteeth: int
    tooth_id: int
    complaint_id: str
    treatment_id: str
    filling_id: str
    cleaning_agent_id: str
    extraction_id: str
