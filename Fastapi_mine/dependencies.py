
from fastapi import Depends , FastAPI,Body,HTTPException,Header
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer #  it is class to secure password 


# dependencies :Depends class to inject these dependencies into your route handlers
#a powerful feature that allows you to provide dependencies, such as 
#database connections or configuration settings,
app = FastAPI()

fakedb = [{"itme1" : "smart phone"},{"item2":"laptop"},{"item3":"desktop"}]

async def hello():
    return "hello sir"


async def common_parameters(q:str | None = None, skip:int = 0,limit:int =100,b:str=Depends(hello)):
    return {"q":q, "skip":skip, "limit":limit}
# here we derive hello dependency


@app.get("/items/")
async def read_items(common:dict=Depends(common_parameters)):
    return common
# here we use common_parameters as dependency

print("classes - dependencies ")
#2. use class as dependency

class commonQueryParams:
    def __init__(self,q:str|None,skip:int=0 , limit:int=100):
        self.q =q
        self.skip =skip
        self.limit = limit

@app.get("/items2/")
async def read_items(common:commonQueryParams = Depends(commonQueryParams)):
    response ={} #empyt dic

    if common.q:
        response.update({'q': common.q})

    items = fakedb[common.skip:common.skip + common.limit] #assign  items to item
    response.update({'itmes':items})  # add items to response dict

    return response

# we can use all commonqery prams class variables in readitems()  because of dendencies


#3.sub Dependencies
#from fastapi import Depends,Body
def query_extractor(q:str | None = None):
    return q

def query_or_body_extract(q:str = Depends(query_extractor),last_query:str | None=Body(None)):
    if not q:
        return last_query
    return q

@app.post("/items/")
async def try_query(query_or_body:str = Depends(query_or_body_extract)):
    return {"query_or_body":query_or_body}


# when we call query_or_body ->query_extractor  sub dependency


#4.dependencies in path operators and gloabal 
#put dependencies at routers
async def verify_token(x_token: str= Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str= Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item1": "laptop"}, {"item2": "desktop"}]


#puting dependencies at globaly for total application
app= FastAPI(dependencies=[Depends(verify_token),Depends(verify_key)])
    
