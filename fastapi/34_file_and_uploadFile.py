from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# 小文件: bytes
@app.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


# 大文件: UploadedFile
@app.post("/uploadfile/")
async def create_upload_file(
        file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}
