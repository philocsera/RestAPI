from fastapi import FastAPI, Depends
from .database import engine, Base, get_db
from sqlalchemy.orm import Session
from . import tables as models
from . import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/db")
def read_db(db: Session = Depends(get_db)):
    return {"message": "Database connection successful"}

@app.post("/groups/", response_model=schemas.GroupResponse)
def create_new_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)