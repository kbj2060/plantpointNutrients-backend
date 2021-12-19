from typing import List, Optional
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
        
    def create(
        self,
        level: int,
        sensor_id: Optional[int],
        machine_id: Optional[int]
    ):
        new_report = models.Report(machine_id=machine_id, sensor_id=sensor_id, level=level)
        self.session.add(new_report)
        self.session.commit()

reportRepository = ReportRepository(connection_data)
