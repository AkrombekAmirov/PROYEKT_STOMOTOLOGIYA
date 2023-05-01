from registration_repository.models import TreatmentHistory, Create_Object, UpdateTreatmentHistory
from .core import AuthorizedDoktorService, DoktorServiceContext
from fastapi.params import Depends, Header
from fastapi import APIRouter
from typing import List


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
    async def update_history(treatmentteeth_id: int, history: UpdateTreatmentHistory, context: DoktorServiceContext = Depends(context_)):
        return context.update_history(treatmentteeth_id=treatmentteeth_id,history=history)

    @router.get('/get_treatment')
    async def get_treatment(patient_id: int, context: DoktorServiceContext = Depends(context_)):
        return context.get_treatment(patient_id=patient_id)

    @router.get('/get_treatment_day')
    async def get_treatment_(patient_id: int, context: DoktorServiceContext = Depends(context_)):
        return context.get_treatment_(patient_id=patient_id)

    @router.get('/get_patients')
    async def get_patients(context: DoktorServiceContext = Depends(context_)):
        return context.get_patients()

    @router.get('/get_patient')
    async def get_patient(id: int, context: DoktorServiceContext = Depends(context_)):
        return context.get_patient(id=id)
    @router.get('/get_obj', description="[Fillings, CleaningAgents, Extractions, DentalComplaints] Tanlangan xizmatni yaratish!")
    async def get_obj(table_name: str, context: DoktorServiceContext = Depends(context_)):
        return context.get_obj(table_name=table_name)

    return router
