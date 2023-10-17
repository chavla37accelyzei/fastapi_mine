from fastapi import Body, FastAPI
from datetime import datetime,time,timedelta
from uuid import UUID
from typing import Annotated

app = FastAPI()

@app.post("/items/{item_id}")
async def read_items(
    item_id:UUID
    start_datetime:Annotated[datetime|None,Body(default=None)],
    end_datetime :Annotated[datetime | None,Body(default=None)],
    repeat_at:Annotated[time|None,Body(default=None)],
    process_after : Annotated[timedelta|None,Body(default=None)]=None,


):

start_process = start_datetime + process_after
duration = end_datetime - start_process

return {
    "itemid":item_id,
    "start_datetime":start_datetime,
    "end_datetime" : end_datetime,
    "repeat_at" :repeate_at
}

