from domain.entities.spraytime import SprayTime as eSprayTime
from repository.repo import BaseRepo
from repository import models
from controllers.app import session


class SprayTimeRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.SprayTime
        self.entity = eSprayTime

    def create(self, period):
        new_spraytime: models.SprayTime = models.SprayTime(period=period)
        session.add(new_spraytime)
        session.commit()

sprayTimeRepository = SprayTimeRepository()
