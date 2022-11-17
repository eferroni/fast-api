from passlib.context import CryptContext
from domain.password.exceptions.password_exceptions import PasswordPolicy


class Password:
    def __init__(self, hashed_password: str):
        self._hashed_password = hashed_password
        self.bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @property
    def hashed_password(self) -> str:
        return self._hashed_password

    def generate_hashed_password(self, plain_password: str) -> None:
        if 8 > len(plain_password) > 16:
            raise PasswordPolicy
        if not any(char.isdigit() for char in plain_password):
            raise PasswordPolicy
        if not any(char.islower() for char in plain_password):
            raise PasswordPolicy
        if not any(char.isupper() for char in plain_password):
            raise PasswordPolicy
        self._hashed_password = self.bcrypt_context.hash(plain_password)

    def verify_password(self, plain_password: str) -> bool:
        return self.bcrypt_context.verify(plain_password, self._hashed_password)

