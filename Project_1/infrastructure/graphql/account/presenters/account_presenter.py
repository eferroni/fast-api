from infrastructure.graphql.account.schemas.activate_account.activate_account_schema import ActivateAccountSchema
from infrastructure.graphql.account.schemas.deactivate_account.deactivate_account_schema import DeactivateAccountSchema
from infrastructure.graphql.account.schemas.delete_account.delete_account_schema import DeleteAccountSchema
from infrastructure.graphql.account.schemas.update_account.update_account_schema import UpdateAccountSchema
from infrastructure.graphql.account.schemas.update_password.update_password_schema import UpdatePasswordSchema
from usecase.account.update_account.update_account_dto import OutputUpdateAccountDto


class AccountPresenter:
    @staticmethod
    def update_account_to_graphql_schema(data: OutputUpdateAccountDto) -> UpdateAccountSchema:
        return UpdateAccountSchema(
            id=data.get('id'),
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            is_active=data.get('is_active'),
        )

    @staticmethod
    def update_password_to_graphql_schema(user_id: str, username: str) -> UpdatePasswordSchema:
        return UpdatePasswordSchema(
            id=user_id,
            username=username,
        )

    @staticmethod
    def activate_account_to_graphql_schema(user_id: str) -> ActivateAccountSchema:
        return ActivateAccountSchema(
            id=user_id,
            isActive=True
        )

    @staticmethod
    def deactivate_account_to_graphql_schema(user_id: str) -> DeactivateAccountSchema:
        return DeactivateAccountSchema(
            id=user_id,
            isActive=False
        )

    @staticmethod
    def delete_account_to_graphql_schema(user_id: str) -> DeleteAccountSchema:
        return DeleteAccountSchema(
            id=user_id,
        )
