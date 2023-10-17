from fastapi import FastAPI, Depends,Query, HTTPException
from typing import Any
from model import employees,Month   #importing table models 


from sqlalchemy import Column,String,Integer,Boolean

from sqlalchemy.orm import Session,sessionmaker 
 # generates new session objects

from fastapi.responses import JSONResponse

from pydantic import BaseModel
from database import Base,engine,SessionLocal,get_db





app = FastAPI()




Base.metadata.create_all(bind=engine) 
#create_all method is then called with the
#  engine to create the necessary  table in the specified  database.

# base model
class employees(BaseModel):
    em_id: int
    em_name:str
    email:str

    class config:
        orm_mode=True
    
#CRUD OPERATIONS

@app.post("/employee",response_model=employees)
def create_employees(emp:employees,db:Session=Depends(get_db)): #sending data into  database schema
    data = employees(em_id=emp.em_id , 
                    em_name=emp.em_name ,
                    email = emp.email) 
     #send data as employee model table
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

# to get employee deatils
@app.get("/employees/{em_id}",response_model=list[employees]) # base model as response
def get_employees(em_id:int,db:Session=Depends(get_db)):
    if db is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return db.query(employees).all() # get all from em table

@app.put("/employee/{em_id}",response_model=employees)
def update_employees(em_id:int,emp:employees,db:Session=Depends(get_db)):
    try:
        data=db.query(employees).filter(employees.em_id ==em_id).first()
        # if given em_id and database em_id same then execute above

        #chageing values
        data.em_id = emp.em_id  # we store employee schema in emp
        data.em_name=emp.em_name
        data.email = emp.email

        db.add(data)
        db.commit()
        return data

    except:
        return HTTPException(status_code=404,details = "employee not found")



# delete employee
@app.delete("/employee/{em_id}",response_class=JSONResponse)
def delete_employee(em_id:int,db:Session=Depends(get_db)):
    try:
        data = db.query(employees).filter(employees.em_id == em_id).first()
        db.delete(data)
        return {f"employee of id {em_id} has been deleted":True}
    
    except:
        return HTTPException(status_code=404,details = "user not found")
    

'''
@app.put("employees/{em_id}")
def update_employee(em_id:int,emp:employees,db:Session=Depends(get_db)):
    new = db.query(employees).filter(employees.em_id == em_id).first()
    if new is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for var, value in vars(employees).items():
        setattr(new, var, value)
    db.commit()
    db.refresh(new)
    return new

@app.delete("employee/{em_id}")
def delete_employee(em_id:id,db:Session=Depends(get_db)):
    data = db.query(employees).filter(employees.em_id == em_id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for var, value in vars(employees).items():
        setattr(data, var, value)
    db.commit()
    db.refresh(data)
    return data
'''

     


