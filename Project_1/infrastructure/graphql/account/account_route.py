from infrastructure.graphql.account.presenters.account_presenter import AccountPresenter
from infrastructure.graphql.account.schemas.activate_account.activate_account_schema import ActivateAccountSchema
from infrastructure.graphql.account.schemas.deactivate_account.deactivate_account_schema import DeactivateAccountSchema
from infrastructure.graphql.account.schemas.delete_account.delete_account_schema import DeleteAccountSchema
from infrastructure.graphql.account.schemas.update_account.update_account_schema import UpdateAccountSchema
from infrastructure.graphql.account.schemas.update_password.update_password_schema import UpdatePasswordSchema
from usecase.account.activate.activate_account_dto import InputActivateAccountDto
from usecase.account.activate.activate_account_usecase import ActivateAccountUseCase
from usecase.account.deactivate.deactivate_account_dto import InputDeactivateAccountDto
from usecase.account.deactivate.deactivate_account_usecase import DeactivateAccountUseCase
from usecase.account.delete.delete_account_dto import InputDeleteAccountDto
from usecase.account.delete.delete_account_usecase import DeleteAccountUseCase
from usecase.account.update_account.update_account_dto import InputUpdateAccountDto, OutputUpdateAccountDto
from usecase.account.update_account.update_account_usecase import UpdateAccountUseCase
from usecase.account.update_password.update_account_password_dto import InputUpdateAccountPasswordDto
from usecase.account.update_password.update_account_password_usecase import UpdateAccountPasswordUseCase
from infrastructure.account.repository.repository import account_repository


async def update_user_account(user_id: str,
                              email: str,
                              first_name: str,
                              last_name: str) -> UpdateAccountSchema:
    input_dto: InputUpdateAccountDto = {"id": user_id,
                                        "email": email,
                                        "first_name": first_name,
                                        "last_name": last_name}
    output_dto: OutputUpdateAccountDto = UpdateAccountUseCase(account_repository).execute(input_dto)
    return AccountPresenter.update_account_to_graphql_schema(output_dto)


async def update_user_account_password(user_id: str,
                                       username: str,
                                       password: str,
                                       new_password: str) -> UpdatePasswordSchema:
    input_dto: InputUpdateAccountPasswordDto = {
        "id": user_id,
        "username": username,
        "password": password,
        "new_password": new_password
    }
    UpdateAccountPasswordUseCase(account_repository).execute(input_dto)
    return AccountPresenter.update_password_to_graphql_schema(user_id, username)


async def activate_user_account(user_id: str) -> ActivateAccountSchema:
    input_dto: InputActivateAccountDto = {"id": user_id}
    ActivateAccountUseCase(account_repository).execute(input_dto)
    return AccountPresenter.activate_account_to_graphql_schema(user_id)


async def deactivate_user_account(user_id: str) -> DeactivateAccountSchema:
    input_dto: InputDeactivateAccountDto = {"id": user_id}
    DeactivateAccountUseCase(account_repository).execute(input_dto)
    return AccountPresenter.deactivate_account_to_graphql_schema(user_id)


async def delete_user_account(user_id: str) -> DeleteAccountSchema:
    input_dto: InputDeleteAccountDto = {"id": user_id}
    DeleteAccountUseCase(account_repository).execute(input_dto)
    return AccountPresenter.delete_account_to_graphql_schema(user_id)
