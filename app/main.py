from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from psutil import *

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"