import collections
from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from infrastructure.book.repository.dict.book_dictionary import BOOKS
from domain.book.exceptions.book_exceptions import BookNotFound, BookIdAlreadyExist


class BookRepositoryDict(BookRepositoryInterface):
    def count(self, book_title: str, book_author: str) -> int:
        counter = 0
        for book_item in BOOKS.keys():
            append = True
            if book_title is not None and book_title.lower() not in BOOKS[book_item]['title'].lower():
                append = False
            if book_author is not None and book_author.lower() not in BOOKS[book_item]['author'].lower():
                append = False
            if append is True:
                counter += 1
        return counter

    def find(self, book_id: str) -> Book:
        if book_id not in BOOKS:
            raise BookNotFound
        book_item = BOOKS[book_id]
        book = Book(book_id, book_item['title'], book_item['author'])
        return book

    def find_all(self, title: str, author: str, page: int, size: int, order: str) -> list[Book]:
        result = collections.OrderedDict(sorted(BOOKS.items(), key=lambda t: t[1][order]))

        book_list = list()
        for book_item in result.keys():
            append = True
            if title is not None and title.lower() not in result[book_item]['title'].lower():
                append = False
            if author is not None and author.lower() not in result[book_item]['author'].lower():
                append = False
            if append is True:
                book = Book(book_item, result[book_item]['title'], result[book_item]['author'])
                book_list.append(book)
        return book_list[((page-1)*size):(page * size)]

    def create(self, book: Book) -> None:
        if book.id in BOOKS:
            raise BookIdAlreadyExist
        BOOKS[book.id] = {'title': book.title, 'author': book.author}

    def update(self, book: Book) -> None:
        BOOKS[book.id] = {'title': book.title, 'author': book.author}

    def delete(self, book: Book) -> None:
        del BOOKS[book.id]
