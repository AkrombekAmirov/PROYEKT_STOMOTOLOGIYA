from registration_repository.models import Create_Object, Update_Object
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

    @router.put('/update_user')
    async def update_user(user_id: int, user: User, context: AdminServiceContext = Depends(context_)):
        return context.update_user(user_id=user_id, user=user)

    @router.delete("/delete/user")
    async def delete_user(user_id: int, context: AdminServiceContext = Depends(context_)):
        return context.delete_user(id=user_id)

    @router.get('/get_doctors', description="doctor ruyxatini qaytaradi!")
    async def get_doctors(context: AdminServiceContext = Depends(context_)):
        return context.get_doctors()

    @router.post('/create_obj',
                 description="[Fillings, Treatments, CleaningAgents, Extractions, DentalComplaints] Tanlangan xizmatni yaratish!")
    async def create_obj(create_obj: Create_Object, context: AdminServiceContext = Depends(context_)):
        return context.create_obj(create_obj)

    @router.get('/get_obj',
                description="[Fillings, Treatments, CleaningAgents, Extractions, DentalComplaints] Tanlangan xizmatni yaratish!")
    async def get_obj(table_name: str, context: AdminServiceContext = Depends(context_)):
        return context.get_objs(table_name=table_name)

    @router.put('/update_objs',
                description="[Fillings, Treatments, CleaningAgents, Extractions, DentalComplaints] Tanlangan xizmatni yaratish!")
    async def update_objs(update_obj: Update_Object, context: AdminServiceContext = Depends(context_)):
        return context.update_objs(update_obj=update_obj)

    return router
