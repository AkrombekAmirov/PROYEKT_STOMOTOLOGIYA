from registration_repository.models import UpdateTreatmentHistory
from patient_repository import PatientRepository
from fastapi.responses import StreamingResponse
from user_repository import UserRepository
from fastapi import HTTPException, status
from file_repository import FileService
from .models import TreatmentHistory
from auth_service import AuthService
from datetime import datetime
from gzip import decompress
from uuid import uuid4


class DoktorService:
    def __init__(self, patient_repository: PatientRepository, user_repository: UserRepository,
                 file_repository: FileService):
        self.patient_repository = patient_repository
        self.user_repository = user_repository
        self.file_repository = file_repository

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
        return self.doktor_service.patient_repository.create_history(treatmentteeth=treatment_history.treatmentteeth,
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
        return self.doktor_service.patient_repository.gets_history(
            treatmentteeth=self.doktor_service.patient_repository.get_treatment(patient_id=patient_id,
                                                                                date_of_treatment=datetime.now().strftime(
                                                                                    "%Y-%m-%d")).id), self.doktor_service.file_repository.get_files(
            patient_id=patient_id)

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

    def create_file(self, patient_id: int, image: bytes, content_type: str):
        uuid = str(uuid4())
        self.doktor_service.file_repository.create_file_chunk(image=image, file_uuid=uuid)
        return self.doktor_service.file_repository.create_file(patient_id=patient_id, content_type=content_type,
                                                               file_id=uuid)

    def get_file(self, file_uuid: str):
        def iterfile():
            yield decompress(b"".join(
                [element.chunk for element in self.doktor_service.file_repository.get_file(file_id=file_uuid)]))

        return StreamingResponse(iterfile(), media_type=self.doktor_service.file_repository.get_file_(
            file_uuid=file_uuid).content_type)

    def get_files(self, patient_id: int):
        return self.doktor_service.file_repository.get_files(patient_id=patient_id)
