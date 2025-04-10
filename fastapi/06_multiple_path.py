from fastapi import FastAPI

app = FastAPI()


# You can declare multiple path parameters and query parameters at the same time,
# FastAPI knows which is which.
# The order of the path parameters does not matter. They will be detected by name.
# http://127.0.0.1:8000/users/66/items/78?q=3e
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        item_id: str,
        user_id: int,
        q: str | None = None,
        short: bool = False,
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
