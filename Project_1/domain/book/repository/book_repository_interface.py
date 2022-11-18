from abc import ABC, abstractmethod
from domain.book.entity.book import Book


class BookRepositoryInterface(ABC):
    @abstractmethod
    def count(self, book_title: str, book_author: str) -> int:
        pass

    @abstractmethod
    def find(self, book_id: str) -> Book:
        pass

    @abstractmethod
    def find_all(self, title: str, author: str, page: int, size: int, order: str) -> list[Book]:
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
