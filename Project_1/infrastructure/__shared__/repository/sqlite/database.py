import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.environ.get("SQLITE_DB_URL")


engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": False},
    # echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
