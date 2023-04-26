from fastapi import APIRouter, Body, UploadFile, HTTPException, status
from .core import AuthorizedRegisterService, RegisterServiceContext
from .models import PatientsCreate, TreatmentHistory, Create_Object
from fastapi.params import Header, Depends
from typing import List, Optional
from gzip import compress

FILE_SIZE = 5242880
CHUNK_SIZE = 262144


def AuthorizedRegisterServiceRouter(authorized_register_service: AuthorizedRegisterService):
    router = APIRouter(prefix='/register')

    async def context_(token=Header(...)):
        return authorized_register_service.context(token=token)

    @router.post('/create_patient', description='yangi kelgan bemorni ruyhatga olish!')
    async def create_patient(patient: PatientsCreate, context: RegisterServiceContext = Depends(context_)):
        return context.create_patient(patient=patient)

    @router.get('/get_patients')
    async def get_patients(context: RegisterServiceContext = Depends(context_)):
        return context.get_patients()

    @router.get('/get_patient')
    async def get_patient(id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_patient(id=id)

    @router.post('/create_treatmentteeth', description='bugungi kun uchun karta ochish (bugun uchun bitta ochishi lozim ikkita bulsa conflict bulib qoladi)')
    async def create_treatmentteeth(patient_id: int, attached_id: int, description: Optional[str] = None,
                                    context: RegisterServiceContext = Depends(context_)):
        return context.create_treatmentteeth(patient_id=patient_id, attached_id=attached_id, description=description)

    @router.get('/get_treatment')
    async def get_treatment(patient_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_treatment(patient_id=patient_id)

    @router.get('/get_treatments')
    async def get_treatments(patient_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_treatments(patient_id=patient_id)

    @router.post('/create_history', description='Bemorga kasallik tashxislarini yozish')
    async def create_history(treatment_history: List[TreatmentHistory],
                             context: RegisterServiceContext = Depends(context_)):
        for treatment_history_ in treatment_history:
            context.create_history(treatment_history=treatment_history_)

    @router.post('/create_obj', description="[Fillings, CleaningAgents, Extractions, DentalComplaints] Tanlangan xizmatni yaratish!")
    async def create_obj(create_obj: Create_Object, context: RegisterServiceContext = Depends(context_)):
        return context.create_obj(create_obj)

    @router.get('/get_dentalComplaints')
    async def get_dentalComplaints(context: RegisterServiceContext = Depends(context_)):
        return context.get_objs(table_name='DentalComplaints')

    @router.post('/create_file', description="bemor uchun file yuklash ")
    async def create_file(patient_id: int, images: List[UploadFile],
                          context: RegisterServiceContext = Depends(context_)):
        zipped_files = []
        for image in images:
            zipped_files.append((compress(await image.read()), image.content_type))
            if len(compress(await image.read())) > FILE_SIZE: raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"image size should be less than {FILE_SIZE // 10224}kb!")
        return {"data": [context.create_file(patient_id=patient_id, image=image[0], content_type=image[1]) for image in
                         zipped_files]}

    @router.get('/get_file', description="file_uuid ga asosan fileni ko'rish api!")
    async def get_file(file_uuid: str, context: RegisterServiceContext = Depends(context_)):
        return context.get_file(file_uuid)

    @router.get('/get_files', description=' bemorni barcha filelar ruyhatini ko\'rish')
    async def get_files(patient_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_files(patient_id=patient_id)

    @router.get('/get_doctors', description="doctor ruyxatini qaytaradi!")
    async def get_doctors(context: RegisterServiceContext = Depends(context_)):
        return context.get_doctors()

    @router.post('/create_queue', description='navbat yaratish')
    async def create_queue(patient_id: int, doctor_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.create_queue(patient_id=patient_id, doctor_id=doctor_id)

    @router.get('/get_queue', description="navbatni ko'rish")
    async def get_queue(doctor_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_queue(doctor_id=doctor_id)

    return router
