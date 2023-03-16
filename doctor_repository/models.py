from pydantic import BaseModel


class CreateTreatmentHistory(BaseModel):
    treatment_record_id: int
    treatment_id: str
    filling_id: str
    cleaning_agent_id: str
    extraction_id: str
