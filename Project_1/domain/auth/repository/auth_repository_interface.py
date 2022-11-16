from abc import ABC, abstractmethod
from domain.auth.entity.user import User


class AuthRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: User) -> None:
        pass

    @abstractmethod
    def authenticate(self, username: str) -> User:
        pass

    @abstractmethod
    def find(self, username: str) -> bool:
        pass
