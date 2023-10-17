from sqlalchemy.orm import Session

from model import * 
from schema import *


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
     #model.user

#def get_user_by_email(db: Session, email: str):
    #return db.query(model.User).filter(model.User.email == email).first()


#def get_users(db: Session, skip: int = 0, limit: int = 100):
    #return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user:User):
    #schema.user
    db_user =User(email=user.email,username =user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session):
    return db.query(Item).all()


def create_user_item(db: Session, item:Item, user_id: int):
    db_item =Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item