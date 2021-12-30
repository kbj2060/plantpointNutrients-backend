from typing import List
from domain.entities.machine import Machine as eMachine
from repository.repo import BaseRepo
from repository import models
from controllers.app import session



class MachineRepository(BaseRepo):
    def read_machines(self) -> List[eMachine]:
        query = session.query(models.Machine)
        return self._model2entity(models=query.all(), entity=eMachine)

    def create_machine(self) -> None:
        new_machine: models.Machine = models.Machine(name='temp', pin=2)
        session.add(new_machine)
        session.commit()

machineRepository = MachineRepository()
