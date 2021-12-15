from domain.entities.watersupply import WaterSupply as eWaterSupply
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class WaterSupplyRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.WaterSupply
        self.entity = eWaterSupply

    def create(self, quantity):
        new_watersupply = models.WaterSupply(quantity=quantity)
        self.session.add(new_watersupply)
        self.session.commit()

waterSupplyRepository = WaterSupplyRepository(connection_data)
