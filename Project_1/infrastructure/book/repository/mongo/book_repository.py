from pymongo.errors import DuplicateKeyError

from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from domain.book.exceptions.book_exceptions import BookNotFound, BookIdAlreadyExist
from infrastructure.__shared__.repository.mongo.database import get_database


class BookRepositoryMongo(BookRepositoryInterface):
    def __init__(self):
        self.db_name = get_database()
        self.collection = self.db_name['books']

    def find(self, book_id: str) -> Book:
        book_item = self.collection.find_one({'_id': book_id})
        if book_item is None:
            raise BookNotFound
        book = Book(book_item.get('_id'), book_item.get('title'), book_item.get('author'))
        return book

    def find_all(self, book_id: str = None) -> list[Book]:
        if book_id is None:
            books = self.collection.find()
        else:
            books = self.collection.find({'_id': book_id})
        book_list = list()
        for book_item in books:
            book = Book(book_item.get('_id'), book_item.get('title'), book_item.get('author'))
            book_list.append(book)
        return book_list

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
