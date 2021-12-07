from datetime import date
from typing import List

from sqlalchemy import Date, cast
from domain.entities.temperature import Temperature as eTemperature
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from repository.schemas import RequestFilters


class TemperatureRepository(BaseRepo):
    def read_temperature(self, filters: RequestFilters) -> eTemperature:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        if filters.today:
            result_models = session.query(models.Temperature).filter(cast(models.Temperature.createdAt, Date) == date.today()).all()
        elif filters.limit > 0:
            result_models = session.query(models.Temperature).order_by(models.Temperature.id.desc()).limit(filters.limit).all()
        else:
            result_models = session.query(models.Temperature).all()

        return self._model2entity(models=result_models, entity=eTemperature)

    def create_temperature(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_temperautre = models.Temperature(section_id=1, sensor_id=1, value=21)
        session.add(new_temperautre)
        session.commit()

temperatureRepository = TemperatureRepository(connection_data)
