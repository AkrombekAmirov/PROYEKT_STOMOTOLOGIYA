from registration_repository.core import AuthorizedRegisterService
from doctor_repository.core import AuthorizedDoktorService
from admin_service.core import AuthorizedAdminService
from .all import (
    auth_service,
    admin_service,
    register_service,
    doctor_service
)

authorized_register_service = AuthorizedRegisterService(register_service=register_service, auth_service=auth_service)
authorized_doctor_service = AuthorizedDoktorService(doktor_service=doctor_service, auth_service=auth_service)
authorized_admin_service = AuthorizedAdminService(admin_service=admin_service, auth_service=auth_service)
