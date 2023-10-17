# bigger applications and multiple files

print("path operations in router")

# import module 
from fastapi import APIRouter,Header,HTTPException
router = APIRouter()

# users module

@router.get("/users/",tags=["users"])
async def read_users():
    return [{"username": "keerthi"}, {"username": "siddu"}]

@router.get("/users/me",tags=["users"])
async def read_user_me():
    return {"username":"prasanna"}

@router.get("/users/{username}", tags=["user"])
async def read_user(username: str):
    return {"username":username}



