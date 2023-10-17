from fastapi import FastAPI
app = FastAPI()

# create router
@app.get('/items/{item_id}')  #path parameter

def item(item_id):
    return {'id':item_id,'media_name':['youtube','insta','twitter'],'fav':'Durga prasanna'}

#creating another router url
@app.get('/client/')


#query_param:type=value_of_param
 
def client_details(limit:int=10,active:bool=True,):
    return {'client':'{} client details'.format(limit),'active':active}

#emegency:optional[str] = None,skip:int=2
#'emergency':emergency,'skiped':skip

print("if we want query our own parameters:declare at starting of para")
#clent_deatils()