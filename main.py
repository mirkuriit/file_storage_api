from utils import create_db
from fastapi import FastAPI
from fastapi.requests import Request

app = FastAPI()
create_db()
@app.get("/")
def index(request: Request):
    print(sorted(dict(request.headers).keys()))
    print(request.client)
    print(request.url)
    return "meow"
