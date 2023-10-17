from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware


print("There are many situations in which you need to notify an error to a client that is using our API.")
#HTTP status code in the range of 400 (from 400 to 499).

#This is similar to the 200 HTTP status codes (from 200 to 299). Those "200" status codes mean that somehow there was a "success" in the request.

#The status codes in the 400 range mean that there was an error from the client.

#Remember all those "404 Not Found" errors (and jokes)?

app = FastAPI()









items = {"foo": "The Foo Wreslers"}

@app.exception_handler()  #one type of decorator
@app.get("/items/{item_id}")
async def read_item(item_id:str):
    if item_id not in items:
        raise HTTPException(status_code=404,detail="Item not found")
    return {"item":items[item_id]}

#custom error handling


class UnicornException(Exception):
    #inherits the Exception class
    def __int__(self,name:str):
        self.name = name

@app.exception_handler(UnicornException)
async def uvicorn_exc_handler(request:Request,exc:UnicornException):
    return JSONResponse(status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},)


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name =='yaho':
        raise UnicornException(name=name)
    return {"unicorn_name":name}
#/unicorns/yolo, ->the path operation will raise a UnicornException.

# Middle ware error -> perform additional error processig ar global

async def custom_err_middleware(request:Request,call_next):
        try:
             response = await call_next(request)
             return response
             
    
        except HTTPException as exc:
             return JSONResponse(content={"error": exc.detail}, status_code=exc.status_code)
        
app.middleware.append(custom_err_middleware)