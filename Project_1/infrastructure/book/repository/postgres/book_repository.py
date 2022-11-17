from sqlalchemy import update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from domain.book.exceptions.book_exceptions import BookNotFound, BookIdAlreadyExist
from infrastructure.__shared__.repository.postgres.database import SessionLocal
import infrastructure.book.repository.postgres.book_model as models


class BookRepositoryPostgres(BookRepositoryInterface):
    def find(self, book_id: str) -> Book:
        with SessionLocal() as s:
            query = s.execute(
                select(models.Books).where(models.Books.id == book_id)
            )
            book_item = query.scalar()
        if book_item is None:
            raise BookNotFound
        book = Book(book_item.id, book_item.title, book_item.author)
        return book

    def find_all(self, book_id: str = None) -> list[Book]:
        with SessionLocal() as s:
            if book_id is None:
                query = s.execute(
                    select(models.Books)
                )
            else:
                query = s.execute(
                    select(models.Books).where(models.Books.id == book_id)
                )
            books = query.scalars().all()
        book_list = list()
        for book_item in books:
            book = Book(book_item.id, book_item.title, book_item.author)
            book_list.append(book)
        return book_list

    def create(self, book: Book) -> None:
        try:
            with SessionLocal() as s:
                book_model = models.Books()
                book_model.id = book.id
                book_model.title = book.title
                book_model.author = book.author

                s.add(book_model)
                s.commit()
        except IntegrityError:
            raise BookIdAlreadyExist

    def update(self, book: Book) -> None:
        with SessionLocal() as s:
            s.execute(
                update(models.Books).where(
                    models.Books.id == book.id
                ).values(title=book.title, author=book.author)
            )
            s.commit()

    def delete(self, book: Book) -> None:
        with SessionLocal() as s:
            s.execute(
                delete(models.Books).where(models.Books.id == book.id)
            )
            s.commit()
