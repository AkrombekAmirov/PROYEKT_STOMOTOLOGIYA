from ..repository import user_repository, token_cache, patient_repository, file_repository
from registration_repository.core import RegisterService
from ..config import secret_key, algorithm, expire_time
from doctor_repository.core import DoktorService
from admin_service.core import AdminService
from auth_service.core import AuthService
from token_manager import TokenManager

token_manager = TokenManager(secret=secret_key, algorithm=algorithm, expire_time=expire_time,
                             user_repository=user_repository)
auth_service = AuthService(token_cache=token_cache, user_repository=user_repository, token_manager=token_manager)
register_service = RegisterService(patient_repository=patient_repository, user_repository=user_repository,
                                   file_repository=file_repository)
doctor_service = DoktorService(patient_repository=patient_repository, user_repository=user_repository)
admin_service = AdminService(user_repository=user_repository)
