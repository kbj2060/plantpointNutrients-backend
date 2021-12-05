from typing import List
from domain.entities.sensor import Sensor as eSensor
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from utils.remove_sa_state import remove_sa_state


class SensorRepository(BaseRepo):
    def _create_sensor_entity(self, results: List[models.Sensor]) -> List[eSensor]:
        return [ eSensor(**remove_sa_state(vars(q))) for q in results ]

    def read_sensors(self, filters: dict = None) -> List[eSensor]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Sensor)

        if filters is None:
            return self._create_sensor_entity(query.all())
        if "section__eq" in filters:
            query = query.filter(models.Sensor.section == filters["section__eq"])
        if "name__eq" in filters:
            query = query.filter(models.Sensor.name == filters["name__eq"])

        return self._create_sensor_entity(query.all())

    def create_sensor(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        # DB 에 넣을 때 models 객체를 이용해 넣어야 한다!
        new_sensor = models.Sensor(section_id=1, name='temp')
        session.add(new_sensor)
        session.commit()

sensorRepository = SensorRepository(connection_data)
