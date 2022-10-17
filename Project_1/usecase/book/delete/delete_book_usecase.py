from domain.book.repository.book_repository_interface import BookRepositoryInterface
from usecase.book.delete.delete_book_dto import InputDeleteBookDto, OutputDeleteBookDto


class DeleteBookUseCase:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputDeleteBookDto) -> OutputDeleteBookDto:
        book = self.repository.find(input_dto['id'])
        self.repository.delete(book)
        return {
            "message": f"Book {book.id} successfully deleted"
        }
