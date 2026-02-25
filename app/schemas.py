from pydantic import BaseModel
from typing import Optional

class GroupCreate(BaseModel):
    name: str

class GroupResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attribute = True