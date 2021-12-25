from typing import  Optional
from pydantic import BaseModel


class RequestCreateSwitch(BaseModel):
    status: bool
    machine_id: int
    controlledBy: str
    name: str
