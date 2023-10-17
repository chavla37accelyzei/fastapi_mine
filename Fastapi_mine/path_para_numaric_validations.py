from fastapi import FastAPI,Path
from pydantic import BaseModel

app = FastAPI()

#pydantic model for path para
class pathparms(BaseModel):
    item_id:int = Path(-, title='itemid',description = 'unique_id',ge = 1,le=1000)

# using path para in 
@app.get('/item/{itme_id}')
async def read_item(itemid:int = Path(-,title ='item_id',description ='uniqueid',ge=1,le = 1000)) :
    
    