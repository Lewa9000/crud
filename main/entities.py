from db import engine, sessionlocal
import models

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


models.Base.metadata.create_all(bind=engine)
 

templates = Jinja2Templates(directory="templates")
 

app = FastAPI()
 

app.mount("/static", 
          StaticFiles(directory="static"), 
          name="static")
 

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
 

