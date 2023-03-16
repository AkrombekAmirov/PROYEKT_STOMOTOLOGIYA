from patient_repository import PatientRepository
from user_repository import UserRepository
from .models import CreateTreatmentHistory
from fastapi import HTTPException, status
from auth_service import AuthService
from datetime import datetime


class DoktorService:
    def __init__(self, patient_repository: PatientRepository, user_repository: UserRepository):
        self.patient_repository = patient_repository
        self.user_repository = user_repository

    def context(self, doktor):
        if doktor.role != 'doktor': raise Exception('incorrect role')
        return DoktorServiceContext(self, doktor=doktor)


class AuthorizedDoktorService:
    def __init__(self, doktor_service: DoktorService, auth_service: AuthService):
        self.doktor_service = doktor_service
        self.auth_service = auth_service

    def context(self, token):
        return self.doktor_service.context(self.auth_service.retrieve_user(token=token))


class DoktorServiceContext:
    def __init__(self, doktor_service: DoktorService, doktor):
        self.doktor_service = doktor_service
        self.doktor = doktor

    def create_history(self, history: CreateTreatmentHistory):
        self.doktor_service.patient_repository.create_history(treatment_record_id=history.treatment_record_id,
                                                              created_by=self.doktor.id,
                                                              treatment_id=history.treatment_id,
                                                              filling_id=history.filling_id,
                                                              cleaning_agent_id=history.cleaning_agent_id,
                                                              extraction_id=history.extraction_id)

    def get_treatment(self):
        self.doktor_service.patient_repository.get_treatment_(attached_id=self.doktor.id,
                                                              date_of_treatment=datetime.now().strftime("%Y-%m-%d"))

    def get_treatments(self):
        self.doktor_service.patient_repository.get_treatment_(attached_id=self.doktor.id)

    def update_treatment_teeth_one(self, id: int, price: str):
        return self.doktor_service.patient_repository.update_TreatmentTeeth(id=id, price=price)

    # def get_treatment_records(self, treatmentteeth: int):
