from user_repository import UserRepository, User
from auth_service import AuthService


class AdminService:
    def __init__(self,
                 user_repository: UserRepository,
                 ):
        self.user_repository = user_repository

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

    def delete_user(self, id):
        return self.service.user_repository.delete_user(id)
