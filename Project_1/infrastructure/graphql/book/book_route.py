import strawberry
from typing import Optional
from infrastructure.book.repository.repository import book_repository
from infrastructure.graphql.book.presenters.book_presenter import BookPresenter
from infrastructure.graphql.book.schemas.create.create_book_schema import CreateBookSchema
from infrastructure.graphql.book.schemas.delete.delete_book_schema import DeleteBookSchema
from infrastructure.graphql.book.schemas.find_all.find_all_book_schema import FindAllBookSchema
from infrastructure.graphql.book.schemas.find.find_book_schema import FindBookSchema
from infrastructure.graphql.book.schemas.update.update_book_schema import UpdateBookSchema
from usecase.book.create.create_book_dto import InputCreateBookDto, OutputCreateBookDto
from usecase.book.create.create_book_usecase import CreateBookUseCase
from usecase.book.delete.delete_book_dto import InputDeleteBookDto, OutputDeleteBookDto
from usecase.book.delete.delete_book_usecase import DeleteBookUseCase
from usecase.book.find.find_book_dto import InputFindBookDto, OutputFindBookDto
from usecase.book.find.find_book_usecase import FindBookUseCase
from usecase.book.find_all.find_all_book_dto import OutputFindAllBookDto, InputFindAllBookDto
from usecase.book.find_all.find_all_book_usecase import FindAllBookUseCase
from usecase.book.update.update_book_dto import InputUpdateBookDto, OutputUpdateBookDto
from usecase.book.update.update_book_usecase import UpdateBookUseCase


def find_book(book_id: strawberry.ID) -> FindBookSchema:
    input_dto: InputFindBookDto = {"id": book_id}
    output_dto: OutputFindBookDto = FindBookUseCase(book_repository).execute(input_dto)
    return BookPresenter.find_book_to_graphql_schema(output_dto)


def find_all_books(title: Optional[str] = None,
                   author: Optional[str] = None,
                   size: int = 10,
                   page: int = 1,
                   order: str = 'title') -> FindAllBookSchema:
    input_dto: InputFindAllBookDto = {
        'title': title,
        'author': author,
        'page': page,
        'size': size,
        'order': order
    }
    use_case = FindAllBookUseCase(book_repository)
    output_dto: OutputFindAllBookDto = use_case.execute(input_dto)
    return BookPresenter.find_all_books_to_graphql_schema(output_dto)


async def create_book(title: str, author: str) -> CreateBookSchema:
    input_dto: InputCreateBookDto = {"title": title, "author": author}
    output_dto: OutputCreateBookDto = CreateBookUseCase(book_repository).execute(input_dto)
    return BookPresenter.add_book_to_graphql_schema(output_dto)


async def update_book(book_id: strawberry.ID, title: str, author: str) -> UpdateBookSchema:
    input_dto: InputUpdateBookDto = {"id": book_id, "title": title, "author": author}
    output_dto: OutputUpdateBookDto = UpdateBookUseCase(book_repository).execute(input_dto)
    return BookPresenter.update_book_to_graphql_schema(output_dto)


async def delete_book(book_id: strawberry.ID) -> DeleteBookSchema:
    input_dto: InputDeleteBookDto = {"id": book_id}
    output_dto: OutputDeleteBookDto = DeleteBookUseCase(book_repository).execute(input_dto)
    return BookPresenter.delete_book_to_graphql_schema(output_dto)
