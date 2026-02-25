from sqlalchemy.orm import Session
from . import tables, schemas

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = tables.Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(tables.Group).offset(skip).limit(limit).all()

def get_group_by_id(db: Session, group_id: int):
    return db.query(tables.Group).filter(tables.Group.id == group_id).first()

def update_group(db: Session, group_id: int, group: schemas.GroupCreate):
    db_group = db.query(tables.Group).filter(tables.Group.id == group_id).first()
    if db_group is None:
        return None
    db_group.name = group.name
    db.commit()
    db.refresh(db_group)
    return db_group

def delete_group(db: Session, group_id: int):
    db_group = db.query(tables.Group).filter(tables.Group.id == group_id).first()
    if db_group is None:
        return None
    db.delete(db_group)
    db.commit()
    return db_group