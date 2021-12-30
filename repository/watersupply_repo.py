from domain.entities.watersupply import WaterSupply as eWaterSupply
from repository.repo import BaseRepo
from repository import models
from controllers.app import session


class WaterSupplyRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.WaterSupply
        self.entity = eWaterSupply

    def create(self, quantity):
        new_watersupply: models.WaterSupply = models.WaterSupply(quantity=quantity)
        session.add(new_watersupply)
        session.commit()

waterSupplyRepository = WaterSupplyRepository()
