from typing import List
from domain.entities.sensor import Sensor as eSensor
from repository.repo import BaseRepo
from repository import models
from controllers.app import session


class SensorRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Sensor
        self.entity = eSensor

    def read(self) -> List[eSensor]:
        query = session.query(models.Sensor)
        return self._model2entity(models=query.all(), entity=eSensor)

    def create(self) -> None:
        new_sensor: models.Sensor = models.Sensor(name='temp')
        session.add(new_sensor)
        session.commit()

sensorRepository = SensorRepository()
