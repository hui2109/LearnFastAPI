from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


# A path parameter is always required as it has to be part of the path.
# Even if you declared it with None or set a default value,
# it would not affect anything, it would still be always required.
@app.get("/items/{item_id}")
async def read_items(
        item_id: Annotated[int, Path(title="The ID of the item to get")] = None,
        q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
