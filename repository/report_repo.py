from typing import List
from domain.entities.report import Report as eReport
from domain.interfaces.RequestFilters import RequestFilters
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class ReportRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Report
        self.entity = eReport

    def read(self, filters: RequestFilters):
        if filters is None: return None
        query = self.session.query(self.model)
        if query is not None: return self._model2entity(models=query.all(), entity=self.entity)
        else: print('Error report is written.')
        
    def create_report(self):
        new_report = models.Report(section_id=1, machine_id=3, sensor_id=None, level=3, solution="dd", isFixed=False)
        self.session.add(new_report)
        self.session.commit()

reportRepository = ReportRepository(connection_data)
