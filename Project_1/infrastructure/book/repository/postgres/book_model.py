from sqlalchemy import Column, String
from infrastructure.__shared__.repository.postgres.database import Base, engine


class Books(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True)
    title = Column(String)
    author = Column(String)

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title})"


Base.metadata.create_all(engine)
