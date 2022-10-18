from fastapi import HTTPException
from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from infrastructure.book.repository.dict.book_dictionary import BOOKS


class BookRepositoryDict(BookRepositoryInterface):
    def find(self, book_id: str) -> Book:
        try:
            book_item = BOOKS[book_id]
            book = Book(book_id, book_item['title'], book_item['author'])
            return book
        except KeyError:
            raise HTTPException(status_code=404, detail="Book not found")

    def find_all(self) -> list[Book]:
        book_list = list()
        for book_item in BOOKS.keys():
            book = Book(book_item, BOOKS[book_item]['title'], BOOKS[book_item]['author'])
            book_list.append(book)
        return book_list

    def create(self, book: Book) -> None:
        BOOKS[book.id] = {'title': book.title, 'author': book.author}

    def update(self, book: Book) -> None:
        try:
            BOOKS[book.id] = {'title': book.title, 'author': book.author}
        except KeyError:
            raise HTTPException(status_code=404, detail="Book not found")

    def delete(self, book: Book) -> None:
        try:
            del BOOKS[book.id]
        except KeyError:
            raise HTTPException(status_code=404, detail="Book not found")
