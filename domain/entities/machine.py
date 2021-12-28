from typing import  Optional, Dict

from sqlalchemy.sql.sqltypes import DateTime
from repository.models import Section
from datetime import datetime
# 기계
# 1. 솔레노이드 밸브 5ea
# 2. 물공급용 워터펌프
# 3. 스프레이용 워터펌프
# 4. 양액공급용 워터펌프 2ea

class Machine:
    def __init__(
        self,
        name: str,
        pin: int,
        id: Optional[int]= None,
        createdAt: Optional[DateTime]= None
        ):
        self.id = id
        self.name = name
        self.pin = pin
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "pin": self.pin,
            "createdAt": self.createdAt
        }
