from typing import List
from domain.entities.nutrientsupply import NutrientSupply as eNutrientSupply
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class NutrientSupplyRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.NutrientSupply
        self.entity = eNutrientSupply
    # def read(self, filters:dict = None) -> List[eNutrientSupply]:
    #     DBSession = sessionmaker(bind=self.engine)
    #     session = DBSession()
    #     query = session.query(models.NutrientSupply)
        
    #     if filters is None:
    #         result_models = query.all()
    #     elif "limit" in filters:
    #         result_models = query.order_by(models.NutrientSupply.id.desc()).limit(filters.limit)
        
    #     return self._model2entity(models=result_models, entity=eNutrientSupply)

    def create(self):
        new_nutrientsupply = models.NutrientSupply(section_id=1, quantity=12)
        self.session.add(new_nutrientsupply)
        self.session.commit()

nutrientSupplyRepository = NutrientSupplyRepository(connection_data)
