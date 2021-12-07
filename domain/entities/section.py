from typing import Dict, Optional
from sqlalchemy.sql.sqltypes import DateTime

class Section:
    def __init__(self, main: str, sub: int, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.main = main
        self.sub = sub
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "main": self.main,
            "sub": self.sub,
            "createdAt": self.createdAt
        }
