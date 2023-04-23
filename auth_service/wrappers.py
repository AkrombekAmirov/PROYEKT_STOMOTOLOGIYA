from fastapi.params import Header
from .models import Credentials
from fastapi import APIRouter, Response
from .core import AuthService


def AuthServiceRouter(auth_service: AuthService):
    router = APIRouter(prefix='/auth')

    # @router.get("/token/generate")
    # async def generate_token():
    #     return auth_service.generate_token()

    @router.get("/token/exists")
    async def exists_token(token=Header(...)):
        return auth_service.exists_token(token)

    @router.get("/token/expire")
    async def expire_token(token=Header(...)):
        return auth_service.expire_token(token)

    @router.post("/login")
    async def login(credentials: Credentials):
        return auth_service._login(credentials)

    @router.get("/user/logout")
    async def user_logout(token=Header(...)):
        return auth_service.logout(token)

    return router
