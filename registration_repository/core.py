from fastapi import HTTPException, status
from patient_repository import PatientRepository
from user_repository import UserRepository
from auth_service import AuthService
from datetime import datetime


class RegisterService:
    def __init__(self, patient_repository: PatientRepository, user_repository: UserRepository):
        self.patient_repository = patient_repository
        self.user_repository = user_repository

    def context(self, register):
        if register.role != "register": raise Exception("incorrect role")
        return RegisterServiceContext(self, register)


class AuthorizedRegisterService:
    def __init__(self, register_service: RegisterService, auth_service: AuthService):
        self.register_service = register_service
        self.auth_service = auth_service

    def context(self, token):
        return self.register_service.context(self.auth_service.retrieve_user(token))


class RegisterServiceContext:
    def __init__(self, register_service: RegisterService, register):
        self.register_service = register_service
        self.register = register

    def create_patient(self, patient):
        return self.register_service.patient_repository.create_petient(petient=patient, created_by=self.register.id)

    def create_treatmentteeth(self, patient_id: int, attached_id: int):
        if self.register_service.patient_repository.get_treatment(patient_id=patient_id,
                                                                  date_of_treatment=datetime.now().strftime(
                                                                      "%Y-%m-%d")):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="treatment conflict: bir kunga bitta ochish mumkin!")
        return self.register_service.patient_repository.create_treatmentteeth(patient_id=patient_id,
                                                                              attached_id=attached_id,
                                                                              created_by=self.register.id)

    def get_treatment(self, patient_id: int):
        return self.register_service.patient_repository.get_treatment(patient_id=patient_id,
                                                                      date_of_treatment=datetime.now().strftime(
                                                                          "%Y-%m-%d"))

    def get_treatments(self, patient_id):
        return self.register_service.patient_repository.get_treatments(patient_id=patient_id)

    def create_dental_complaints(self, complaint_name, price):
        return self.register_service.patient_repository.create_dental_complaints(complaint_name=complaint_name, price=price)

    def treatment_records(self, treatment_id: int, treatments):
        for treatment in treatments:
            self.register_service.patient_repository.TreatmentRecords(treatmentteeth=treatment_id,
                                                                      complaint_id=treatment.complaint_id,
                                                                      tooth_id=treatment.tooth_id, notes='salom')

    def get_treatment_records(self, treatment_id: int):
        return self.register_service.patient_repository.get_treatment_records(treatmentteeth=treatment_id)

    def create_obj(self, table_name: str, name: str, price: str):
        return self.register_service.patient_repository.create_obj(table_name=table_name, name=name, price=price)
