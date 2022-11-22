import strawberry


@strawberry.type
class DeactivateAccountSchema:
    id: str
    isActive: bool
