from repository.repo import BaseRepo
from domain.entities.humidity import Humidity as eHumidity
from repository import models
from utils.get_db import get_db


class HumidityRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eHumidity
        self.model = models.Humidity

    def create(self, value, db=next(get_db())) -> None:
        new_humidity: models.Humidity =self.model(value=int(value))
        db.add(new_humidity)
        db.commit()

humidityRepository = HumidityRepository()
