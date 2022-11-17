import os
from dotenv import load_dotenv

from infrastructure.auth.repository.dict.auth_repository import AuthRepositoryDict
from infrastructure.auth.repository.mongo.auth_repository import AuthRepositoryMongo
from infrastructure.auth.repository.postgres.auth_repository import AuthRepositoryPostgres
from infrastructure.auth.repository.sqlite.auth_repository import AuthRepositorySqlite
from infrastructure.__shared__.constants import repository

load_dotenv()
REPOSITORY = os.environ.get("REPOSITORY")
if REPOSITORY == repository.SQLITE:
    auth_repository = AuthRepositorySqlite()
elif REPOSITORY == repository.POSTGRES:
    auth_repository = AuthRepositoryPostgres()
elif REPOSITORY == repository.MONGO:
    auth_repository = AuthRepositoryMongo()
elif REPOSITORY == repository.DICT:
    auth_repository = AuthRepositoryDict()
