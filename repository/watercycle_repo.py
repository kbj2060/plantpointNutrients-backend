from domain.entities.watercycle import WaterCycle as eWaterCycle
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class WaterCycleRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.WaterCycle
        self.entity = eWaterCycle

    # def read(self, filters:dict = None) -> List[eWaterCycle]:
    #     DBSession = sessionmaker(bind=self.engine)
    #     session = DBSession()
    #     query = session.query(models.WaterCycle)
        
    #     if filters is None:
    #         result_models = query.all()
    #     elif "limit" in filters:
    #         result_models = query.order_by(models.WaterCycle.id.desc()).limit(filters.limit)
        
    #     return self._model2entity(models=result_models, entity=eWaterCycle)

    def create(self):
        new_watercycle = models.WaterCycle(section_id=1, period=12)
        self.session.add(new_watercycle)
        self.session.commit()

waterCycleRepository = WaterCycleRepository(connection_data)
