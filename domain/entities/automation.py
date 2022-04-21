from typing import  Optional, Dict

from sqlalchemy.sql.sqltypes import DateTime
from repository.models import Section
from datetime import datetime

class AutomationHistory:
    def __init__(
        self,
        subject: str,
        start: DateTime,
        isCompleted: bool,
        id: Optional[int]= None
        ):
        self.id = id
        self.subject = subject
        self.start = start
        self.isCompleted = isCompleted
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "subject": self.subject,
            "start": self.start,
            "isCompleted": self.isCompleted
        }

class AutomationLed:
    def __init__(
        self,
        end: str,
        start: DateTime,
        createdAt: datetime,
        id: Optional[int]= None
        ):
        self.id = id
        self.end = end
        self.start = start
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "end": self.end,
            "start": self.start,
            "createdAt": self.createdAt
        }

class AutomationRoofFan:
    def __init__(
        self,
        term: int,
        createdAt: datetime,
        id: Optional[int]= None
        ):
        self.id = id
        self.term = term
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "term": self.term,
            "createdAt": self.createdAt
        }

class AutomationFan:
    def __init__(
        self,
        term: int,
        createdAt: datetime,
        id: Optional[int]= None
        ):
        self.id = id
        self.term = term
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "term": self.term,
            "createdAt": self.createdAt
        }

class AutomationAC:
    def __init__(
        self,
        end: str,
        start: DateTime,
        createdAt: datetime,
        id: Optional[int]= None
        ):
        self.id = id
        self.end = end
        self.start = start
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "end": self.end,
            "start": self.start,
            "createdAt": self.createdAt
        }