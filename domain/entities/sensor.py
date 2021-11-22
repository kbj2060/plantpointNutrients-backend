from typing import Dict


class Sensor:
    def __init__(self, name: str, section: str):
        self.name = name
        self.section = section
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "section": self.section,
        }
