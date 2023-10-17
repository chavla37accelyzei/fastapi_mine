from typing import Annotated

from fastapi import FastAPI, File, Form,UploadFile,Body

app = FastAPI()

'''@app.post("/logn/") #router
async def login(username:str = Form(...,),
                password:str=Form(...),
                ):
    return ('username',username)

@app.post("/login-json/")
async def loginjson(username:str=Body(...),
                    password:str=Body())
'''
