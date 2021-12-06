from typing import List
from domain.entities.section import Section as eSection
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class SectionRepository(BaseRepo):
    def read_sections(self) -> List[eSection]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Section)
        return self._model2entity(models=query.all(), entity=eSection)


sectionRepository = SectionRepository(connection_data)
