
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from fastapi import FastAPI

Base = declarative_base()


    

class Item(Base):
    __tablename__ = "item"  # items as table

    id = Column(Integer, primary_key=True,index=True) #colums
    name = Column(String, index = True)
    description = Column(String)

class employee(Base):
    __tablename__ = "employee"

    em_id = Column(Integer,primary_key=True,index = True)
    name = Column(String,index = True)
    description = Column(String)

#define user class=table


class user(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True, index=True)
    email = Column(String,unique=True, index=True)
    hashed_password = Column(String)

    #add relation ship
   # items = relationship("user",back_populates="Item")


