from sqlalchemy import Column, String
from infrastructure.book.repository.sqlite.database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True)
    title = Column(String)
    author = Column(String)

