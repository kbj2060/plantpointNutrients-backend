from datetime import date
from typing import List

from sqlalchemy import Date, cast
from domain.entities.temperature import Temperature as eTemperature
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from domain.interfaces.RequestFilters import RequestFilters
from sqlalchemy import and_


class TemperatureRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Temperature
        self.entity = eTemperature

    def create(self, m_section, s_section, value) -> None:
        section = self.session.query(
            models.Section.id
        ).filter(
            and_(models.Section.main == str(m_section), models.Section.sub == str(s_section))
        ).first()
        new_temperautre = self.model(section_id=section.id, value=int(value))
        self.session.add(new_temperautre)
        self.session.commit()

temperatureRepository = TemperatureRepository(connection_data)
