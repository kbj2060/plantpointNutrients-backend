from typing import List
from domain.entities.sensor import Sensor as eSensor
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class SensorRepository(BaseRepo):
    def _create_sensor_models(self, results: List[models.Sensor]) -> List[eSensor]:
        return [ eSensor(
            name=q.name, section=q.section, createdAt=q.createdAt
        ) for q in results ]

    def get_sensors(self, filters: dict = None) -> List[eSensor]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Sensor)

        if filters is None:
            return self._create_sensor_models(query.all())
        if "section__eq" in filters:
            query = query.filter(models.Sensor.section == filters["section__eq"])
        if "name__eq" in filters:
            query = query.filter(models.Sensor.name == filters["name__eq"])

        return self._create_sensor_models(query.all())

sensorRepository = SensorRepository(connection_data)
