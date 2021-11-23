from typing import Dict, Optional


class Sensor:
    def __init__(self, name: str, section: str, created: Optional[str]= None):
        self.name = name
        self.section = section
        self.created = created
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "section": self.section,
            "created": self.created
        }
