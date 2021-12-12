from sqlalchemy.sql.expression import and_
from config import connection_data
from repository.repo import BaseRepo
from domain.entities.humidity import Humidity as eHumidity
from repository import models

class HumidityRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.entity = eHumidity
        self.model = models.Humidity

    def create(self, m_section, s_section, value) -> None:
        section = self.session.query(
            models.Section.id
        ).filter(
            and_(models.Section.main == str(m_section), models.Section.sub == str(s_section))
        ).first()
        new_humidity =self.model(section_id=section.id, value=int(value))
        self.session.add(new_humidity)
        self.session.commit()

humidityRepository = HumidityRepository(connection_data)
