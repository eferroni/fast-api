import sqlite3
from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from domain.book.exceptions.book_exceptions import BookNotFound, BookIdAlreadyExist


class BookRepositorySqlite(BookRepositoryInterface):
    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()
        self._create_books_table()

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def _create_books_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL
        );""")

    def find(self, book_id: str) -> Book:
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book_item = self.cursor.fetchone()
        if book_item is None:
            raise BookNotFound
        book = Book(book_item[0], book_item[1], book_item[2])
        return book

    def find_all(self, book_id: str = None) -> list[Book]:
        if book_id is None:
            self.cursor.execute("SELECT * FROM books")
        else:
            self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        books = self.cursor.fetchall()
        book_list = list()
        for book_item in books:
            book = Book(book_item[0], book_item[1], book_item[2])
            book_list.append(book)
        return book_list

    def create(self, book: Book) -> None:
        try:
            self.cursor.execute("INSERT INTO books (id, title, author) VALUES (?, ?, ?)",
                                (book.id, book.title, book.author))
            self.commit()
        except sqlite3.IntegrityError:
            raise BookIdAlreadyExist

    def update(self, book: Book) -> None:
        self.cursor.execute("UPDATE books set title = ?, author = ? WHERE id = ?",
                            (book.title, book.author, book.id))
        self.commit()

    def delete(self, book: Book) -> None:
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book.id,))
        self.commit()
