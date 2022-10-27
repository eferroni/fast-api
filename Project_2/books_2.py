from fastapi import FastAPI, HTTPException, Request, status, Form, Header
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from starlette.responses import JSONResponse


class NegativeNumberException(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return


app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                       min_length=1,
                                       max_length=100)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "14689a67-77d5-475e-802c-2471237d87ea",
                "title": "Computer Science Pro",
                "author": "Coding with Edu",
                "description": "A very nice description of a book",
                "rating": 70
            }
        }


class BookNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                       min_length=1,
                                       max_length=100)


BOOKS = []


@app.exception_handler(NegativeNumberException)
def negative_number_exception_handler(request: Request, exception: NegativeNumberException):
    return JSONResponse(
        status_code=418,
        content={"message": f"negative number"}
    )


@app.post("/books/login")
def book_login(username: str = Form(), password: str = Form()):
    return {
        "username": username,
        "password": password
    }


@app.post("/books/login_header/")
def book_login_header(book_id: UUID, username: str = Header(), password: str = Header()):
    if username == 'FastAPIUser' and password == 'test1234!':
        for book in BOOKS:
            if book.id == book_id:
                return book
        raise raise_item_cannot_be_found_exception()
    raise HTTPException(status_code=403,
                        detail="User not found")


@app.get("/header")
def read_header(random_header: Optional[str] = Header(None)):
    return {"random-header": random_header}


@app.get("/")
def read_all_books(books_to_return: Optional[int] = None):
    if books_to_return and books_to_return < 0:
        raise NegativeNumberException(books_to_return=books_to_return)

    if len(BOOKS) < 1:
        create_books_no_api()

    if books_to_return is not None and len(BOOKS) >= books_to_return > 0:
        return BOOKS[0:books_to_return]
    return BOOKS


@app.get("/book/{book_id}")
def read_book(book_id: UUID):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise raise_item_cannot_be_found_exception()


@app.get("/book/rating/{book_id}", response_model=BookNoRating)
def read_book_no_rating(book_id: UUID):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise raise_item_cannot_be_found_exception()


@app.put("/book/{book_id}")
def update_book(book_id: UUID, book: Book):
    for index, item in enumerate(BOOKS):
        if item.id == book_id:
            BOOKS[index] = book
            return book
    raise raise_item_cannot_be_found_exception()


@app.delete("/book/{book_id}")
def delete_book(book_id: UUID):
    for index, item in enumerate(BOOKS):
        if item.id == book_id:
            del BOOKS[index]
            return f"Id {book_id} deleted"
    raise raise_item_cannot_be_found_exception()


@app.post("/", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_books_no_api():
    book_1 = Book(id="24689a67-77d5-475e-802c-2471237d87ea", title="Title 1", author="Author 1", description="Description 1", rating=10)
    book_2 = Book(id="f5da4585-54bf-47b8-86e4-917b3e8672a8", title="Title 2", author="Author 2", description="Description 2", rating=20)
    book_3 = Book(id="3c41abf0-6e5a-4ddf-a0ee-320cb9eeafb7", title="Title 3", author="Author 3", description="Description 3", rating=30)
    book_4 = Book(id="b468303b-005c-453e-9737-1735eb4f4dcc", title="Title 4", author="Author 4", description="Description 4", rating=40)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)


def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404,
                         detail="Book not found",
                         headers={"X-Header-Error": "Nothing to be seen at the uuid function"})


