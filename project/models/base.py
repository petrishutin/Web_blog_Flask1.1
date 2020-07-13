from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

from .engine import engine


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base, bind=engine)
