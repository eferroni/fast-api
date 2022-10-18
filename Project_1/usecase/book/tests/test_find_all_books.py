from infrastructure.book.repository.dict.book_repository import BookRepositoryDict

from usecase.book.find_all.find_all_book_dto import InputFindAllBookDto, OutputFindAllBookDto
from usecase.book.find_all.find_all_book_usecase import FindAllBookUseCase


def test_should_find_all_books():
    input_dto: InputFindAllBookDto = {}
    book_repository = BookRepositoryDict()
    output_dto: list[OutputFindAllBookDto] = FindAllBookUseCase(book_repository).execute(input_dto)
    assert len(output_dto) == 5
    assert output_dto[-1] == {
        "id": "book_5",
        "title": "Title 5",
        "author": "Author 5"
    }


def test_should_not_find_all_books():
    input_dto: InputFindAllBookDto = {"id": "invalid_id"}
    book_repository = BookRepositoryDict()
    output_dto: list[OutputFindAllBookDto] = FindAllBookUseCase(book_repository).execute(input_dto)
    assert len(output_dto) == 0
