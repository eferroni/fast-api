import strawberry


@strawberry.type
class CreateBookSchema:
    id: str
    title: str
    author: str
