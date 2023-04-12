from key_value_cache.domain import KeyValueCache
from user_repository import UserRepository
from string import ascii_uppercase, digits
from random import choices
from re import match


def password_policy(password):
    assert match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", password) is not None, "Password policy error"


class AuthService:
    def __init__(self,
                 token_cache: KeyValueCache,
                 user_repository: UserRepository):
        self.token_cache = token_cache
        self.user_repository = user_repository

    def generate_token(self) -> str:
        token = ''.join(choices(ascii_uppercase + digits, k=10))
        self.token_cache.set(token, None)
        return token

    def exists_token(self, token) -> bool:
        return self.token_cache.exists(token)

    def expire_token(self, token):
        if not self.exists_token(token): raise Exception("Token does not login")
        return self.token_cache.expire(token)

    def _login(self, token, credentials):
        user = self.user_repository.get_one_filtered(**credentials.dict())
        if not user: raise Exception("user not found")
        # if user.role != role: raise Exception(f"you are not {role}")
        self.token_cache.set(token, user.id)
        return user.dict()

    # def login_admin(self, token, credentials) -> bool:
    #     return self._login(token, credentials, "admin")
    #
    # def login_register(self, token, credentials) -> bool:
    #     return self._login(token, credentials, "register")
    #
    # def login_doctor(self, token, credentials):
    #     return self._login(token, credentials, "doctor")

    def logout(self, token):
        if not self.exists_token(token): raise Exception("Token does not exist")
        if self.token_cache.get(token) is None: raise Exception("no need")
        self.token_cache.set(token, None)
        return True

    def login_required(self, token):
        if not self.exists_token(token): raise Exception("Token does not")
        user_id = self.token_cache.get(token)
        if None == user_id: raise Exception("Not logged in")
        return user_id

    def retrieve_user(self, token):
        user = self.user_repository.get_user(self.login_required(token))
        if not user: raise Exception("user not found")
        return user
