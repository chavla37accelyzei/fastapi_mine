from fastapi import FastAPI ,Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker  # generates new session objects
from models import Base,Item,user,employee



Base = declarative_base #class for declarative definitions,schemas ,relationships

# Database URL
DATABASE_URL = "mysql+pymysql://root:prasanna@123@127.0.0.1:3306/cricket"

# create DB engine
engine = create_engine(DATABASE_URL)

#Crate Tables on startup


#session class to handle db connection
sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind =engine)
app=FastAPI()



#@app.on_event("startup")
#async def startup():
    #await engine.connect()

#@app.on_event("shutdown")
#async def shutdown():
    #pawait engine.disconnect()

#dependency
app = FastAPI()
def get_db():
    db = sessionlocal()  #databse session
    try:
        yield db      # returns the databse session to route

    except:
        return "database error"
    
    finally :
        db.close()

#create utem using post

# CRUD FUNCTIONS CREATE,USE,DELETE
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





