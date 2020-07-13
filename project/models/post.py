import datetime

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .user import User
from .base import Base


class Post(Base):
    __tablename__ = "posts"

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now())
    user = relationship(User, back_populates="posts")

    def __init__(self, text: str, user_id: int):
        self.user_id = user_id
        self.text = text

    def __repr__(self):
        return f"<Post #{self.id} user_id {self.user_id} created: {self.created_date} text: {self.text}>"
