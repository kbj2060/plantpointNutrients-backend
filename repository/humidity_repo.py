from repository.repo import BaseRepo
from domain.entities.humidity import Humidity as eHumidity
from repository import models
from controllers.app import session


class HumidityRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.entity = eHumidity
        self.model = models.Humidity

    def create(self, value) -> None:
        new_humidity: models.Humidity =self.model(value=int(value))
        session.add(new_humidity)
        session.commit()

humidityRepository = HumidityRepository()
