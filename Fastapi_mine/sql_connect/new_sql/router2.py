from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import AddUser
from main2 import get_db
from models2 import User

router = APIRouter(prefix="/api")

@router.post("/users/")
async def create_user(create:AddUser, db:User = Depends(get_db),response_model =None):
    db_user= create_user(create)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/{user_id}")
async def read_user( current_user: User = Depends(get_db),response_model = None):
    user = read_user(current_user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#@router.post("/users")
#def add_user(data:AddUser, current_user: Users=Depends(get_current_user)):
    #response = user_service.add_user(data)
    #return response