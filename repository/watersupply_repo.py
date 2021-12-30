from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from domain.entities.watersupply import WaterSupply as eWaterSupply
from repository.repo import BaseRepo
from repository import models
from utils.get_db import get_db


class WaterSupplyRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.WaterSupply
        self.entity = eWaterSupply

    def create(self, quantity, db=next(get_db())):
        new_watersupply: models.WaterSupply = models.WaterSupply(quantity=quantity)
        db.add(new_watersupply)
        db.commit()

waterSupplyRepository = WaterSupplyRepository()
