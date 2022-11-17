from sqlalchemy import Column, String, Boolean, UniqueConstraint
from infrastructure.__shared__.repository.sqlite.database import Base, engine


class Users(Base):
    __tablename__ = "users"
    # __table_args__ = (UniqueConstraint('username', name='_username'),)

    id = Column(String, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

Base.metadata.create_all(engine)
