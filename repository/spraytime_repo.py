from domain.entities.spraytime import SprayTime as eSprayTime
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class SprayTimeRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.SprayTime
        self.entity = eSprayTime

    def create(self, period):
        new_spraytime: models.SprayTime = models.SprayTime(period=period)
        self.session.add(new_spraytime)
        self.session.commit()

sprayTimeRepository = SprayTimeRepository(connection_data)
