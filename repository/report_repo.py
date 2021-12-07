from typing import List
from domain.entities.report import Report as eReport
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class ReportRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Report
        self.entity = eReport
    # def read(self, filters:dict = None) -> List[eReport]:
    #     DBSession = sessionmaker(bind=self.engine)
    #     session = DBSession()
    #     query = session.query(models.Report)
        
    #     if filters is None:
    #         result_models = query.all()
    #     elif "limit" in filters:
    #         result_models = query.order_by(models.Report.id.desc()).limit(filters.limit)
        
    #     return self._model2entity(models=result_models, entity=eReport)

    def create_report(self):
        new_report = models.Report(section_id=1, machine_id=3, sensor_id=None, level=3, solution="dd", isFixed=False)
        self.session.add(new_report)
        self.session.commit()

reportRepository = ReportRepository(connection_data)
