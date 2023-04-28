from patient_repository import PatientRepository
from fastapi.responses import StreamingResponse
from user_repository import UserRepository
from file_repository import FileService
from .models import TreatmentHistory
from auth_service import AuthService
from datetime import datetime
from gzip import decompress
from uuid import uuid4


class RegisterService:
    def __init__(self, patient_repository: PatientRepository, user_repository: UserRepository,
                 file_repository: FileService):
        self.patient_repository = patient_repository
        self.user_repository = user_repository
        self.file_repository = file_repository

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

    def get_patients(self):
        return self.register_service.patient_repository.get_petients()

    def get_patient(self, id: int):
        return self.register_service.patient_repository.get_petient(id=id)

    def create_treatmentteeth(self, patient_id: int, attached_id: int, description: str):
        # if self.register_service.patient_repository.get_treatment(patient_id=patient_id,
        #                                                           date_of_treatment=datetime.now().strftime(
        #                                                               "%Y-%m-%d")):
        #     raise HTTPException(status_code=status.HTTP_409_CONFLICT,
        #                         detail="treatment conflict: bir kunga bitta ochish mumkin!")
        return self.register_service.patient_repository.create_treatmentteeth(patient_id=patient_id,
                                                                              attached_id=attached_id,
                                                                              description=description,
                                                                              created_by=self.register.id)

    def get_treatment(self, patient_id: int):
        return self.register_service.patient_repository.get_treatment(patient_id=patient_id,
                                                                      date_of_treatment=datetime.now().strftime(
                                                                          "%Y-%m-%d"))

    def get_treatments(self, patient_id):
        return self.register_service.patient_repository.get_treatments(patient_id=patient_id)

    def create_history(self, treatment_history: TreatmentHistory):
        return self.register_service.patient_repository.create_history(treatmentteeth=treatment_history.treatmentteeth,
                                                                       tooth_id=treatment_history.tooth_id,
                                                                       complaint_id=treatment_history.complaint_id,
                                                                       treatment_id=treatment_history.treatment_id,
                                                                       filling_id=treatment_history.filling_id,
                                                                       cleaning_agent_id=treatment_history.cleaning_agent_id,
                                                                       extraction_id=treatment_history.extraction_id,
                                                                       created_by=self.register.id)

    def create_file(self, patient_id: int, image: bytes, content_type: str):
        uuid = str(uuid4())
        self.register_service.file_repository.create_file_chunk(image=image, file_uuid=uuid)
        return self.register_service.file_repository.create_file(patient_id=patient_id, content_type=content_type,
                                                                 file_id=uuid)

    def get_file(self, file_uuid: str):
        def iterfile():
            yield decompress(b"".join([element.chunk for element in self.register_service.file_repository.get_file(file_id=file_uuid)]))
        return StreamingResponse(iterfile(), media_type=self.register_service.file_repository.get_file_(file_uuid=file_uuid).content_type)

    def get_files(self, patient_id: int):
        return self.register_service.file_repository.get_files(patient_id=patient_id)

    def get_doctors(self):
        return self.register_service.user_repository.get_doctors(role="doctor")

    def create_obj(self, create_obj):
        return self.register_service.patient_repository.create_obj(create_obj=create_obj)

    def get_objs(self, table_name: str):
        return self.register_service.patient_repository.get_objs(table_name=table_name)

    def create_queue(self, patient_id: int, doctor_id: int):
        return self.register_service.patient_repository.create_queue(patient_id=patient_id, doctor_id=doctor_id)

    def get_queue(self, doctor_id: int):
        return self.register_service.patient_repository.get_queue(doctor_id=doctor_id)
