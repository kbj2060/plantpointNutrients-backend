from typing import List
from domain.entities.waterspray import WaterSpray as eWaterSpray
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class WaterSprayRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.WaterSpray
        self.entity = eWaterSpray

    def create(self, period):
        new_waterspray = models.WaterSpray(period=period)
        self.session.add(new_waterspray)
        self.session.commit()

waterSprayRepository = WaterSprayRepository(connection_data)
