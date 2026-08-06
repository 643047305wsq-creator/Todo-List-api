from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from practice_2 import Sessionlocal,Book,B,engine
from sqlalchemy.orm import Session
from typing import List
app=FastAPI()
B.metadata.create_all(bind=engine)
def get():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()
class A(BaseModel):
    name:str
    author:str
    is_read:bool
    id:int
    class Config:
        from_attributes=True
@app.post("/books/",response_model=A)
def add(a:A,db:Session=Depends(get)):
    add_book=Book(name=a.name,author=a.author)
    db.add(add_book)
    db.commit()
    db.refresh(add_book)
    return add_book
class P(BaseModel):
    is_read:bool
    class Config:
        from_attributes=True
@app.get("/books",response_model=List[A])
def get_db(book_is_read:bool,db:Session=Depends(get)):
    get_book=db.query(Book).filter_by(is_read=book_is_read).all()
    return get_book
@app.put("/books/{book_id}",response_model=P)
def put(book_id:int,p:P,db:Session=Depends(get)):
    put_book=db.query(Book).filter(Book.id==book_id).first()
    if put_book is None:
        raise HTTPException(status_code=404,detail="没有查询到这条记录")
    put_book.is_read=p.is_read
    db.commit()
    db.refresh(put_book)
    return put_book
@app.delete("/books/{book_id}")
def delete(book_id:int,db:Session=Depends(get)):
    delete_book=db.query(Book).filter(Book.id==book_id).first()
    if delete_book is None:
          raise HTTPException(status_code=404,detail="没有查询到这条记录")
    db.delete(delete_book)
    db.commit()
    return {"message":"记录已删除"}