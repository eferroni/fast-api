from domain.account.repository.account_repository_interface import AccountRepositoryInterface
from usecase.account.activate.activate_account_dto import InputActivateAccountDto


class ActivateAccountUseCase:
    def __init__(self, repository: AccountRepositoryInterface):
        self.repository = repository

    def execute(self, input_dto: InputActivateAccountDto) -> None:
        user = self.repository.find(input_dto['id'])
        user.activate()

        self.repository.update(user)
        return
