from datetime import date
from typing import List

from sqlalchemy import Date, cast
from domain.entities.temperature import Temperature as eTemperature
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from utils.remove_sa_state import remove_sa_state


class TemperatureRepository(BaseRepo):
    def _create_temperature_entity(self, results: List[models.Temperature]) -> List[eTemperature]:
        return [ eTemperature(**remove_sa_state(vars(q))) for q in results ]

    def read_temperature(self) -> eTemperature:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        last_temperature = session.query(models.Temperature).order_by(models.Temperature.id.desc()).first()
        return eTemperature(**remove_sa_state(vars(last_temperature)))

    def read_today_temperature(self) -> List[eTemperature]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Temperature).filter(cast(models.Temperature.createdAt, Date) == date.today())
        return self._create_temperature_entity(query.all())

    def create_temperature(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_temperautre = models.Temperature(section_id=1, sensor_id=1, value=21)
        session.add(new_temperautre)
        session.commit()

temperatureRepository = TemperatureRepository(connection_data)
