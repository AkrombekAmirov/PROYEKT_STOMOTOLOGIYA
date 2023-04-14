from .core import AuthorizedDoktorService, DoktorServiceContext
from .models import TreatmentHistory
from fastapi.params import Depends, Header
from fastapi import APIRouter
from typing import List


def AuthorizedDoktorServiceRouter(authorized_doktor_service: AuthorizedDoktorService):
    router = APIRouter(prefix='/doctor')

    async def context_(token=Header(...)):
        return authorized_doktor_service.context(token=token)

    @router.post('/create_history')
    async def create_history(history: List[TreatmentHistory], context: DoktorServiceContext = Depends(context_)):
        for treatment_history_ in history:
            context.create_history(treatment_history=treatment_history_)

    @router.get('/get_treatment')
    async def get_treatment(context: DoktorServiceContext = Depends(context_)):
        return context.get_treatment()

    # @router.get('/get_treatments')
    # async def get_treatments()

    return router
