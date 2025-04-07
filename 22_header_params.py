from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


@app.get("/data/")
async def read_tokens(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}
