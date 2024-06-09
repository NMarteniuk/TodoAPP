from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String,nullable=False)

    items = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True, index=True, nullable=False)
    text = Column(String, index=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="items")