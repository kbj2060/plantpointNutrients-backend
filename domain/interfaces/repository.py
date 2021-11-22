from abc import ABCMeta, abstractmethod
from typing import List

from domain.entities import machine,sensor


class Repository(metaclass=ABCMeta):
    @abstractmethod
    def get_machines(self, filters: dict = None) -> List[machine.Machine]:
        pass

    @abstractmethod
    def get_sensors(self, filters: dict = None) -> List[sensor.Sensor]:
        pass