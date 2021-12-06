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
    def read_humidity(self, filters: dict = None) -> List[eHumidity]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        if filters is None:
            result_models = session.query(models.Humidity).all()
        elif "limit" in filters:
            result_models = session.query(models.Humidity).order_by(models.Humidity.id.desc()).limit(filters.limit)
        elif "today" in filters:
            result_models = session.query(models.Humidity).filter(cast(models.Humidity.createdAt, Date) == date.today()).all()

        return self._model2entity(models=result_models, entity=eHumidity)

    def create_humidity(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_humidity = models.Humidity(section_id=1, sensor_id=1, value=21)
        session.add(new_humidity)
        session.commit()

humidityRepository = HumidityRepository(connection_data)
