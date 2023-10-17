from fastapi import FastAPI,HTTPExcption,Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

#custom middleware
# Define a middleware function

app=FastAPI()


async def custom_middleware(request:Request,call_next):
    # this code runs before handlng the request
    print("Before request")

    response = await call_next(request) # continue to next route

    print("After request")

    return response

app.middleware("http")(custom_middleware) #allow http request



app.get("/")  # router will execite after the middleware
async def read():
    return {"message":"Hello mom and sis"}
