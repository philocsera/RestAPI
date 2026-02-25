from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/groups/", response_model=list[schemas.GroupResponse])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = crud.get_groups(db=db, skip=skip, limit=limit)
    return groups

@app.get("/groups/{group_id}", response_model=schemas.GroupResponse)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group_by_id(db=db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@app.patch("/groups/{group_id}", response_model=schemas.GroupResponse)
def update_group(group_id: int, group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_group = crud.get_group_by_id(db=db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    db_group.name = group.name
    db.commit()
    db.refresh(db_group)
    return db_group

@app.delete("/groups/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    retn = crud.delete_group(db=db, group_id=group_id)
    if retn is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"message": "Group deleted successfully"}