from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from main2 import Base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    