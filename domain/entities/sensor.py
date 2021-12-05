from typing import Dict, Optional

class Sensor:
    def __init__(self, name: str, section_id: int, id: Optional[int] = None, createdAt: Optional[str]= None):
        self.id = id
        self.name = name
        self.section_id = section_id
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "section_id": self.section_id,
            "createdAt": self.createdAt
        }
