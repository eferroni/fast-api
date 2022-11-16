from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from usecase.account.update_account.update_account_dto import InputUpdateAccountDto, OutputUpdateAccountDto


class UpdateAccountUseCase:
    def __init__(self, repository: AccountRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputUpdateAccountDto) -> OutputUpdateAccountDto:
        user = self.repository.find(input_dto['id'])
        user.change_email(input_dto['email'])
        user.change_first_name(input_dto['first_name'])
        user.change_last_name(input_dto['last_name'])

        self.repository.update(user)
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_active": user.is_active
        }
