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
    def read_temperature(self, filters: dict = None) -> eTemperature:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        if filters is None:
            result_models = session.query(models.Temperature).all()
        elif "limit" in filters:
            result_models = session.query(models.Temperature).order_by(models.Temperature.id.desc()).limit(filters.limit)
        elif "today" in filters:
            result_models = session.query(models.Temperature).filter(cast(models.Temperature.createdAt, Date) == date.today()).all()

        return self._model2entity(models=result_models, entity=eTemperature)

    def create_temperature(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_temperautre = models.Temperature(section_id=1, sensor_id=1, value=21)
        session.add(new_temperautre)
        session.commit()

temperatureRepository = TemperatureRepository(connection_data)
