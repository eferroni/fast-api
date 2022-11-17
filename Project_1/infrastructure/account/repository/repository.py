import os
from dotenv import load_dotenv

from infrastructure.account.repository.dict.account_repository import AccountRepositoryDict
from infrastructure.account.repository.mongo.account_repository import AccountRepositoryMongo
from infrastructure.account.repository.postgres.account_repository import AccountRepositoryPostgres
from infrastructure.account.repository.sqlite.account_repository import AccountRepositorySqlite
from infrastructure.__shared__.constants import repository

load_dotenv()
REPOSITORY = os.environ.get("REPOSITORY")
if REPOSITORY == repository.SQLITE:
    account_repository = AccountRepositorySqlite()
elif REPOSITORY == repository.POSTGRES:
    account_repository = AccountRepositoryPostgres()
elif REPOSITORY == repository.MONGO:
    account_repository = AccountRepositoryMongo()
elif REPOSITORY == repository.DICT:
    account_repository = AccountRepositoryDict()
