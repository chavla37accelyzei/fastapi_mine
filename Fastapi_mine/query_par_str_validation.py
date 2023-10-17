from fastapi import FastAPI,Query
from pydantic import BaseModel

app = FastAPI()

class QueryParams(BaseModel):
    search_query:str = Query(---, title='Search Query',min_length=3,max_length=50,regex="^[a-zA-Z0-9__]+$")

#user query par in endpoint
@app.get("/search/")
async def search_items(query_params:QueryParams): #passing BaseModel
    return{"search query":query_params.search_query}


#/search/?search_query=my_query123
