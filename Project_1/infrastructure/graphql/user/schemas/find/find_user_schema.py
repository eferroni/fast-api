import strawberry


@strawberry.type
class FindUserSchema:
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
