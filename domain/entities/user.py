from typing import  Optional, Dict
from sqlalchemy.sql.sqltypes import DateTime

class User:
    def __init__(
        self,
        email: str,
        name: str,
        password: str,
        id: Optional[int] = None,
        createdAt: Optional[DateTime]= None
        ):
        self.id = id
        self.email = email
        self.name = name
        self.password = password
        self.createdAt = createdAt
    
    @classmethod
    def from_dict(cls, adict: Dict) -> object:
        return cls(**adict)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "password": self.password,
            "createdAt": self.createdAt
        }
