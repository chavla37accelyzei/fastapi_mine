from sqlalchemy import Column,String,Integer,Boolean

from sqlalchemy.orm import Session,sessionmaker 
 # generates new session objects

from database import Base,engine,SessionLocal,get_db



# model creation
class Month(Base):
    __tablename__ = "Month"
    month_id =  Column(Integer,primary_key=True,index=True)
    name = Column(String(length=50))
    no_of_holidays = Column(Integer)

class employees(Base):
    __tablename__ = "employees"
    em_id =  Column(Integer,primary_key=True,index=True)
    em_name =  Column(String(length=50))
    email = Column(String(length=50))