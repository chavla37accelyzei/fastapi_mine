#request nad response models

from pydantic import BaseModel

''' class UserBase(BaseModel):
    email: str = None


class UserCreate(UserBase):
    password: str=None
    '''


class AddUser(BaseModel):
    id: int=None
    username:str=None
    email:str=None

class Config:
    orm_mode = True
    

    


