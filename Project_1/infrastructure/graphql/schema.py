import strawberry

from infrastructure.graphql.__shared__.authentication import (
    IsAuthenticatedActive, IsAuthenticatedSameUser
)
from infrastructure.graphql.account.account_route import (
    update_user_account, update_user_account_password,
    activate_user_account, deactivate_user_account, delete_user_account
)
from infrastructure.graphql.account.schemas.activate_account.activate_account_schema import ActivateAccountSchema
from infrastructure.graphql.account.schemas.deactivate_account.deactivate_account_schema import DeactivateAccountSchema
from infrastructure.graphql.account.schemas.delete_account.delete_account_schema import DeleteAccountSchema
from infrastructure.graphql.account.schemas.update_account.update_account_schema import UpdateAccountSchema
from infrastructure.graphql.account.schemas.update_password.update_password_schema import UpdatePasswordSchema
from infrastructure.graphql.auth.schemas.create.create_user_schema import CreateUserSchema
from infrastructure.graphql.auth.schemas.login.login_schema import LoginSchema
from infrastructure.graphql.book.book_route import (
    find_all_books, find_book, create_book, update_book, delete_book
)
from infrastructure.graphql.auth.auth_route import (
    create_user, login
)
from infrastructure.graphql.book.schemas.create.create_book_schema import CreateBookSchema
from infrastructure.graphql.book.schemas.delete.delete_book_schema import DeleteBookSchema
from infrastructure.graphql.book.schemas.find_all.find_all_book_schema import FindAllBookSchema
from infrastructure.graphql.book.schemas.find.find_book_schema import FindBookSchema
from infrastructure.graphql.book.schemas.update.update_book_schema import UpdateBookSchema
from infrastructure.graphql.user.schemas.find.find_user_schema import FindUserSchema
from infrastructure.graphql.user.schemas.find_all.find_all_user_schema import FindAllUserSchema
from infrastructure.graphql.user.user_route import find_user, find_all_users


@strawberry.type
class Query:
    book: FindBookSchema = strawberry.field(resolver=find_book, permission_classes=[IsAuthenticatedActive])
    books: FindAllBookSchema = strawberry.field(resolver=find_all_books, permission_classes=[IsAuthenticatedActive])

    login: LoginSchema = strawberry.field(resolver=login)

    user: FindUserSchema = strawberry.field(resolver=find_user, permission_classes=[IsAuthenticatedActive])
    users: FindAllUserSchema = strawberry.field(resolver=find_all_users, permission_classes=[IsAuthenticatedActive])


@strawberry.type
class Mutation:
    create_book: CreateBookSchema = strawberry.field(resolver=create_book, permission_classes=[IsAuthenticatedActive])
    update_book: UpdateBookSchema = strawberry.field(resolver=update_book, permission_classes=[IsAuthenticatedActive])
    delete_book: DeleteBookSchema = strawberry.field(resolver=delete_book, permission_classes=[IsAuthenticatedActive])

    create_user: CreateUserSchema = strawberry.field(resolver=create_user)

    update_account: UpdateAccountSchema = strawberry.field(
        resolver=update_user_account, permission_classes=[IsAuthenticatedSameUser]
    )
    update_password: UpdatePasswordSchema = strawberry.field(
        resolver=update_user_account_password, permission_classes=[IsAuthenticatedSameUser]
    )
    activate_account: ActivateAccountSchema = strawberry.field(
        resolver=activate_user_account, permission_classes=[IsAuthenticatedSameUser]
    )
    deactivate_account: DeactivateAccountSchema = strawberry.field(
        resolver=deactivate_user_account, permission_classes=[IsAuthenticatedSameUser]
    )
    delete_account: DeleteAccountSchema = strawberry.field(
        resolver=delete_user_account, permission_classes=[IsAuthenticatedSameUser]
    )


schema = strawberry.Schema(query=Query, mutation=Mutation)
