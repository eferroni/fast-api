from infrastructure.book.repository.dict.book_repository import BookRepositoryDict
from usecase.book.find.find_book_dto import InputFindBookDto, OutputFindBookDto
from usecase.book.find.find_book_usecase import FindBookUseCase
from fastapi import HTTPException


def test_find_book_usecase():
    input_dto: InputFindBookDto = {"id": "book_1"}
    book_repository = BookRepositoryDict()
    output_dto: OutputFindBookDto = FindBookUseCase(book_repository).execute(input_dto)
    assert output_dto == {
        "id": "book_1",
        "title": "Title 1",
        "author": "Author 1"
    }


def test_find_book_usecase_not_found():
    try:
        input_dto: InputFindBookDto = {"id": "invalid_id"}
        book_repository = BookRepositoryDict()
        FindBookUseCase(book_repository).execute(input_dto)
        assert False
    except HTTPException:
        assert True
