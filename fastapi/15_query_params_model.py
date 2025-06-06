from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


# ex url:
# http://127.0.0.1:8000/items/?limit=3&offset=2&order_by=created_at&tags=string2&tags=string1
@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query


# Forbid Extra Query Parameters
class FilterParams2(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []
