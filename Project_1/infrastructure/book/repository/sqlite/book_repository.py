from sqlalchemy.exc import IntegrityError

from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from domain.book.exceptions.book_exceptions import BookNotFound, BookIdAlreadyExist
from infrastructure.__shared__.repository.sqlite.database import SessionLocal
import infrastructure.book.repository.sqlite.book_model as models


class BookRepositorySqlite(BookRepositoryInterface):
    def __init__(self):
        self.session = SessionLocal()

    def close(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def find(self, book_id: str) -> Book:
        book_item = self.session.query(models.Books).filter(models.Books.id == book_id).first()
        if book_item is None:
            raise BookNotFound
        book = Book(book_item.id, book_item.title, book_item.author)
        return book

    def find_all(self, book_id: str = None) -> list[Book]:
        if book_id is None:
            books = self.session.query(models.Books).all()
        else:
            books = self.session.query(models.Books).filter(models.Books.id == book_id).all()
        book_list = list()
        for book_item in books:
            book = Book(book_item.id, book_item.title, book_item.author)
            book_list.append(book)
        return book_list

    def create(self, book: Book) -> None:
        try:
            book_model = models.Books()
            book_model.id = book.id
            book_model.title = book.title
            book_model.author = book.author

            self.session.add(book_model)
            self.commit()
        except IntegrityError:
            raise BookIdAlreadyExist

    def update(self, book: Book) -> None:
        self.session.query(models.Books).filter(models.Books.id == book.id).update(
            {
                "title": book.title,
                "author": book.author
            }
        )
        self.commit()

    def delete(self, book: Book) -> None:
        self.session.query(models.Books).filter(models.Books.id == book.id).delete()
        self.commit()
