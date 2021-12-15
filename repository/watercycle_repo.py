from domain.entities.watercycle import WaterCycle as eWaterCycle
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class WaterCycleRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.WaterCycle
        self.entity = eWaterCycle

    def create(self, period):
        new_watercycle = models.WaterCycle(period=period)
        self.session.add(new_watercycle)
        self.session.commit()

waterCycleRepository = WaterCycleRepository(connection_data)
