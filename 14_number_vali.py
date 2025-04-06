from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


# gt: Greater Than
# le: Less than or Equal
@app.get("/items/{item_id}")
async def read_items(
        item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
        q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# float number validation
@app.get("/data/{item_id}")
async def read_items(
        *,
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: str,
        size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results
