from typing import Dict, Optional
from sqlalchemy.sql.sqltypes import DateTime


class WaterSupply:
    def __init__(self, section_id: int, quantity: int, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.section_id = section_id
        self.quantity = quantity
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "section_id": self.section_id,
            "quantity": self.quantity,
            "createdAt": self.createdAt
        }
