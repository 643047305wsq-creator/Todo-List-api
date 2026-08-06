from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
class Item(BaseModel):
    name:str
    price:float
    is_offer:bool=False
@app.post("/items/")
def create_item(item: Item):
    return {"received": item}