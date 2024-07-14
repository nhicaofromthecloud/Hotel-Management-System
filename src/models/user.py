# src/models/user.py
from sqlalchemy import Column, Integer, String
from src.utils.db import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.full_name}>'
