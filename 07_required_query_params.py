from fastapi import FastAPI

app = FastAPI()


# Here the query parameter needy is a required query parameter of type str.
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


# And of course, you can define some parameters as required,
# some as having a default value, and some entirely optional:
# neddy is required, skip has a default value and limit are optional.
@app.get("/items/{item_id}")
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
