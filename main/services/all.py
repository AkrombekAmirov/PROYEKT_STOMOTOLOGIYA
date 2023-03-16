from ..repository import user_repository, token_cache, patient_repository
from registration_repository.core import RegisterService
from doctor_repository.core import DoktorService
from admin_service.core import AdminService
from auth_service.core import AuthService
from token_manager import TokenManager
register_service = RegisterService(patient_repository=patient_repository, user_repository=user_repository)
doctor_service = DoktorService(patient_repository=patient_repository, user_repository=user_repository)
auth_service = AuthService(token_cache=token_cache, user_repository=user_repository)
admin_service = AdminService(user_repository=user_repository)
token_manager = TokenManager("test_secret")
