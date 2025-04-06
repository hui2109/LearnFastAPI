from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


# To declare a query parameter q that can appear multiple times in the URL,
# you can write:
# ex url: http://localhost:8000/items/?q=foo&q=bar

# To declare a query parameter with a type of list,
# you need to explicitly use Query,
# otherwise it would be interpreted as a request body.
@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items
