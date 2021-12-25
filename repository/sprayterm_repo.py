from typing import List
from domain.entities.sprayterm import SprayTerm as eSprayTerm
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class SprayTermRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.SprayTerm
        self.entity = eSprayTerm

    def create(self, period):
        new_waterspray = models.SprayTerm(period=period)
        self.session.add(new_waterspray)
        self.session.commit()

sprayTermRepository = SprayTermRepository(connection_data)
