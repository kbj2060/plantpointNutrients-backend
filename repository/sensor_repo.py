from typing import List
from domain.entities.sensor import Sensor as eSensor
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class SensorRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Sensor
        self.entity = eSensor

    def read(self) -> List[eSensor]:
        query = self.session.query(models.Sensor)
        return self._model2entity(models=query.all(), entity=eSensor)

    def create(self) -> None:
        new_sensor: models.Sensor = models.Sensor(name='temp')
        self.session.add(new_sensor)
        self.session.commit()

sensorRepository = SensorRepository(connection_data)
