# to provide additional information aabout api 
# we use meta data & doc urls using some attributes
print("to provide additional information aabout api \n  we use meta data & doc urls using some attributes")
print("\n attributes: tags = [] ,summary='' ,\n description etc..")

from fastapi import FastAPI



# we can also add additional metadata for different tags used to group our path operations 
tags_metadata=[{
    "name":"users",
    "description":"user operations"

},
{
    "name":"items",
    "description":"we can manage items",
    "external Docs":{
        "description":'Items external data',
        "url":"https://gmail.com"
    }
}]
app = FastAPI(
    openapi_tags = tags_metadata,          
    title="My API",
    description = "small desc of API it can use markdown",
    version = "0.0.1",
    terms_of_service="https://github.com/git" , # it can be url
    contact = dict(
        name = "keerhi_chavala", # contact is type of dict
        url = "http://keerthivandana58/github.com", 
        gmail = "vkeerthichavla@gmail.com"        
    ),

    license_info=dict(name = "Startup",url="https://www.startupindia.gov.in/")

)







# define routes
@app.get("/user/",tags = ['user'])
async def get_user():
    return [dict(name = "keerthi")]

@app.get("/items",tags=['items'])
async def read_item():
    return [dict(name = "ice cream",price = "10-100")]

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    """
    Read an item.
    
    Args:
        - **item_id**: The ID of the item to read.
        - **q** (optional): A query parameter for filtering items.
    
    Returns:
        - **item**: Details of the item.
    """
    








# static files
# we can serve static files automatically from a directory using static files

from fastapi.staticfiles import staticFiles

app.mount("/static",staticFiles(directory="static"),name="static")
#mounting means adding complete independent application in specific path
<link rel="stylesheet" href="/static/styles.css">
