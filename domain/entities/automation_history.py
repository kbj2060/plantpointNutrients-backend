from typing import  Optional, Dict

from sqlalchemy.sql.sqltypes import DateTime
from repository.models import Section
from datetime import datetime
# 기계
# 1. 솔레노이드 밸브 5ea
# 2. 물공급용 워터펌프
# 3. 스프레이용 워터펌프
# 4. 양액공급용 워터펌프 2ea

class AutomationHistory:
    def __init__(
        self,
        subject: str,
        start: DateTime,
        end: DateTime,
        success: bool,
        id: Optional[int]= None
        ):
        self.id = id
        self.subject = subject
        self.start = start
        self.end = end
        self.success = success
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "subject": self.subject,
            "start": self.start,
            "end": self.end,
            "success": self.success
        }
