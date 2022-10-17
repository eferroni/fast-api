from fastapi import HTTPException
from domain.book.repository.book_repository_interface import BookRepositoryInterface
from usecase.book.update.update_book_dto import InputUpdateBookDto, OutputUpdateBookDto


class UpdateBookUseCase:
    def __init__(self, repository: BookRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputUpdateBookDto) -> OutputUpdateBookDto:
        try:
            book = self.repository.find(input_dto['id'])
            book.title = input_dto['title']
            book.author = input_dto['author']

            self.repository.update(book)
            return {
                "id": book.id,
                "title": book.title,
                "author": book.author
            }
        except KeyError:
            raise HTTPException(status_code=404,
                                detail="Book not found")
