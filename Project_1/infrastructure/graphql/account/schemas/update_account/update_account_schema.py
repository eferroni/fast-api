import strawberry


@strawberry.type
class UpdateAccountSchema:
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
