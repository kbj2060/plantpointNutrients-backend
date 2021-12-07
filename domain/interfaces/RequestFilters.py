from typing import  Optional
from pydantic import BaseModel


class RequestFilters(BaseModel):
    limit: Optional[int] = 0
    today: Optional[bool] = False