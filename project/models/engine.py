from sqlalchemy import create_engine

from config import DB_URL

#engine = create_engine("sqlite:///myapp.db")
engine = create_engine(DB_URL)
