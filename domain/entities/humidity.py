from typing import  Optional, Dict
from domain.entities.temperature import Temperature

class Humidity(Temperature):
    def __init__(self, section_id: int,  sensor_id: int, value: float, id: Optional[int]= None, createdAt: Optional[str]= None):
        super().__init__()

