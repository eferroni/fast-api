import strawberry


@strawberry.type
class ActivateAccountSchema:
    id: str
    isActive: bool
