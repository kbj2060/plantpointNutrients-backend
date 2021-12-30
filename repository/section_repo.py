from typing import List
from domain.entities.section import Section as eSection
from repository.repo import BaseRepo
from repository import models

from controllers.app import session


class SectionRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Section
        self.entity = eSection

    def read(self) -> List[eSection]:
        query = session.query(models.Section)
        return self._model2entity(models=query.all(), entity=self.entity)


sectionRepository = SectionRepository()
