from typing import List
from domain.entities.machine import Machine as eMachine
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from utils.remove_sa_state import remove_sa_state


class MachineRepository(BaseRepo):
    def read_machines(self, filters: dict = None) -> List[eMachine]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Machine)

        if filters is None:
            return self._model2entity(models=query.all(), entity=eMachine)
        if "section__eq" in filters:
            result_models = query.filter(models.Machine.section == filters["section__eq"]).all()
        if "name__eq" in filters:
            result_models = query.filter(models.Machine.name == filters["name__eq"]).all()
        if "purpose__eq" in filters:
            result_models = query.filter(models.Machine.purpose < filters["purpose__eq"]).all()

        return self._model2entity(models=result_models, entity=eMachine)

    def create_machine(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        # DB 에 넣을 때 models 객체를 이용해 넣어야 한다!
        new_machine = models.Machine(section_id=1, purpose='temp', name='temp')
        session.add(new_machine)
        session.commit()

machineRepository = MachineRepository(connection_data)
