from fastapi import FastAPI

app = FastAPI()     #object creation , app as obj name

@app.get('/')       #router creation

def home():
    return {'name':'prasanna','city':'rajam'}

# to create another function
#create another url
@app.get('/items/')  #it is one url with itmes as name

def list_items():
    return {'company':["accelyzei","tcs","apple"],'type':'MNCs & STARTUPS'}
   # return ["prasanna","sada","aswini,"dinesh","home"]

@app.get('/items/{item_id}')   #sending path parameters

def item(item_id):   #path param(item_id) to function
    return {'id':item_id,'company':'accelyzei','location':'hyd'}


print("specifiying data type to path parameter")
@app.get('/item/{item_id}')

def items(item_id:int):
    return {'id_count':item_id,'name':'Durga Prasanna','goal':'IPS'}
