from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel):
    Authorization: str = None

class AutomationHistory(BaseModel):
    id: int
    subject: str
    start: datetime
    end: datetime
    success: bool

class User(BaseModel):
    id: int
    email: str
    name: str
    password: str
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Section(BaseModel):
    id: int
    main: str
    sub: str
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Machine(BaseModel):
    id: int
    name: str
    pin: int
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Humidity(BaseModel):
    id: int
    value: float
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Temperature(BaseModel):
    id: int
    value: float
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Switch(BaseModel):
    id: int
    machine_id: int
    status: int
    controlledBy_id: int
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class WaterSupply(BaseModel):
    id: int
    quantity: float
    createdAt: datetime
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class WaterCycle(BaseModel):
    id: int
    period: int
    createdAt: datetime
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class SprayTerm(BaseModel):
    id: int
    period: int
    createdAt: datetime
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class NutrientSupply(BaseModel):
    id: int
    quantity: float
    createdAt: datetime
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Report(BaseModel):
    id: int
    level: int
    problem: str
    isFixed: bool
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


