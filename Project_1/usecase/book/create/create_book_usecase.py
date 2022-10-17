import uuid

from domain.book.entity.book import Book
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from usecase.book.create.create_book_dto import InputCreateBookDto, OutputCreateBookDto


class CreateBookUseCase:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputCreateBookDto) -> OutputCreateBookDto:
        book_id = str(uuid.uuid4())
        book = Book(book_id, input_dto['title'], input_dto['author'])
        self.repository.create(book)
        return {
            "id": book.id,
            "title": book.title,
            "author": book.author
        }
