import strawberry
from typing import List, Optional
from infrastructure.book.repository.repository import book_repository
from usecase.book.create.create_book_dto import InputCreateBookDto, OutputCreateBookDto
from usecase.book.create.create_book_usecase import CreateBookUseCase
from usecase.book.find.find_book_dto import InputFindBookDto, OutputFindBookDto
from usecase.book.find.find_book_usecase import FindBookUseCase
from usecase.book.find_all.find_all_book_dto import OutputFindAllBookDto
from usecase.book.find_all.find_all_book_usecase import FindAllBookUseCase


@strawberry.type
class BookSchema:
    id: str
    title: str
    author: str


def find_book(book_id: str) -> BookSchema:
    input_dto: InputFindBookDto = {"id": book_id}
    output_dto: OutputFindBookDto = FindBookUseCase(book_repository).execute(input_dto)
    return BookSchema(
            id=output_dto.get('id'),
            title=output_dto.get('title'),
            author=output_dto.get('author'),
        )


def find_all_books(book_id: Optional[str] = None) -> List[BookSchema]:
    input_dto = {}
    if book_id is not None:
        input_dto['id'] = book_id
    use_case = FindAllBookUseCase(book_repository)
    output_dto: list[OutputFindAllBookDto] = use_case.execute(input_dto)
    return [
        BookSchema(
            id=book.get('id'),
            title=book.get('title'),
            author=book.get('author'),
        ) for book in output_dto
    ]


async def add_book(book):
    input_dto: InputCreateBookDto = {"title": book.title, "author": book.author}
    output_dto: OutputCreateBookDto = CreateBookUseCase(book_repository).execute(input_dto)
    return output_dto
