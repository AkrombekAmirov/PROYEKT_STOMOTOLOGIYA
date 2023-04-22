from jwt import encode, decode, exceptions
from user_repository import UserRepository
from datetime import datetime, timedelta
import datetime



class TokenExpired(Exception):
    pass


class TokenManager:
    def __init__(self, secret, algorithm, expire_time, user_repository: UserRepository):
        self.secret = secret
        self.algorithm = algorithm
        self.expire_time = expire_time
        self.user_repository = user_repository

    def encrypt(self, data: dict):
        to_encode = data.copy()
        to_encode.update({"exp": datetime.utcnow() + timedelta(days=1)})
        return encode(payload=to_encode, key=self.secret, algorithm=self.algorithm)

    def decrypt(self, token):
        return bool(self.user_repository.get_user(decode(token, self.secret, algorithms=[self.algorithm]).get("sub")))

    def get(self, token):
        return decode(token, self.secret, algorithms=[self.algorithm]).get("sub")

    def expire(self, token):
        try:
            decoded_token = decode(token, self.secret, algorithms=[self.algorithm])
            if datetime.utcnow() > datetime.fromtimestamp(decoded_token.get("exp")):
                raise TokenExpired("Token expired")
        except exceptions.DecodeError:
            return False
        except TokenExpired:
            return False
        return self.encrypt({"sub": decoded_token.get("sub")})
