from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int
    name: str
    password: str
    type: str
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

class WaterSpray(BaseModel):
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
    level: str
    machine_id: int
    sensor_id: int
    isFixed: bool
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


