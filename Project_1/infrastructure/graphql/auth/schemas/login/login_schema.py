import strawberry


@strawberry.type
class LoginSchema:
    access_token: str
    token_type: str
