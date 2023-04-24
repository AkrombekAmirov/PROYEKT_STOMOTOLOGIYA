from sqlmodel import SQLModel, Field, ForeignKey, ARRAY, Integer, Column
from sqlalchemy.dialects import postgresql
from datetime import datetime
from typing import List


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


class TreatmentTeeth(SQLModel, table=True):  # kasallik kartasini ochish
    id: int = Field(primary_key=True, index=True)
    created_by: int = Field(nullable=True)
    patient_id: int = Field(ForeignKey("patients.id"), index=True)
    attached_id: int = Field(nullable=True)
    date_of_treatment: str = Field(default=datetime.now().strftime("%Y-%m-%d"))
    price: str = Field(default='0')
    description: str = Field(default=None)
    doctor_description: str = Field(default=None)


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
    treatmentteeth: int
    tooth_id: List[int] = Field(sa_column=Column(postgresql.ARRAY(Integer)))
    complaint_id: str
    treatment_id: str = Field(default=None)
    filling_id: str = Field(default=None)
    cleaning_agent_id: str = Field(default=None)
    extraction_id: str = Field(default=None)
    created_by: int
    date_of_creation: str = Field(default=datetime.now().strftime("%Y-%m-%d"))


class QueuePatient(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    queue_number: int = Field(default=0)
    patient_id: int = Field(nullable=True)
    doctor_id: int
