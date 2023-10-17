from sqlalchemy.orm import Session
from main2 import engine


def get_db():
    db = Session(bind=engine)  #databse session
    try:
        yield db      # returns the databse session to route

    except:
        return "database error"
    
    finally :
        db.close()

        #