from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from usecase.account.deactivate.deactivate_account_dto import InputDeactivateAccountDto


class DeactivateAccountUseCase:
    def __init__(self, repository: AccountRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputDeactivateAccountDto) -> None:
        user = self.repository.find(input_dto['id'])
        user.deactivate()

        self.repository.update(user)
        return
