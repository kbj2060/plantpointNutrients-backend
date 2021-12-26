from domain.entities.report import Report as eReport
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class ReportRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Report
        self.entity = eReport
        
    def create(self, level: int, problem: str):
        new_report = models.Report(problem=problem, level=level)
        self.session.add(new_report)
        self.session.commit()

reportRepository = ReportRepository(connection_data)
