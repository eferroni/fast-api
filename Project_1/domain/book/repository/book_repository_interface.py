from abc import ABC, abstractmethod
from domain.book.entity.book import Book


class BookRepositoryInterface(ABC):
    @abstractmethod
    def find(self, book_id: str) -> Book:
        pass

    @abstractmethod
    def find_all(self, book_id: str = None) -> list[Book]:
        pass

    @abstractmethod
    def create(self, book: Book) -> None:
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        pass

    @abstractmethod
    def delete(self, book: Book) -> None:
        pass
