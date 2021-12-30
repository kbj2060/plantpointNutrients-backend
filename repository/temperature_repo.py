from fastapi.params import Depends

from sqlalchemy.orm.session import Session
from domain.entities.temperature import Temperature as eTemperature
from repository.repo import BaseRepo
from repository import models

from utils.get_db import get_db


class TemperatureRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Temperature
        self.entity = eTemperature

    def create(self, value, db=next(get_db())) -> None:
        new_temperautre: models.Temperature = self.model(value=int(value))
        db.add(new_temperautre)
        db.commit()

temperatureRepository = TemperatureRepository()
