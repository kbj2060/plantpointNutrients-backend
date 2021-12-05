from typing import List
from domain.entities.temperature import Temperature as eTemperature
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class TemperatureRepository(BaseRepo):
    def _create_temperature_entity(self, results: List[models.Temperature]) -> List[eTemperature]:
        return [ q.__dict__ for q in results ]

    def read_temperature(self) -> List[eTemperature]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Temperature)
        return self._create_temperature_entity(query.all())

    def create_temperature(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_temperautre = models.Temperature(section_id=1, sensor_id=1, value=21)
        session.add(new_temperautre)
        session.commit()

temperatureRepository = TemperatureRepository(connection_data)
