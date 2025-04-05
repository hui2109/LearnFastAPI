from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


# Note: the method is "post"!
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# You can declare path parameters and request body at the same time.
# FastAPI will recognize that the function parameters that
# match path parameters should be taken from the path,
# and that function parameters that are declared to be Pydantic models
# should be taken from the request body.
# # Note: the method is "put"!
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


# Request body + path + query parameters
# If the parameter is also declared in the path, it will be used as a path parameter.
# If the parameter is of a singular type (like int, float, str, bool, etc.)
# it will be interpreted as a query parameter.
# If the parameter is declared to be of the type of Pydantic model,
# it will be interpreted as a request body.
@app.put("/data/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
