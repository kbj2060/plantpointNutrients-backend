from typing import Dict, Optional
from sqlalchemy.sql.sqltypes import DateTime

class Sensor:
    def __init__(self, name: str, pin: int, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.name = name
        self.pin = pin
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "pin": self.pin,
            "createdAt": self.createdAt
        }
