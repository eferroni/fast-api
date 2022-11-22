import strawberry


@strawberry.type
class FindBookSchema:
    id: str
    title: str
    author: str
