from datetime import date
from typing import List

from sqlalchemy import Date, cast
from domain.entities.temperature import Temperature as eTemperature
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from domain.interfaces.RequestFilters import RequestFilters


class TemperatureRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Temperature
        self.entity = eTemperature

    def create(self) -> None:
        new_temperautre = models.Temperature(section_id=1, sensor_id=1, value=21)
        self.session.add(new_temperautre)
        self.session.commit()

temperatureRepository = TemperatureRepository(connection_data)
