from pydantic import BaseModel
from typing import Optional

class GroupCreate(BaseModel):
    name: str

class GroupResponse(BaseModel):
    id: int

    class Config:
        from_attribute = True