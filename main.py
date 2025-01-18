from utils import create_db
from fastapi import FastAPI
from fastapi.requests import Request

app = FastAPI()

@app.get("/")
def index(request: Request):
    print(request.u)
    print(request.headers)
    return "meow"
