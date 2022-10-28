from unittest import TestCase
from unittest.mock import patch
from fastapi import HTTPException

from infrastructure.book.repository.dict.book_repository import BookRepositoryDict
from usecase.book.create.create_book_usecase import CreateBookUseCase
from usecase.book.delete.delete_book_usecase import DeleteBookUseCase
from usecase.book.find.find_book_usecase import FindBookUseCase
from usecase.book.find_all.find_all_book_usecase import FindAllBookUseCase
from usecase.book.update.update_book_usecase import UpdateBookUseCase


class TestBookDictRepository(TestCase):
    def test_should_find_all_books(self):
        # noinspection PyTypeChecker
        input_dto = {}
        book_repository = BookRepositoryDict()
        # noinspection PyTypeChecker
        output_dto = FindAllBookUseCase(book_repository).execute(input_dto)
        self.assertGreater(len(output_dto), 1)
        assert output_dto[0] == {
            "id": "book_1",
            "title": "Title 1",
            "author": "Author 1"
        }

    def test_should_find_no_books(self):
        input_dto = {"id": "invalid_id"}
        book_repository = BookRepositoryDict()
        output_dto = FindAllBookUseCase(book_repository).execute(input_dto)
        self.assertEqual(0, len(output_dto))

    def test_should_find_a_book(self):
        input_dto = {"id": "book_1"}
        book_repository = BookRepositoryDict()
        output_dto = FindBookUseCase(book_repository).execute(input_dto)
        assert output_dto == {
            "id": "book_1",
            "title": "Title 1",
            "author": "Author 1"
        }

    def test_should_not_find_a_book(self):
        with self.assertRaises(KeyError):
            input_dto = {"id": "invalid_id"}
            book_repository = BookRepositoryDict()
            FindBookUseCase(book_repository).execute(input_dto)

    @patch('uuid.uuid4')
    def test_should_create_a_book(self, mock_uuid4):
        mock_uuid4.return_value = 'abcd1234'
        input_dto = {"title": "book_title", "author": "book_author"}
        book_repository = BookRepositoryDict()
        output_dto = CreateBookUseCase(book_repository).execute(input_dto)
        self.assertEqual(
            {"id": "abcd1234",
             "title": "book_title",
             "author": "book_author"},
            output_dto)

    def test_should_not_create_a_book_without_author(self):
        with self.assertRaises(KeyError):
            input_dto = {"title": "book_title"}
            book_repository = BookRepositoryDict()
            # noinspection PyTypeChecker
            CreateBookUseCase(book_repository).execute(input_dto)

    def test_should_not_create_a_book_without_title(self):
        with self.assertRaises(KeyError):
            input_dto = {"author": "book_author"}
            book_repository = BookRepositoryDict()
            # noinspection PyTypeChecker
            CreateBookUseCase(book_repository).execute(input_dto)

    def test_should_update_a_book(self):
        book_repository = BookRepositoryDict()

        update_input_dto = {"id": "book_3", "title": "book_title_updated", "author": "book_author_updated"}
        update_output_dto = UpdateBookUseCase(book_repository).execute(update_input_dto)
        self.assertEqual(
            {"id": "book_3",
             "title": "book_title_updated",
             "author": "book_author_updated"},
            update_output_dto)

    def test_should_not_update_a_book_with_wrong_id(self):
        with self.assertRaises(KeyError):
            input_dto = {"id": "wrong_id", "title": "book_title_updated", "author": "book_author_updated"}
            book_repository = BookRepositoryDict()
            # noinspection PyTypeChecker
            UpdateBookUseCase(book_repository).execute(input_dto)

    def test_should_not_update_a_book_without_author(self):
        with self.assertRaises(KeyError):
            input_dto = {"id": "book_1", "title": "book_title_updated"}
            book_repository = BookRepositoryDict()
            # noinspection PyTypeChecker
            UpdateBookUseCase(book_repository).execute(input_dto)

    def test_should_not_update_a_book_without_title(self):
        with self.assertRaises(KeyError):
            input_dto = {"id": "book_1", "author": "book_author_updated"}
            book_repository = BookRepositoryDict()
            # noinspection PyTypeChecker
            UpdateBookUseCase(book_repository).execute(input_dto)

    def test_should_delete_a_book(self):
        book_repository = BookRepositoryDict()

        delete_input_dto = {"id": "book_2"}
        delete_output_dto = DeleteBookUseCase(book_repository).execute(delete_input_dto)
        self.assertEqual({"message": "Book book_2 successfully deleted"}, delete_output_dto)
        with self.assertRaises(KeyError):
            input_dto = {"id": "book_2"}
            book_repository = BookRepositoryDict()
            FindBookUseCase(book_repository).execute(input_dto)

    def test_should_not_delete_a_book_with_wrong_id(self):
        with self.assertRaises(KeyError):
            delete_input_dto = {"id": "wrong_id"}
            book_repository = BookRepositoryDict()
            DeleteBookUseCase(book_repository).execute(delete_input_dto)
