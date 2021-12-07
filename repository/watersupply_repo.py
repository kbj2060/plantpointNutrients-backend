from domain.entities.watersupply import WaterSupply as eWaterSupply
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class WaterSupplyRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.WaterSupply
        self.entity = eWaterSupply

    # def read_watersupply(self, filters:dict = None) -> List[eWaterSupply]:
    #     DBSession = sessionmaker(bind=self.engine)
    #     session = DBSession()
    #     query = session.query(models.WaterSupply)
        
    #     if filters is None:
    #         result_models = query.all()
    #     elif "limit" in filters:
    #         result_models = query.order_by(models.WaterSupply.id.desc()).limit(filters.limit)
        
    #     return self._model2entity(models=result_models, entity=eWaterSupply)

    def create(self):
        new_watersupply = models.WaterSupply(section_id=1, quantity=12)
        self.session.add(new_watersupply)
        self.session.commit()

waterSupplyRepository = WaterSupplyRepository(connection_data)
