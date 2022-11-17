import os
from dotenv import load_dotenv

from infrastructure.book.repository.mongo.book_repository import BookRepositoryMongo
from infrastructure.book.repository.dict.book_repository import BookRepositoryDict
from infrastructure.book.repository.sqlite.book_repository import BookRepositorySqlite
from infrastructure.book.repository.postgres.book_repository import BookRepositoryPostgres
from infrastructure.__shared__.constants import repository

load_dotenv()
REPOSITORY = os.environ.get("REPOSITORY")
if REPOSITORY == repository.SQLITE:
    book_repository = BookRepositorySqlite()
elif REPOSITORY == repository.POSTGRES:
    book_repository = BookRepositoryPostgres()
elif REPOSITORY == repository.MONGO:
    book_repository = BookRepositoryMongo()
elif REPOSITORY == repository.DICT:
    book_repository = BookRepositoryDict()
