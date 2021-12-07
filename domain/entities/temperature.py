from typing import  Optional, Dict
from sqlalchemy.sql.sqltypes import DateTime

class Temperature:
    def __init__(self, section_id: int, sensor_id: int, value: float, id: Optional[int] = None, createdAt: Optional[DateTime]= None):
        self.id = id
        self.section_id = section_id
        self.sensor_id = sensor_id
        self.value = value
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "section_id": self.section_id,
            "sensor_id": self.sensor_id,
            "value": self.value,
            "createdAt": self.createdAt
        }
