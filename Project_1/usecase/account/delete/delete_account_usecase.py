from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from usecase.account.delete.delete_account_dto import InputDeleteAccountDto


class DeleteAccountUseCase:
    def __init__(self, repository: AccountRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputDeleteAccountDto) -> None:
        user = self.repository.find(input_dto['id'])
        self.repository.delete(user)
        return
