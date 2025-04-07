from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool = True
    if_modified_since: str | None = None
    transparent: str | None = None
    x_tag: list[str] = []


# For example, if you have a header parameter save_data in the code,
# the expected HTTP header will be save-data, and it will show up like that in the docs.
# If for some reason you need to disable this automatic conversion,
# you can do it as well for Pydantic models for header parameters.
@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header(convert_underscores=True)]):
    return headers
