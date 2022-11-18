from abc import ABC, abstractmethod
from domain.user.entity.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def count(self, username: str, email: str, first_name: str, last_name: str) -> int:
        pass

    @abstractmethod
    def find(self, user_id: str) -> User:
        pass

    @abstractmethod
    def find_all(self, username: str, email: str, first_name: str,
                 last_name: str, page: int, size: int, order: str) -> list[User]:
        pass


