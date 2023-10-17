# to cusomize various aspects of api routes
# path(), query() ,tags = []

# tags set of unquie tag strings for this item we can add tags to parameters

from enum import Enum
from fastapi import FastAPI
app = FastAPI()

class Tags(Enum) : #tags set of unquie tag strings for this item
    items = "items"
    user = "user"

@app.get("/items/",tags = [Tags.items])
async def get_items():
    return ['apple','apple products']

@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["steev", "modi",
            "prasanna"]




