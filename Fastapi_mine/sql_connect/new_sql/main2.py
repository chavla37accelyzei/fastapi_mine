from fastapi import FastAPI ,Depends, HTTPException
from sqlalchemy import create_engine,inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker # generates new session objects
from models2 import Base,User



from schema import AddUser
#from router2 import router

#from database import get_db




#Base = declarative_base() #class for declarative definitions,schemas ,relationships

# Database URL
DATABASE_URL = "mysql+pymysql://root:prasanna@123@127.0.0.1:3306/testdb"

# create DB engine
engine = create_engine(DATABASE_URL)




#Crate Tables on startupu


#session class to handle db connection
sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind =engine)



app=FastAPI()


    

    
#@app.on_event("startup")
#async def startup():
    #await engine.connect()

#@app.on_event("shutdown")
#async def shutdown():
    #await engine.disconnect()

#dependency


def get_db():
    db = sessionlocal(bind=engine)  #databse session
    try:
        yield db      # returns the databse session to route

    except:
        return "database error"
    
    finally :
        db.close()




#@router.post("/users")
#def add_user(data:AddUser, current_user: Users=Depends(get_current_user)):
    #response = user_service.add_user(data)
    #return response

#app.include_router(router)


@app.post("/User/")
async def create_user(create:AddUser, db:User = Depends(get_db),response_model =None):
    db_user= create_user(create)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
 
    

#read item using get
@app.get("/User/{user_id}")
async def read_user(user_id:int,db:User = Depends(get_db)):
    db=sessionlocal()
    new_user = User(
       email="keerthi@gmail.com",
       username="keerthi"
       #username = db.username,
       #email = db.email
    )
    # 
    # 
    # if user.id == user_id :
        
    db.close()
    return {"new user":new_user}
    #user = read_user(current_user)
    #if user is None:
        #raise HTTPException(status_code=404, detail="User not found")
    #return user 
    


#create utem using post


 #CRUD FUNCTIONS CREATE,USE,DELETE
'''
@app.post("/items/")
def create_item(item:Item,db: Session = Depends(get_db)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

#read item using get
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db),response_model=None):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404,detail="item not found")
    return item



# retrive tables from

@app.get("/tables/")
async def get_tables(db: Session = Depends(Base)):
    with db as session:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        return {"tables": tables}
'''

