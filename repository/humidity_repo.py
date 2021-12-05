from typing import List

from sqlalchemy.orm.session import sessionmaker
from config import connection_data
from repository.repo import BaseRepo
from domain.entities.humidity import Humidity as eHumidity
from repository import models


class HumidityRepository(BaseRepo):
    def _create_humidity_entity(self, results: List[models.Humidity]) -> List[eHumidity]:
        return [ eHumidity(q) for q in results ]

    def read_humidity(self) -> List[eHumidity]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Humidity)
        return self._create_humidity_entity(query.all())

    def create_humidity(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_humidity = models.Humidity(section_id=1, sensor_id=1, value=21)
        session.add(new_humidity)
        session.commit()

humidityRepository = HumidityRepository(connection_data)
