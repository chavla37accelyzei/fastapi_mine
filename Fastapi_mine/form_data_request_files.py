# form is class that inherits from body
from fastapi import FastAPI,Form
from typing import Annotated
import requests

app = FastAPI()


@app.post("/login/")
async def login(username:Annotated[str,Form(...,minlength=3,maxlength=12)], 
                password:Annotated[str, Form(...,min_length=4,max_length=12)]):
    return {"username":username}

@app.post("/submitForm/")
async def submitForm(
    username:str=Form(...,min_length=3,max_length=12),
    email:str = Form(...,regex="[a-zA-Z0-9.%+-]@[a-zA--Z0-9-]+\.[a-zA-Z0-9]{2,4}$"),
    age:int = Form(...,gt=0)  #should > 0

):
    return  {"username": username, "email": email, "age": age}

data = {
    "username": "keerthi",
    "email": "keerthichavla@gmail.com",
    "age": 20
}


response = requests.post("http://localhost:120.0.0.800/submitForm",data=data)
print(response.json())