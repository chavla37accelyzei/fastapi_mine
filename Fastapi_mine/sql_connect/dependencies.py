from fastapi import FastAPI , Header,HTTPException,Depends
# we are going to need some dependencies used in several places of the application
# so we can maintain our dependenci modules: app/dependencies.py
# to read custom r header X-Tocken
async def get_token_header(x_token:str = Header()):
    if x_token != "fake-secret-token":
        raise HTTPException(status_code=400,detail="X-Token header invalid")

async def get_query_token(token:str):
    if token != "keerthi":
        raise HTTPException(status_code=404,detail = "no keerthi token provided")


