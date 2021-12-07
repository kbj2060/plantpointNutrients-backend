from typing import List
from domain.entities.waterspray import WaterSpray as eWaterSpray
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class WaterSprayRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.WaterSpray
        self.entity = eWaterSpray

    # def read_waterspray(self, filters:dict = None) -> List[eWaterSpray]:
    #     DBSession = sessionmaker(bind=self.engine)
    #     session = DBSession()
    #     query = session.query(models.WaterSpray)
        
    #     if filters is None:
    #         result_models = query.all()
    #     elif "limit" in filters:
    #         result_models = query.order_by(models.WaterSpray.id.desc()).limit(filters.limit)
        
    #     return self._model2entity(models=result_models, entity=eWaterSpray)

    def create(self):
        new_waterspray = models.WaterSpray(section_id=1, period=12, operating_time=12)
        self.session.add(new_waterspray)
        self.session.commit()

waterSprayRepository = WaterSprayRepository(connection_data)
