from domain.entities.report import Report as eReport
from repository.repo import BaseRepo
from repository import models
from controllers.app import session


class ReportRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Report
        self.entity = eReport
        
    def create(self, level: int, problem: str):
        new_report: models.Report = models.Report(problem=problem, level=level)
        session.add(new_report)
        session.commit()

reportRepository = ReportRepository()
