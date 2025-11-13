from pydantic import BaseModel

from sqlalchemy import Column, Integer, String, Text, ForeignKey

from passlib.context import CryptContext

from .db import Base


__all__ = ['Base', 'User']


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def hash_password(self):
        self.password = pwd_context.hash(self.password)


class UserSignUp(BaseModel):
    username: str
    password: str


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    image = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))  # foreign key
