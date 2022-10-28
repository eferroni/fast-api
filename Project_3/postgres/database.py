from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRESQL_PASSWORD = config('SQLITE3_PASSWORD')

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{POSTGRESQL_PASSWORD}@localhost/TodoApplicationDatabase"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
