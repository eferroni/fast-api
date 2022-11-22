import strawberry


@strawberry.type
class UpdateBookSchema:
    id: str
    title: str
    author: str
