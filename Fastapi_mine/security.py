# for security purpose import oAuth2
from fastapi import FastAPI,dict, HTTPException, status
from fastapi.security import OAuth2PasswordBearer ,OAuth2PasswordRequestForm
#  it is class to secure password 
from fastapi import Depends
from pydantic import BaseModel

app = FastAPI()



oauth2_scheme = OAuth2PasswordBearer(tockenUrl = "token")
#The same way we use Pydantic to declare bodies, use it

# create a database
fake_database = {

    "keerthi": {

        "username":"KeerthiChavla" ,
        "email":"vkeerthichavla@gmail.com",
        "fullname":"Keerthi chavla vandana",
        "hashed_password":"mysismyprinces",  # it checks plain password and hashed password
        "disable":False


     } ,
    "prasanna" : {
        "username":"prasanna",
        "email" : "durgaprasanna@gmail.com",
        "fullname":"v.DurgaPrasanna",
        "hashed_password":"mysismyworld",
        "disable": True


    }
}


def fake_hash_password(password: str):
    return f"fakehashed password:{password}"

def userInDb(user):
    hashed_password = str

class user(BaseModel):
    username:str
    email:str|None = None
    full_name:str |None=None
    disabled:bool |None = None

def get_user(db,username:str):  #username=token
    if username in db:
        user_dict = db[username]
        return userInDb(**user_dict)
    

def fake_decode_token(token): #definition
    return get_user(fake_database,token) #return these to get_user method
    #return user(
       # username = token + "fakedecoded" , email = "keerthi@gmail.com" ,full_name ="keerthi chavla"
   # )

async def get_current_user(token:str= Depends(oauth2_scheme)): #dervies dependency
                        # name:type=field()
    user = fake_decode_token(token)
    return user




@app.get("/items/")  #decorator
async def read_items(token: str = Depends(oauth2_scheme)) : #using dependencies
    return {"token":token}

@app.get("/users/me")
async def get_me(current_user:user=Depends(get_current_user)):
   return current_user




# security with json
from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)




