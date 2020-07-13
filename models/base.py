from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declared_attr, declarative_base

engine = create_engine("sqlite:///myapp.db")


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base, bind=engine)
