from typing import Optional
from fastapi import FastAPI, status, HTTPException
from infrastructure.book.repository.dict.book_repository import BookRepositoryDict
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
from domain.book.validator.create_book_validator import CreateBookValidator
from domain.book.validator.update_book_validator import UpdateBookValidator

app = FastAPI()

# class DirectionName(str, Enum):
#     north = "North"
#     south = "South"
#     east = "East"
#     west = "West"
#
#
# @app.get("/directions/{direction_name}")
# async def get_direction(direction_name: DirectionName):
#     if direction_name == DirectionName.north:
#         return {"Direction": direction_name, "sub": "Up"}
#     if direction_name == DirectionName.south:
#         return {"Direction": direction_name, "sub": "Down"}
#     if direction_name == DirectionName.west:
#         return {"Direction": direction_name, "sub": "Left"}
#     return {"Direction": direction_name, "sub": "Right"}


@app.get("/books/")
async def find_all_books(book_id: Optional[str] = None):
    try:
        input_dto = {}
        if book_id:
            input_dto['id'] = book_id
        book_repository = BookRepositoryDict()
        use_case = FindAllBookUseCase(book_repository)
        output_dto: list[OutputFindAllBookDto] = use_case.execute(input_dto)
        return output_dto
    except Exception:
        raise HTTPException(status_code=500,
                            detail="Something went wrong :(")


@app.get("/books/{book_id}")
async def find_book(book_id: str):
    try:
        input_dto: InputFindBookDto = {"id": book_id}
        book_repository = BookRepositoryDict()
        output_dto: OutputFindBookDto = FindBookUseCase(book_repository).execute(input_dto)
        return output_dto

    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Something went wrong :(")


@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def create_book(book: CreateBookValidator):
    try:
        input_dto: InputCreateBookDto = {"title": book.title, "author": book.author}
        book_repository = BookRepositoryDict()
        output_dto: OutputCreateBookDto = CreateBookUseCase(book_repository).execute(input_dto)
        return output_dto
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=e)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Something went wrong :(")


@app.put("/books/{book_id}")
async def update_book(book_id: str, book: UpdateBookValidator):
    try:
        input_dto: InputUpdateBookDto = {"id": book_id, "title": book.title, "author": book.author}
        book_repository = BookRepositoryDict()
        output_dto: OutputUpdateBookDto = UpdateBookUseCase(book_repository).execute(input_dto)
        return output_dto
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Something went wrong :(")


@app.delete("/books/{book_id}")
async def delete_book(book_id: str):
    try:
        input_dto: InputDeleteBookDto = {"id": book_id}
        book_repository = BookRepositoryDict()
        output_dto: OutputDeleteBookDto = DeleteBookUseCase(book_repository).execute(input_dto)
        return output_dto
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Something went wrong :(")
