from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from infrastructure.book.repository.dict.book_dictionary import BOOKS
from domain.book.exceptions.book_exceptions import BookNotFound, BookIdAlreadyExist


class BookRepositoryDict(BookRepositoryInterface):
    def find(self, book_id: str) -> Book:
        if book_id not in BOOKS:
            raise BookNotFound
        book_item = BOOKS[book_id]
        book = Book(book_id, book_item['title'], book_item['author'])
        return book

    def find_all(self, book_id: str = None) -> list[Book]:
        book_list = list()
        for book_item in BOOKS.keys():
            append = True
            if book_id is not None and book_item != book_id:
                append = False
            if append is True:
                book = Book(book_item, BOOKS[book_item]['title'], BOOKS[book_item]['author'])
                book_list.append(book)

        return book_list

    def create(self, book: Book) -> None:
        if book.id in BOOKS:
            raise BookIdAlreadyExist
        BOOKS[book.id] = {'title': book.title, 'author': book.author}

    def update(self, book: Book) -> None:
        BOOKS[book.id] = {'title': book.title, 'author': book.author}

    def delete(self, book: Book) -> None:
        del BOOKS[book.id]
