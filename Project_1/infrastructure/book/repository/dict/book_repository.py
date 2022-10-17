from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from infrastructure.book.repository.dict.book_dictionary import BOOKS


class BookRepositoryDict(BookRepositoryInterface):
    def find(self, id: str) -> Book:
        book_item = BOOKS[id]
        book = Book(id, book_item['title'], book_item['author'])
        return book

    def find_all(self) -> list[Book]:
        book_list = list()
        for book_item in BOOKS.keys():
            book = Book(book_item, BOOKS[book_item]['title'], BOOKS[book_item]['author'])
            book_list.append(book)
        return book_list

    def create(self, book: Book) -> None:
        BOOKS[book.id] = {'title': book.title, 'author': book.author}

    def update(self, book: Book) -> None:
        BOOKS[book.id] = {'title': book.title, 'author': book.author}

    def delete(self, book: Book) -> None:
        del BOOKS[book.id]