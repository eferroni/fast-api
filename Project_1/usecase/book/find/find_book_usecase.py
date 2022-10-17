from domain.book.repository.book_repository_interface import BookRepositoryInterface
from usecase.book.find.find_book_dto import InputFindBookDto, OutputFindBookDto


class FindBookUseCase:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputFindBookDto) -> OutputFindBookDto:
        book = self.repository.find(input['id'])
        return {
            "id": book.id,
            "title": book.title,
            "author": book.author
        }
