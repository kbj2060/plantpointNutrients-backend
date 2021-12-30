from typing import List
from fastapi.params import Depends

from sqlalchemy.orm.session import Session
from domain.entities.section import Section as eSection
from repository.repo import BaseRepo
from repository import models

from utils.get_db import get_db


class SectionRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Section
        self.entity = eSection

    def read(self, db=next(get_db())) -> List[eSection]:
        query = db.query(models.Section)
        return self._model2entity(models=query.all(), entity=self.entity)


sectionRepository = SectionRepository()
