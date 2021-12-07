from typing import List
from domain.entities.section import Section as eSection
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class SectionRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Section
        self.entity = eSection

    def read(self) -> List[eSection]:
        query = self.session.query(models.Section)
        return self._model2entity(models=query.all(), entity=self.entity)


sectionRepository = SectionRepository(connection_data)
