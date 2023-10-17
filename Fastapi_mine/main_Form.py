from fastapi import  FastAPI ,Form,Body,Request,Body,File,File,UploadFile,Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import List

app = FastAPI()

#Basemodel
class read(BaseModel):
    name:str
    country:str
    age:int
    salary:float = None #not much required


templates=Jinja2Templates(directory="html.html")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def token_generate(form_data:OAuth2PasswordRequestForm=Depends()):
    print(form_data)
    return {"access_token":"form_data.username","token_type":'beares'}


#if user name presnallow inthis method
@app.post("/user/profilepic") #user with profilephots
async def profile_pic(token:str = Depends(oauth2_scheme)):
    print(token)
    return {
        "user":"keerthi",
        "profilepic" :"my face"
    }




@app.post("/language/") #router
async def language(language_name:str=Form(...),country:str=Form(...)):
    return {"name":language_name,"country":country}

# sending data using get,post,put,delete methods
list_of_users = list()


@app.get("/home/{username}") #router
def write_home(username:str,age:int):
    return{
        "username":username,
        'age':age
    }

@app.post("/postdata/") # we can send data via header only
def put_data(username:str):
    list_of_users.append(username)
    return{
        'username':list_of_users
    }

#send data via put request 
@app.put('/username/{user_name}')
def put_data(username:str):
    print(username)
    list_of_users.append(username)
    return {'usename':username}

# delete data via DELETE()
@app.delete("/deleteData/{username}")
def delete_Data(username:str):
    list_of_users.remove(username)
    return list_of_users


print(" defineing all request methods in single route")
@app.api_route("/homedata/", methods = ["GET","POST","PUT","DELETE"])
def handle(username:str):
    return {"username": list_of_users}

''' @app.get("/send/")
def post_data(read:read,spouse_status:str=Body(...)): #accepting basevalues
    return{
        "name":read.name,
         "spouse_status":spouse_status
    }
    '''

# Body -> comeswith post request

#sending data dynamically
@app.get("/home/{username}",response_class=HTMLResponse) #send data to html page
def write_home(request:Request,username:str):
    return templates.TemplateResponse('html.html',{request:request,"username":username})
#what is the request coming from user that use as context.
# we send username to html page

#submit form
@app.post("/submitform")
async def handle_form(assignment:str=Form(...),assignment_file:UploadFile=Form(...)):
    print(assignment)
    print(assignment_file.filename)
    content_assignment = await assignment.read()
    print(content_assignment)

