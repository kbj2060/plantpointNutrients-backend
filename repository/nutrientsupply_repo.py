from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from domain.entities.nutrientsupply import NutrientSupply as eNutrientSupply
from repository.repo import BaseRepo
from repository import models
from utils.get_db import get_db 


class NutrientSupplyRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.NutrientSupply
        self.entity = eNutrientSupply

    def create(self, qauntity, db=next(get_db())):
        new_nutrientsupply: models.NutrientSupply = models.NutrientSupply(quantity=qauntity)
        db.add(new_nutrientsupply)
        db.commit()

nutrientSupplyRepository = NutrientSupplyRepository()
