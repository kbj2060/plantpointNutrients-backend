from typing import List
from fastapi.params import Depends

from sqlalchemy.orm.session import Session
from domain.entities.sensor import Sensor as eSensor
from repository.repo import BaseRepo
from repository import models
from utils.get_db import get_db


class SensorRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Sensor
        self.entity = eSensor

    def read(self, db=next(get_db())) -> List[eSensor]:
        query = db.query(models.Sensor)
        return self._model2entity(models=query.all(), entity=eSensor)

    def create(self, db=next(get_db())) -> None:
        new_sensor: models.Sensor = models.Sensor(name='temp')
        db.add(new_sensor)
        db.commit()

sensorRepository = SensorRepository()
