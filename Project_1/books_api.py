from fastapi import FastAPI
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

app = FastAPI()


# class DirectionName(str, Enum):
#     north = "North"
#     south = "South"
#     east = "East"
#     west = "West"


# @app.get("/")
# async def fetch_all_books(skip_book: Optional[str] = None):
#     if skip_book:
#         new_books = BOOKS.copy()
#         del new_books[skip_book]
#         return new_books
#     return BOOKS
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


# @app.get("/books/mybook")
# async def read_favorite_book():
#     return {"book_title": "My Favorite one"}

# @app.get("/book/")
# async def fetch_book_with_query_params(book_name: str):
#     return BOOKS[book_name]
#
#


@app.get("/book/")
async def find_all_books():
    book_repository = BookRepositoryDict()
    output_dto: OutputFindAllBookDto = FindAllBookUseCase(book_repository).execute()
    return output_dto


@app.get("/book/{book_id}")
async def find_book(book_id: str):
    input_dto: InputFindBookDto = {"id": book_id}
    book_repository = BookRepositoryDict()
    output_dto: OutputFindBookDto = FindBookUseCase(book_repository).execute(input_dto)
    return output_dto


@app.post("/book/")
async def create_book(book_title: str, book_author: str):
    input_dto: InputCreateBookDto = {"title": book_title, "author": book_author}
    book_repository = BookRepositoryDict()
    output_dto: OutputCreateBookDto = CreateBookUseCase(book_repository).execute(input_dto)
    return output_dto


@app.put("/book/{book_id}")
async def update_book(book_id: str, book_title: str, book_author: str):
    input_dto: InputUpdateBookDto = {"id": book_id, "title": book_title, "author": book_author}
    book_repository = BookRepositoryDict()
    output_dto: OutputUpdateBookDto = UpdateBookUseCase(book_repository).execute(input_dto)
    return output_dto


@app.delete("/book/{book_id}")
async def delete_book(book_id: str):
    input_dto: InputDeleteBookDto = {"id": book_id}
    book_repository = BookRepositoryDict()
    output_dto: OutputDeleteBookDto = DeleteBookUseCase(book_repository).execute(input_dto)
    return output_dto
