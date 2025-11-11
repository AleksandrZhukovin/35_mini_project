from sqlalchemy import Column, Integer, String

from .db import Base


__all__ = ['Base', 'User']


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
