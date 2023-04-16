from .core import AuthorizedRegisterService, RegisterServiceContext
from fastapi.params import Header, Depends
from .models import PatientsCreate, TreatmentHistory, Create_Object
from fastapi import APIRouter, Body
from typing import List


def AuthorizedRegisterServiceRouter(authorized_register_service: AuthorizedRegisterService):
    router = APIRouter(prefix='/register')

    async def context_(token=Header(...)):
        return authorized_register_service.context(token=token)

    @router.post('/create_patient')
    async def create_patient(patient: PatientsCreate, context: RegisterServiceContext = Depends(context_)):
        return context.create_patient(patient=patient)

    @router.get('/get_patients')
    async def get_patients(context: RegisterServiceContext = Depends(context_)):
        return context.get_patients()

    @router.get('/get_patient')
    async def get_patient(id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_patient(id=id)

    @router.post('/create_treatmentteeth')
    async def create_treatmentteeth(patient_id: int, attached_id: int,
                                    context: RegisterServiceContext = Depends(context_)):
        return context.create_treatmentteeth(patient_id=patient_id, attached_id=attached_id)

    @router.get('/get_treatment')
    async def get_treatment(patient_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_treatment(patient_id=patient_id)

    @router.get('/get_treatments')
    async def get_treatments(patient_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_treatments(patient_id=patient_id)

    # @router.post('/treatment_records')
    # async def treatment_records(treatment_id: int, treatment: List[TreatmentRecords],
    #                             context: RegisterServiceContext = Depends(context_)):
    #     return context.treatment_records(treatment_id=treatment_id, treatments=treatment)
    #
    # @router.get('/get_treatment_records')
    # async def get_treatment_records(treatment_id: int, context: RegisterServiceContext = Depends(context_)):
    #     return context.get_treatment_records(treatment_id=treatment_id)
    #
    # @router.post('/create_dental_complaints')
    # async def create_dental_complaints(complaint_name: str, price: str,
    #                                    context: RegisterServiceContext = Depends(context_)):
    #     return context.create_dental_complaints(complaint_name=complaint_name, price=price)

    @router.post('/create_history')
    async def create_history(treatment_history: List[TreatmentHistory],
                             context: RegisterServiceContext = Depends(context_)):
        for treatment_history_ in treatment_history:
            context.create_history(treatment_history=treatment_history_)

    @router.post('/create_obj', description="Fillings, CleaningAgents, Extractions, DentalComplaints")
    async def create_obj(create_obj: Create_Object, context: RegisterServiceContext = Depends(context_)):
       return context.create_obj(create_obj)

    # @router.post('/create_treatments')
    # async def create_treatments(name: str, price: str, context: RegisterServiceContext = Depends(context_)):
    #     return context.create_obj(table_name='Treatments', name=name, price=price)
    #
    # @router.post('/create_fillings')
    # async def create_fillings(name: str, price: str, context: RegisterServiceContext = Depends(context_)):
    #     return context.create_obj(table_name='Fillings', name=name, price=price)
    #
    # @router.post('/create_cleaning_agents')
    # async def create_create_cleaning_agents(name: str, price: str, context: RegisterServiceContext = Depends(context_)):
    #     return context.create_obj(table_name='CleaningAgents', name=name, price=price)
    #
    # @router.post('/create_extractions')
    # async def create_create_cleaning_agents(name: str, price: str, context: RegisterServiceContext = Depends(context_)):
    #     return context.create_obj(table_name='Extractions', name=name, price=price)
    #
    # @router.post('/create_dental_complaints')
    # async def create_dental_complaints(name: str, price: str, context: RegisterServiceContext = Depends(context_)):
    #     return context.create_obj(table_name='DentalComplaints', name=name, price=price)

    @router.post('/create_queue')
    async def create_queue(patient_id: int, doctor_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.create_queue(patient_id=patient_id, doctor_id=doctor_id)

    @router.get('/get_queue')
    async def get_queue(doctor_id: int, context: RegisterServiceContext = Depends(context_)):
        return context.get_queue(doctor_id=doctor_id)

    return router
