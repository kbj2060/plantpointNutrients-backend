from typing import Dict, Optional
from sqlalchemy.sql.sqltypes import DateTime


class WaterSpray:
    def __init__(self, section_id: int, operating_time: int, period: int, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.section_id = section_id
        self.operating_time = operating_time
        self.period = period
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "section_id": self.section_id,
            "operating_time": self.operating_time,
            "period": self.period,
            "createdAt": self.createdAt
        }
