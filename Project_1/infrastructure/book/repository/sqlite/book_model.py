from sqlalchemy import Column, String
from infrastructure.__shared__.repository.sqlite.database import Base, engine


class Books(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True)
    title = Column(String)
    author = Column(String)


Base.metadata.create_all(engine)
