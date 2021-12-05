from typing import  Optional
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
    section_id: int
    purpose: str
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Sensor(BaseModel):
    id: int
    name: str
    section_id: int
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Humidity(BaseModel):
    id: int
    section_id: int
    sensor_id: int
    value: float
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Temperature(BaseModel):
    id: int
    section_id: int
    sensor_id: int
    value: float
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Switch(BaseModel):
    id: int
    section_id: int
    machine_id: int
    status: int
    controlledBy_id: int
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class WaterSupply(BaseModel):
    id: int
    section_id: int
    quantity: float
    createdAt: datetime
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class WaterCycle(BaseModel):
    id: int
    section_id: int
    period: int
    createdAt: datetime
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class WaterSpray(BaseModel):
    id: int
    section_id: int
    operating_time: int
    period: int
    createdAt: datetime
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class NutrientSupply(BaseModel):
    id: int
    section_id: int
    quantity: float
    createdAt: datetime
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Report(BaseModel):
    id: int
    section_id: int
    level: str
    subject: str
    solution: str
    isFixed: bool
    createdAt: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
