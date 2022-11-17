import os
from dotenv import load_dotenv

from infrastructure.user.repository.dict.user_repository import UserRepositoryDict
from infrastructure.user.repository.mongo.user_repository import UserRepositoryMongo
from infrastructure.user.repository.postgres.user_repository import UserRepositoryPostgres
from infrastructure.user.repository.sqlite.user_repository import UserRepositorySqlite
from infrastructure.__shared__.constants import repository

load_dotenv()
REPOSITORY = os.environ.get("REPOSITORY")
if REPOSITORY == repository.SQLITE:
    user_repository = UserRepositorySqlite()
elif REPOSITORY == repository.POSTGRES:
    user_repository = UserRepositoryPostgres()
elif REPOSITORY == repository.MONGO:
    user_repository = UserRepositoryMongo()
elif REPOSITORY == repository.DICT:
    user_repository = UserRepositoryDict()
