from typing import  Optional, Dict
from domain.entities.temperature import Temperature

class Humidity(Temperature):
    def __init__(self, section_id: int, sensor_id: int, value: float, id: Optional[int] = None, createdAt: Optional[str]= None):
        self.id = id
        self.section_id = section_id
        self.sensor_id = sensor_id
        self.value = value
        self.createdAt = createdAt

