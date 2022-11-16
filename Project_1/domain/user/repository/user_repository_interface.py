from abc import ABC, abstractmethod
from domain.user.entity.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def find(self, user_id: str) -> User:
        pass

    @abstractmethod
    def find_all(self, user_id: str = None) -> list[User]:
        pass


