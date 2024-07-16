from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for request validation
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Define some dummy data
items = {
    1: {"name": "Item 1", "description": "The first item", "price": 10.0, "tax": 1.0},
    2: {"name": "Item 2", "description": "The second item", "price": 20.0, "tax": 2.0},
}

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Read item endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

# Create item endpoint
@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item.dict()
    return items[item_id]

# Update item endpoint
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id] = item.dict()
        return items[item_id]
    return {"error": "Item not found"}

# Delete item endpoint
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted successfully"}
    return {"error": "Item not found"}
