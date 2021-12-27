from domain.entities.nutrientsupply import NutrientSupply as eNutrientSupply
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class NutrientSupplyRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.NutrientSupply
        self.entity = eNutrientSupply

    def create(self, qauntity):
        new_nutrientsupply: models.NutrientSupply = models.NutrientSupply(quantity=qauntity)
        self.session.add(new_nutrientsupply)
        self.session.commit()

nutrientSupplyRepository = NutrientSupplyRepository(connection_data)
