from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()
#define parametes for request body
class RequestBodyParams(BaseModel):
    name: str
    ph_no :int
    account:bool

@app.post("/process/")
async def process_request_body(params:RequestBodyParams):
    return {
        "name":params.name,
        "ph_no":params.ph_no,
         "account":params.account
    }

# post request with Json data
data = {
    "name":"Keerthi",
    "ph no":37,
    "account_no":True
}

result = requests.post("http://localhost:120.0.0.800/process",json=data)

print(result.json())