from typing import Dict, Optional

from sqlalchemy.sql.sqltypes import DateTime

class Report:
    def __init__(
        self, 
        section_id: int, 
        level: int, 
        isFixed: int, 
        id: Optional[int] = None, 
        machine_id: Optional[int] = None, 
        createdAt: Optional[DateTime]= None
    ):
        self.id = id
        self.section_id = section_id
        self.level = level
        self.machine_id = machine_id
        self.isFixed = isFixed
        self.createdAt = createdAt

    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "section_id": self.section_id,
            "machine_id": self.machine_id,
            "level": self.level,
            "isFixed": self.isFixed,
            "createdAt": self.createdAt
        }
