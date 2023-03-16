from .core import AuthorizedDoktorService, DoktorServiceContext
from .models import CreateTreatmentHistory
from fastapi.params import Depends, Header
from fastapi import APIRouter
from typing import List


def AuthorizedDoktorServiceRouter(authorized_doktor_service: AuthorizedDoktorService):
    router = APIRouter(prefix='/doctor')

    async def context_(token=Header(...)):
        return authorized_doktor_service.context(token=token)

    @router.post('/create_history')
    async def create_history(history: CreateTreatmentHistory, context: DoktorServiceContext = Depends(context_)):
        return context.create_history(history=history)

    @router.get('/get_treatment')
    async def get_treatment(context: DoktorServiceContext = Depends(context_)):
        return context.get_treatment()

    return router
