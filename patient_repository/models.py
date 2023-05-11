from sqlmodel import SQLModel, Field, ForeignKey, ARRAY, Integer, Column, String
from sqlalchemy.dialects import postgresql
from pydantic import BaseModel
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


class DentalComplaints(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)  # koreyc pulpit periodantint tishsizlik
    name: str
    price: str


class TreatmentHistory(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    treatmentteeth: int
    tooth_id: List[int] = Field(sa_column=Column(postgresql.ARRAY(Integer)))
    complaint_id: List[str] = Field(sa_column=Column(postgresql.ARRAY(String)))
    treatment_id: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String)))
    filling_id: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String)))
    cleaning_agent_id: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String)))
    extraction_id: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String)))
    created_by: int
    date_of_creation: str = Field(default=datetime.now().strftime("%Y-%m-%d"))


class QueuePatient(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    queue_number: int = Field(default=0)
    patient_id: int = Field(nullable=True)
    doctor_id: int


class Treatment(BaseModel):
    id: int
    name: str
    price: str


class TreatmentHistoryDetails(BaseModel):
    treatmentteeth: int
    tooth_id: list[int]
    complaint_id: list[Treatment]
    treatment_id: list[Treatment]
    filling_id: list[Treatment]
    cleaning_agent_id: list[Treatment]
    extraction_id: list[Treatment]
    created_by: int
    date_of_creation: str


class TreatmentHistory_(BaseModel):
    treatmentteeth: int
    date_of_creation: str
    details: TreatmentHistoryDetails
    id: int
    created_by: int


class TreatmentTeeth_(BaseModel):
    id: int
    date_of_treatment: str
    patient_id: int
    description: str
    attached_id: int
    price: str
    doctor_description: str
    created_by: int

#
# class TreatmentInfo(BaseModel):
#     treatment_teeth: Treatments
#     treatment_history: List[]

# def get_treatment_(self, **kwargs):
#     session = Session(bind=self.engine)
#     results = []
#     treatmentteeth = session.query(TreatmentTeeth).filter_by(**kwargs).first()
#     if treatmentteeth:
#         treatment_history = session.query(TreatmentHistory).filter_by(treatmentteeth=treatmentteeth.id).first()
#         if treatment_history:
#             complaint_ids = treatment_history.details.complaint_id
#             complaints = session.query(DentalComplaints).filter(DentalComplaints.id.in_(complaint_ids)).all()
#             complaint_data = [Complaint(id=c.id, name=c.name, price=c.price) for c in complaints]
#             filling_ids = treatment_history.details.filling_id
#             fillings = session.query(Fillings).filter(Fillings.id.in_(filling_ids)).all()
#             filling_data = [Treatment(id=f.id, name=f.name, price=f.price) for f in fillings]
#             cleaning_agent_ids = treatment_history.details.cleaning_agent_id
#             cleaning_agents = session.query(CleaningAgents).filter(CleaningAgents.id.in_(cleaning_agent_ids)).all()
#             cleaning_agent_data = [Treatment(id=c.id, name=c.name, price=c.price) for c in cleaning_agents]
#             extraction_ids = treatment_history.details.extraction_id
#             extractions = session.query(Extractions).filter(Extractions.id.in_(extraction_ids)).all()
#             extraction_data = [Treatment(id=e.id, name=e.name, price=e.price) for e in extractions]
#             treatment_data = treatment_history.details.treatment_id
#             tooth_ids = treatment_history.details.tooth_id
#             created_by = treatment_history.details.created_by
#             treatment_history_data = TreatmentHistory(treatmentteeth=treatment_history.treatmentteeth,
#                                                       date_of_creation=treatment_history.date_of_creation,
#                                                       details=TreatmentHistoryDetails(tooth_id=tooth_ids,
#                                                                                       complaint_id=complaint_data,
#                                                                                       treatment_id=treatment_data,
#                                                                                       filling_id=filling_data,
#                                                                                       cleaning_agent_id=cleaning_agent_data,
#                                                                                       extraction_id=extraction_data,
#                                                                                       created_by=created_by),
#                                                       id=treatment_history.id,
#                                                       created_by=treatment_history.created_by)
#             results.append({"treatmentteeth": treatmentteeth, "treatment_history": treatment_history_data})
#     return r
