import jwt


class TokenManager:
    def __init__(self, secret):
        self.secret = secret

    def encrypt(self, data):
        return jwt.encode(data, self.secret, algorithm="HS256")

    def decrypt(self, token):
        return jwt.decode(token, self.secret, algorithms=["HS256"])
