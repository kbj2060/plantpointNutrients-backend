from typing import Dict, Optional

from sqlalchemy.sql.sqltypes import DateTime

class Report:
    def __init__(
        self, 
        level: int,
        problem: str,
        isFixed: int, 
        id: Optional[int] = None, 
        createdAt: Optional[DateTime]= None
    ):
        self.id = id
        self.level = level
        self.problem = problem
        self.isFixed = isFixed
        self.createdAt = createdAt

    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "problem": self.problem,
            "level": self.level,
            "isFixed": self.isFixed,
            "createdAt": self.createdAt
        }
