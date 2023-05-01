from registration_repository.models import TreatmentHistory, UpdateTreatmentHistory
from patient_repository import PatientRepository
from user_repository import UserRepository
from fastapi import HTTPException, status
from auth_service import AuthService
from datetime import datetime


class DoktorService:
    def __init__(self, patient_repository: PatientRepository, user_repository: UserRepository):
        self.patient_repository = patient_repository
        self.user_repository = user_repository

    def context(self, doktor):
        if doktor.role != 'doctor': raise Exception('incorrect role')
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

    def create_history(self, treatment_history: TreatmentHistory):
        self.doktor_service.patient_repository.create_history(treatmentteeth=treatment_history.treatmentteeth,
                                                              tooth_id=treatment_history.tooth_id,
                                                              complaint_id=treatment_history.complaint_id,
                                                              treatment_id=treatment_history.treatment_id,
                                                              filling_id=treatment_history.filling_id,
                                                              cleaning_agent_id=treatment_history.cleaning_agent_id,
                                                              extraction_id=treatment_history.extraction_id,
                                                              created_by=self.doktor.id)

    def get_history(self, treatmentteeth_id: int):
        return self.doktor_service.patient_repository.gets_history(treatmentteeth=treatmentteeth_id)

    def update_history(self, treatmentteeth_id: int, history: UpdateTreatmentHistory):
        return self.doktor_service.patient_repository.update_history(treatmentteeth_id=treatmentteeth_id,
                                                                     tooth_id=history.tooth_id,
                                                                     complaint_id=history.complaint_id,
                                                                     treatment_id=history.treatment_id,
                                                                     filling_id=history.filling_id,
                                                                     cleaning_agent_id=history.cleaning_agent_id,
                                                                     extraction_id=history.extraction_id)

    def get_treatment(self, patient_id: int):
        return self.doktor_service.patient_repository.get_treatment_(patient_id=patient_id)

    def get_treatment_(self, patient_id: int):
        return self.doktor_service.patient_repository.get_treatment(patient_id=patient_id,
                                                                    date_of_treatment=datetime.now().strftime(
                                                                        "%Y-%m-%d"))

    def get_treatments(self):
        return self.doktor_service.patient_repository.get_treatment_(attached_id=self.doktor.id)

    def update_treatment_teeth_one(self, id: int, price: str):
        return self.doktor_service.patient_repository.update_TreatmentTeeth(id=id, price=price)

    def get_patients(self):
        return self.doktor_service.patient_repository.get_petients()

    def get_patient(self, id: int):
        return self.doktor_service.patient_repository.get_petient(id=id)

    def get_obj(self, table_name: str):
        return self.doktor_service.patient_repository.get_objs(table_name=table_name)
