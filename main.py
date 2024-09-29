from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

# http://localhost:8080/
@app.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@app.put("/items/{item_id}", status_code=200)
async def update_item(item_id: int, item: dict, q: str = Query(None)):
    response_data = {
        "item_id": item_id,
        "name": item["name"],
        "description": item["description"],
        "price": item["price"],
        "tax": item["tax"],
    }
    
    if q:
        response_data["q"] = q 

    return response_data


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
