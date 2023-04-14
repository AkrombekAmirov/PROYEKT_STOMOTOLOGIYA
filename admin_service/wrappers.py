from .core import AdminServiceContext, AuthorizedAdminService
from fastapi.params import Header, Depends
from .models import User
from fastapi import APIRouter


def AuthorizedAdminServiceRouter(authorized_admin_service: AuthorizedAdminService):
    router = APIRouter(prefix='/admin')

    async def context_(token=Header(...)):
        return authorized_admin_service.context(token)

    @router.post("/user/create")
    async def create_user(user: User, context: AdminServiceContext = Depends(context_)):
        return context.create_user(user=user)

    @router.get("/get/user")
    async def get_user(user_id: int, context: AdminServiceContext = Depends(context_)):
        return context.get_user(user_id=user_id)

    @router.get("/get/users")
    async def get_users(context: AdminServiceContext = Depends(context_)):
        return context.get_users()

    @router.delete("/delete/user")
    async def delete_user(user_id: int, context: AdminServiceContext = Depends(context_)):
        return context.delete_user(id=user_id)

    return router
