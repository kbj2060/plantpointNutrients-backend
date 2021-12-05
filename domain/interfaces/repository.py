from abc import ABCMeta, abstractmethod
from typing import List

from domain.entities.machine import Machine as eMachine
from domain.entities.sensor import Sensor as eSensor


class Repository(metaclass=ABCMeta):
    @abstractmethod
    def get_machines(self, filters: dict = None) -> List[eMachine]:
        pass

    @abstractmethod
    def get_sensors(self, filters: dict = None) -> List[eSensor]:
        pass