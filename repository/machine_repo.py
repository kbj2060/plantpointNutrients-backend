from typing import List
from domain.entities.machine import Machine as eMachine
from repository.repo import BaseRepo
from repository import models
from controllers.app import database
from utils.get_db import get_db



class MachineRepository(BaseRepo):
    def read_machines(self, db=next(get_db())) -> List[eMachine]:
        query = db.query(models.Machine)
        return self._model2entity(models=query.all(), entity=eMachine)

    def create_machine(self, db=next(get_db())) -> None:
        new_machine: models.Machine = models.Machine(name='temp', pin=2)
        db.add(new_machine)
        db.commit()

machineRepository = MachineRepository()
