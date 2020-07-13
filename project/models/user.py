import hashlib

from flask_login import UserMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base, UserMixin):
    __tablename__ = "users"

    username = Column(String(32), nullable=False, unique=True)
    _password = Column("password", String(200), nullable=False)
    posts = relationship("Post", back_populates="user")

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = self.hash_password(value)

    @classmethod
    def hash_password(cls, value: str) -> str:
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def __repr__(self):
        return f"<User #{self.id} Name: {self.username}>"
