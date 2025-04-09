from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    print(type(item))
    json_compatible_item_dict = jsonable_encoder(item)
    print(json_compatible_item_dict)
    fake_db[id] = json_compatible_item_dict
    print(fake_db)
