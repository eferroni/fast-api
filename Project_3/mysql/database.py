from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

MYSQL_PASSWORD = config('MYSQL_PASSWORD')

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost:3306/todoapp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
