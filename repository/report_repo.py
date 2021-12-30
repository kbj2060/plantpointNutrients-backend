from domain.entities.report import Report as eReport
from repository.repo import BaseRepo
from repository import models
from utils.get_db import get_db


class ReportRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Report
        self.entity = eReport
        
    def create(self, level: int, problem: str, db=next(get_db())):
        new_report: models.Report = models.Report(problem=problem, level=level)
        db.add(new_report)
        db.commit()

reportRepository = ReportRepository()
