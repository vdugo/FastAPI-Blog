from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import models
from database.database import engine
from routers import post

app = FastAPI()
app.include_router(post.router)

@app.get('/')
def hello_world():
    return "hello world"

models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
    