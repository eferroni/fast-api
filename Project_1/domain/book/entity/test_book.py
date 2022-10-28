from unittest import TestCase
from book import Book


class TestBookEntity(TestCase):
    def test_should_raise_error_for_empty_id(self):
        with self.assertRaises(ValueError):
            book = Book("", "book_title", "book_author")

    def test_should_raise_error_for_empty_title(self):
        with self.assertRaises(ValueError):
            book = Book("1234", "", "book_author")

    def test_should_raise_error_for_empty_author(self):
        with self.assertRaises(ValueError):
            book = Book("1234", "book_title", "")

    def test_should_change_title(self):
        book = Book("1234", "book_title", "book_author")
        book.change_title("book_title_updated")
        self.assertEqual("book_title_updated", book.title)

    def test_should_change_author(self):
        book = Book("1234", "book_title", "book_author")
        book.change_author("book_author_updated")
        self.assertEqual("book_author_updated", book.author)
