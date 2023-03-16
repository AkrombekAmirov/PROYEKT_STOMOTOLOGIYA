from sqlmodel import SQLModel, Field, ForeignKey
from datetime import datetime


class Patients(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    created_by: str
    first_name: str
    last_name: str
    address: str
    phone_number: str
    date_of_creation: datetime = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class DentalComplaints(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)  # koreyc pulpit periodantint tishsizlik
    complaint_name: str
    price: str


class TreatmentTeeth(SQLModel, table=True):  # kasallik ochish
    id: int = Field(primary_key=True, index=True)
    created_by: int = Field(nullable=True)
    patient_id: int = Field(ForeignKey("patients.id"), index=True)
    attached_id: int = Field(nullable=True)
    date_of_treatment: str = Field(default=datetime.now().strftime("%Y-%m-%d"))
    price: str = Field(default='0')


class TreatmentRecords(SQLModel, table=True):  # shikoyatlari misol uchun tish yuqligi
    id: int = Field(primary_key=True, index=True)
    treatmentteeth: int
    complaint_id: str = Field(ForeignKey("dental_complaints.id"), index=True)
    tooth_id: int = Field(ForeignKey("teeth.id"), index=True)


class Treatments(SQLModel, table=True):  # plomba
    id: int = Field(primary_key=True, index=True)
    name: str
    price: str


class Fillings(SQLModel, table=True):  # pulpit
    id: int = Field(primary_key=True, index=True)
    name: str
    price: str


class CleaningAgents(SQLModel, table=True):  # yuvish antiseptik
    id: int = Field(primary_key=True, index=True)
    name: str
    price: str


class Extractions(SQLModel, table=True):  # protezlar
    id: int = Field(primary_key=True, index=True)
    name: str
    price: str


class TreatmentHistory(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    treatment_record_id: int = Field(ForeignKey("treatment_records.id"), index=True)
    treatment_id: str = Field(ForeignKey("treatments.id"), index=True)
    filling_id: str = Field(ForeignKey("fillings.id"))
    cleaning_agent_id: str = Field(ForeignKey("cleaning_agents.id"))
    extraction_id: str = Field(ForeignKey("extractions.id"))
    created_by: int = Field(nullable=True)
    date_of_creation: str = Field(default=datetime.now().strftime("%Y-%m-%d"))
