from typing import  Optional, Dict
from sqlalchemy.sql.sqltypes import DateTime

class User:
    def __init__(self, name: str, password: str, type: str, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.name = name
        self.password = password
        self.type = type
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "type": self.type,
            "createdAt": self.createdAt
        }
