from typing import  Optional, Dict
from sqlalchemy.sql.sqltypes import DateTime

class Temperature:
    def __init__(self, value: float, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.value = value
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "value": self.value,
            "createdAt": self.createdAt
        }
