from domain.entities.temperature import Temperature as eTemperature
from repository.repo import BaseRepo
from repository import models
from controllers.app import session


class TemperatureRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Temperature
        self.entity = eTemperature

    def create(self, value) -> None:
        new_temperautre: models.Temperature = self.model(value=int(value))
        session.add(new_temperautre)
        session.commit()

temperatureRepository = TemperatureRepository()
