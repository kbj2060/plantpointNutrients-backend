from typing import List

from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Date, cast
from config import connection_data
from repository.repo import BaseRepo
from domain.entities.humidity import Humidity as eHumidity
from repository import models
from utils.remove_sa_state import remove_sa_state
from datetime import date


class HumidityRepository(BaseRepo):
    def _create_humidity_entity(self, results: List[models.Humidity]) -> List[eHumidity]:
        return [ eHumidity(**remove_sa_state(vars(q))) for q in results ]

    def read_humidity(self) -> List[eHumidity]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        last_humidity = session.query(models.Humidity).order_by(models.Humidity.id.desc()).first()
        return eHumidity(**remove_sa_state(vars(last_humidity)))

    def read_today_humidity(self) -> List[eHumidity]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Humidity).filter(cast(models.Humidity.createdAt, Date) == date.today())
        return self._create_humidity_entity(query.all())

    def create_humidity(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_humidity = models.Humidity(section_id=1, sensor_id=1, value=21)
        session.add(new_humidity)
        session.commit()

humidityRepository = HumidityRepository(connection_data)
