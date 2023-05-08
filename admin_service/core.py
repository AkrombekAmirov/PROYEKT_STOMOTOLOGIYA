from patient_repository import PatientRepository
from user_repository import UserRepository, User
from auth_service import AuthService


class AdminService:
    def __init__(self,
                 user_repository: UserRepository, patient_repository: PatientRepository
                 ):
        self.user_repository = user_repository
        self.patient_repository = patient_repository

    def context(self, user):
        if user.role != "admin": raise Exception("incorrect role")
        return AdminServiceContext(self, user)


class AuthorizedAdminService:
    def __init__(self, admin_service: AdminService, auth_service: AuthService):
        self.admin_service = admin_service
        self.auth_service = auth_service

    def context(self, token):
        return self.admin_service.context(self.auth_service.retrieve_user(token))


class AdminServiceContext:
    def __init__(self, admin_service: AdminService, admin) -> None:
        self.service = admin_service
        self.admin = admin

    def create_user(self, user):
        return self.service.user_repository.create_user(User(**user.dict())).id

    def get_user(self, user_id: int):
        return self.service.user_repository.get_user(id=user_id)

    def get_users(self):
        return self.service.user_repository.get_users()

    def update_user(self, user_id: int, user):
        return self.service.user_repository.update_user(user_id=user_id, user=user)

    def delete_user(self, id):
        return self.service.user_repository.delete_user(id)

    def get_doctors(self):
        return self.service.user_repository.get_doctors(role="doctor")

    def create_obj(self, create_obj):
        return self.service.patient_repository.create_obj(create_obj=create_obj)

    def get_objs(self, table_name: str):
        return self.service.patient_repository.get_objs(table_name=table_name)

    def update_objs(self, update_obj):
        return self.service.patient_repository.update_objs(update_obj)
