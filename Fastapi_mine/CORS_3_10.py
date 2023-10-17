from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.google.com",
    "https://localhost.tiangolo.com",
    "https://gmial.com",
    "http://localhost",
    "http://localhost:8080",
]

#add to middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,  # allow any origin
    allow_credentials = True,
    allow_methods = ["*"], # allow get ,post etc..
    allow_headers = ["*"],  # requests all types of https headers
)




@app.get("/")
async def main():
    return {"message": "Hello World"}