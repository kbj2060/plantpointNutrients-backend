from typing import List
from domain.entities.sensor import Sensor as eSensor
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from utils.remove_sa_state import remove_sa_state


class SensorRepository(BaseRepo):
    def read_sensors(self, filters: dict = None) -> List[eSensor]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Sensor)

        if filters is None:
            return self._model2entity(models=query.all(), entity=eSensor)
        if "section__eq" in filters:
            result_models = query.filter(models.Sensor.section == filters["section__eq"]).all()
        if "name__eq" in filters:
            result_models = query.filter(models.Sensor.name == filters["name__eq"]).all()

        return self._model2entity(models=result_models, entity=eSensor)

    def create_sensor(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        # DB 에 넣을 때 models 객체를 이용해 넣어야 한다!
        new_sensor = models.Sensor(section_id=1, name='temp')
        session.add(new_sensor)
        session.commit()

sensorRepository = SensorRepository(connection_data)
