from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from database import sessionlocal,engine,Base,Todo
from sqlalchemy.orm import Session
from typing import List
app=FastAPI()
def a():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close
Base.metadata.create_all(bind=engine)
class Todocreate(BaseModel):
    title:str
@app.post("/todos/")
def create_todo(todocreate:Todocreate,db:Session=Depends(a)):
    new_todo=Todo(title=todocreate.title,completed=False)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
class R(BaseModel):
    id:int
    title:str
    completed:bool
    class Config:
        from_attributes=True
@app.get("/todos/",response_model=List[R])
def read(db:Session=Depends(a)):
    todos=db.query(Todo).all()
    return todos
class TodoUpdate(BaseModel):
    title:str
    completed:bool
@app.put("/todo/{todo_id}",response_model=R)
def update_todo(todo_id:int,todo_update:TodoUpdate,db:Session=Depends(a)):
    todos=db.query(Todo).filter(Todo.id==todo_id).first()
    if todos is None:
            raise HTTPException(status_code=404,detail="没有查询到这条记录")
    todos.title=todo_update.title
    todos.completed=todo_update.completed
    db.commit()
    db.refresh(todos)
    return todos
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(a)):
    todos=db.query(Todo).filter(Todo.id==todo_id).first()
    if todos is None:
            raise HTTPException(status_code=404,detail="没有查询到这条记录")
    db.delete(todos)
    db.commit()
    return {"message":"已删除这条记录"}
