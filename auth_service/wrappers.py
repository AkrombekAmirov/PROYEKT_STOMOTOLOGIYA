from fastapi.params import Header
from .models import Credentials
from fastapi import APIRouter, Response
from .core import AuthService


def AuthServiceRouter(auth_service: AuthService):
    router = APIRouter()

    @router.get("/token/generate")
    async def generate_token():
        return auth_service.generate_token()

    @router.get("/token/exists")
    async def exists_token(token=Header(...)):
        return auth_service.exists_token(token)

    @router.get("/token/expire")
    async def expire_token(token=Header(...)):
        return auth_service.expire_token(token)

    @router.post("/admin/login")
    async def admin_login(credentials: Credentials, token=Header(...)):
        return auth_service.login_admin(token, credentials)

    @router.post("/register/login")
    async def register_login(credentials: Credentials, token=Header(...)):
        return auth_service.login_register(token, credentials)

    @router.post("/doctor/login")
    async def doctor_login(credentials: Credentials, token=Header(...)):
        return auth_service.login_doctor(token, credentials)

    @router.get("/user/logout")
    async def user_logout(token=Header(...)):
        return auth_service.logout(token)

    return router
