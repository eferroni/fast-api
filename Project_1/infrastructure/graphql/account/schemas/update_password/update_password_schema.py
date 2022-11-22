import strawberry


@strawberry.type
class UpdatePasswordSchema:
    id: str
    username: str
