from config import connection_data
from repository.repo import BaseRepo
from domain.entities.humidity import Humidity as eHumidity
from repository import models

class HumidityRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.entity = eHumidity
        self.model = models.Humidity

    def create(self) -> None:
        new_humidity = models.Humidity(section_id=1, sensor_id=1, value=21)
        self.session.add(new_humidity)
        self.session.commit()

humidityRepository = HumidityRepository(connection_data)
