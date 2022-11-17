from typing import Optional
from fastapi import status, HTTPException, APIRouter
from usecase.book.create.create_book_dto import InputCreateBookDto, OutputCreateBookDto
from usecase.book.create.create_book_usecase import CreateBookUseCase
from usecase.book.delete.delete_book_dto import InputDeleteBookDto, OutputDeleteBookDto
from usecase.book.delete.delete_book_usecase import DeleteBookUseCase
from usecase.book.find.find_book_dto import InputFindBookDto, OutputFindBookDto
from usecase.book.find.find_book_usecase import FindBookUseCase
from usecase.book.find_all.find_all_book_dto import OutputFindAllBookDto
from usecase.book.find_all.find_all_book_usecase import FindAllBookUseCase
from usecase.book.update.update_book_dto import InputUpdateBookDto, OutputUpdateBookDto
from usecase.book.update.update_book_usecase import UpdateBookUseCase
from infrastructure.api.v1.validator.book.create_book_validator import CreateBookValidator
from infrastructure.api.v1.validator.book.update_book_validator import UpdateBookValidator
from infrastructure.book.repository.repository import book_repository


router = APIRouter(prefix="/books", tags=["books"])


@router.get("/")
async def find_all_books(book_id: Optional[str] = None):
    try:
        input_dto = {}
        if book_id is not None:
            input_dto['id'] = book_id
        use_case = FindAllBookUseCase(book_repository)
        output_dto: list[OutputFindAllBookDto] = use_case.execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.get("/{book_id}")
async def find_book(book_id: str):
    try:
        input_dto: InputFindBookDto = {"id": book_id}
        output_dto: OutputFindBookDto = FindBookUseCase(book_repository).execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: CreateBookValidator):
    try:
        input_dto: InputCreateBookDto = {"title": book.title, "author": book.author}
        output_dto: OutputCreateBookDto = CreateBookUseCase(book_repository).execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.put("/{book_id}")
async def update_book(book_id: str, book: UpdateBookValidator):
    try:
        input_dto: InputUpdateBookDto = {"id": book_id, "title": book.title, "author": book.author}
        output_dto: OutputUpdateBookDto = UpdateBookUseCase(book_repository).execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")


@router.delete("/{book_id}")
async def delete_book(book_id: str):
    try:
        input_dto: InputDeleteBookDto = {"id": book_id}
        output_dto: OutputDeleteBookDto = DeleteBookUseCase(book_repository).execute(input_dto)
        return output_dto
    except Exception as e:
        raise HTTPException(
            status_code=e.status if hasattr(e, 'status') else status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message if hasattr(e, 'message') else "Something went wrong :(")
