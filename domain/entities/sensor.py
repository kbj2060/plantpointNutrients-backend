from typing import Dict, Optional

from repository.models import Section


class Sensor:
    def __init__(self, name: str, section: Section, createdAt: Optional[str]= None):
        self.name = name
        self.section = section
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "section": self.section,
            "createdAt": self.createdAt
        }
