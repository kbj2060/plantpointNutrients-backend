from typing import Dict, Optional
from sqlalchemy.sql.sqltypes import DateTime

class Sensor:
    def __init__(self, name: str, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.name = name
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "createdAt": self.createdAt
        }
