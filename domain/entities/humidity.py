from typing import  Optional, Dict
from domain.entities.temperature import Temperature

class Humidity(Temperature):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

