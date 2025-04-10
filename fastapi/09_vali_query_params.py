from typing import Annotated
from fastapi import FastAPI
from fastapi import Query

app = FastAPI()


# Here we are using Query() because this is a query parameter.
# Later we will see others like Path(), Body(), Header(), and Cookie(),
# that also accept the same arguments as Query().
# pattern: regular expression
# Having a default value of any type, including None, makes the parameter optional (not required).
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = "XXXX"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
