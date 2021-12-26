from typing import Optional
from pydantic import BaseModel


class ReadUser(BaseModel):
    email__eq: Optional[str]
    name__eq: Optional[str]