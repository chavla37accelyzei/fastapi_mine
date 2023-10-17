from fastapi import FastAPI, Form,Header,Cookie
app = FastAPI()

@app.post("/submit-form/")
async def submit_form(
    username: str = Form(..., min_length=3, max_length=20),
    email: str = Form(..., regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"),
    age: int = Form(..., gt=0)
):
    return {"username": username, "email": email, "age": age}

import requests

data = {
    "username": "keerthi",
    "email": "keerthichavla@gmail.com",
    "age": 20
}

response = requests.post("http://localhost:8000/submit-form/", data=data)
print(response.json())


#cookies
@app.get("/set-cookie/")
async def set_cookie():
    response = JSONResponse(content={"message": "Cookie set!"})
    response.set_cookie(key="user_id", value="12345", max_age=3600, httponly=True)
    return response

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/get-cookie/")
async def get_cookie(request: Request):
    user_id = request.cookies.get("user_id")
    return {"user_id": user_id}

#headers
@app.get("/process/")
async def process_headers(
    user_agent: str = Header(None, description="User-Agent header"),
    api_key: str = Header(..., description="API Key header")
):
    return {"User-Agent": user_agent, "API Key": api_key}