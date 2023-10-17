from fastapi import FastAPI ,Request
from pydantic import BaseModel
app=FastAPI()

#using pydantic
class New_Employee(BaseModel):
    emp_id:int
    name:str
    age:int
    teams:list

@app.post("/add_employee")
def add_employee(employee:New_Employee) :  #sending base class
    new_em = employee(emp_id = employee.emp_id,name=employee.name,age=employee.age)
    #new_em is an instance of employee

    New_Employee.save()
    return {'message':'employee is successfully added'}

#OR using request
@app.post("/items/")
async def create_item(request:Request): #sending request
    #access reques body
    body = await request .body
    return{'request body':body.decode()}


