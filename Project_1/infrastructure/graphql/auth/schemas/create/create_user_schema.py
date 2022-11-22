import strawberry


@strawberry.type
class CreateUserSchema:
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
