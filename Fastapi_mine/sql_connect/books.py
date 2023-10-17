from fastapi import FastAPI ,Depends,HTTPExcption
from pydantic import BaseModel,Field


from sqlalchemy.orm import Session,sessionmaker  # generates new session objects
from models import Base,Item

print("Defining schema")
# Database URL
#DATABASE_URL = "sqllite://test.db"

# create DB engine
#engine = create_engine(DATABASE_URL)

#Crate Tables on startup
#Base.metadata.create_all(bind = engine)

#session class to handle db connection
#sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind =engine)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

books = []

class Book(BaseModel):

    title:str = Field(min_length=1)
    author:str = Field(min_length=1,max_len=100)
    description:str = Field(min_len=1,max_length=100)
    rating:int = Field(gt= 0)


def get_db():
    db = sessionlocal()  #databse session
    try:
        yield db      # returns the databse session to route

    except:
        return "database error"
    
    finally :
        db.close()




#add book model to db
@app.get("/")
def readbook(db:Session=Depends(get_db)):
    return db.query(models.books).all()
    

@app.post("/create_book/")
def create_book(book:Book,db:Session=Depends(get_db)):
    bookmodel = models.books()
    bookmodel.title=book.title
    bookmodel.author = book.author
    bookmodel.ratings = book.ratings

    db.add(book.model)

#create utem using post
@app.post("/items/")
def create_item(item:Item,db: Session = Depends(get_db)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

#read item using get
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPExcption(status_code=404,detail="item not found")
    return item




