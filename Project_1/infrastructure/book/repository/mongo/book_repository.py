import re

from pymongo.errors import DuplicateKeyError

from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from domain.book.exceptions.book_exceptions import BookNotFound, BookIdAlreadyExist
from infrastructure.__shared__.repository.mongo.database import get_database


class BookRepositoryMongo(BookRepositoryInterface):
    def __init__(self):
        self.db_name = get_database()
        self.collection = self.db_name['books']

    def count(self, book_title: str, book_author: str) -> int:
        query_filter = {}
        if book_title is not None:
            query_filter['title'] = re.compile(book_title, re.IGNORECASE)
        if book_author is not None:
            query_filter['author'] = re.compile(book_author, re.IGNORECASE)

        count = self.collection.count_documents(query_filter)
        return count

    def find(self, book_id: str) -> Book:
        book_item = self.collection.find_one({'_id': book_id})
        if book_item is None:
            raise BookNotFound
        book = Book(book_item.get('_id'), book_item.get('title'), book_item.get('author'))
        return book

    def find_all(self, title: str, author: str, page: int, size: int, order: str) -> list[Book]:
        query_filter = {}
        if title is not None:
            query_filter['title'] = re.compile(title, re.IGNORECASE)
        if author is not None:
            query_filter['author'] = re.compile(author, re.IGNORECASE)

        books = self.collection.find(query_filter).skip(((page-1)*size)).limit(size).sort(order)
        return [
            Book(book_item.get('_id'), book_item.get('title'),
                 book_item.get('author')) for book_item in books
        ]

    def create(self, book: Book) -> None:
        try:
            book_item = {
                "_id": book.id,
                "title": book.title,
                "author": book.author
            }

            self.collection.insert_one(book_item)
        except DuplicateKeyError:
            raise BookIdAlreadyExist

    def update(self, book: Book) -> None:
        self.collection.update_one({'_id': book.id}, {'$set': {
            "title": book.title,
            "author": book.author
        }})

    def delete(self, book: Book) -> None:
        self.collection.delete_one({'_id': book.id})
