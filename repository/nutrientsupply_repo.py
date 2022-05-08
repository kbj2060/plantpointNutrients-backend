from domain.entities.nutrientsupply import NutrientSupply as eNutrientSupply
from repository.repo import BaseRepo
from repository import models
from controllers.app import session

class NutrientSupplyRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.NutrientSupply
        self.entity = eNutrientSupply

    def create(self, qauntity):
        new_nutrientsupply: models.NutrientSupply = models.NutrientSupply(quantity=qauntity)
        session.add(new_nutrientsupply)
        session.commit()

nutrientSupplyRepository = NutrientSupplyRepository()
