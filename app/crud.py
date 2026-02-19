from sqlalchemy.orm import Session
from . import tables, schemas

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = tables.Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group