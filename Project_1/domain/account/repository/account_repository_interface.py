from abc import ABC, abstractmethod
from domain.account.entity.user import User


class AccountRepositoryInterface(ABC):
    @abstractmethod
    def find(self, user_id: str) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user: User) -> None:
        pass
