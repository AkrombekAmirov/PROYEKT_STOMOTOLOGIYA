from registration_repository.models import TreatmentHistory, UpdateTreatmentHistory
from fastapi import APIRouter, UploadFile, HTTPException, status
from .core import AuthorizedDoktorService, DoktorServiceContext
from fastapi.params import Depends, Header
from gzip import compress
from typing import List

FILE_SIZE = 5242880
CHUNK_SIZE = 262144


def AuthorizedDoktorServiceRouter(authorized_doktor_service: AuthorizedDoktorService):
    router = APIRouter(prefix='/doctor')

    async def context_(token=Header(...)):
        return authorized_doktor_service.context(token=token)

    @router.post('/create_history')
    async def create_history(history: TreatmentHistory, context: DoktorServiceContext = Depends(context_)):
        return context.create_history(treatment_history=history)

    @router.get('/get_history')
    async def get_history(treatmentteeth_id: int, context: DoktorServiceContext = Depends(context_)):
        return context.get_history(treatmentteeth_id=treatmentteeth_id)

    @router.put('/update_history')
    async def update_history(treatmentteeth_id: int, history: UpdateTreatmentHistory,
                             context: DoktorServiceContext = Depends(context_)):
        return context.update_history(treatmentteeth_id=treatmentteeth_id, history=history)

    @router.get('/get_treatment')
    async def get_treatment(patient_id: int, context: DoktorServiceContext = Depends(context_)):
        return context.get_treatment(patient_id=patient_id)

    @router.get('/get_treatment_day', description='Bemorning bugungi kasallik tashxisini qaytaradi!')
    async def get_treatment_(patient_id: int, context: DoktorServiceContext = Depends(context_)):
        return context.get_treatment_(patient_id=patient_id)

    @router.get('/get_patients')
    async def get_patients(context: DoktorServiceContext = Depends(context_)):
        return context.get_patients()

    @router.get('/get_patient')
    async def get_patient(id: int, context: DoktorServiceContext = Depends(context_)):
        return context.get_patient(id=id)

    @router.get('/get_obj',
                description="[Fillings, Treatments, CleaningAgents, Extractions, DentalComplaints] Tanlangan xizmatni yaratish!")
    async def get_obj(table_name: str, context: DoktorServiceContext = Depends(context_)):
        return context.get_obj(table_name=table_name)

    @router.post('/create_file', description="bemor uchun file yuklash ")
    async def create_file(patient_id: int, images: List[UploadFile],
                          context: DoktorServiceContext = Depends(context_)):
        zipped_files = []
        for image in images:
            zipped_files.append((compress(await image.read()), image.content_type))
            if len(compress(await image.read())) > FILE_SIZE: raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"image size should be less than {FILE_SIZE // 10224}kb!")
        return {"data": [context.create_file(patient_id=patient_id, image=image[0], content_type=image[1]) for image in
                         zipped_files]}

    @router.get('/get_file', description="file_uuid ga asosan fileni ko'rish api!")
    async def get_file(file_uuid: str, context: DoktorServiceContext = Depends(context_)):
        return context.get_file(file_uuid)

    @router.get('/get_files', description=' bemorni barcha filelar ruyhatini ko\'rish')
    async def get_files(patient_id: int, context: DoktorServiceContext = Depends(context_)):
        return context.get_files(patient_id=patient_id)

    return router
