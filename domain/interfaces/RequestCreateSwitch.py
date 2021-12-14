from typing import  Optional
from pydantic import BaseModel


class RequestCreateSwitch(BaseModel):
    status: Optional[bool]
    machine_id: Optional[int]
    controlledBy_id: Optional[int]
    name: Optional[str]