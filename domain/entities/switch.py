from typing import Dict, Optional
from sqlalchemy.sql.sqltypes import DateTime

class Switch:
    def __init__(self, machine_id: int, section_id: int, status: int, controlledBy_id: int, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.section_id = section_id
        self.machine_id = machine_id
        self.status = status
        self.controlledBy_id = controlledBy_id
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "section_id": self.section_id,
            "machine_id": self.machine_id,
            "status": self.status,
            "controlledBy_id": self.controlledBy_id,
            "createdAt": self.createdAt
        }
