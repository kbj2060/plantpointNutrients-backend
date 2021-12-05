from typing import  Optional, Dict
from repository.models import Section

# 기계
# 1. 솔레노이드 밸브 5ea
# 2. 물공급용 워터펌프
# 3. 스프레이용 워터펌프
# 4. 양액공급용 워터펌프 2ea


class Machine:
    def __init__(self, name: str, section_id: Section,  purpose:str, id: Optional[int]= None, createdAt: Optional[str]= None):
        self.id = id
        self.name = name
        self.section_id = section_id
        self.purpose = purpose
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "section_id": self.section_id,
            "purpose": self.purpose,
            "createdAt": self.createdAt
        }
