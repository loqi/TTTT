from ctypes.wintypes import PLARGE_INTEGER
from io import SEEK_CUR
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


