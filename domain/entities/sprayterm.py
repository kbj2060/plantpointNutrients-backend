from typing import Dict, Optional
from sqlalchemy.sql.sqltypes import DateTime


class SprayTerm:
    def __init__(
        self,
        period: int,
        id: Optional[int] = None,
        createdAt: Optional[DateTime]= None
        ):
        self.id = id
        self.period = period
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "period": self.period,
            "createdAt": self.createdAt
        }
