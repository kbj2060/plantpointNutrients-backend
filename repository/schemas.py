from typing import  Optional
from pydantic import BaseModel
from datetime import datetime


class Machine(BaseModel):
    id:Optional[int]
    name: str
    section: str
    purpose: str
    created: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Sensor(BaseModel):
    id:int
    name: str
    section: str
    created: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True