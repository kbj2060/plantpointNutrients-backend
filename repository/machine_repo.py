from typing import List
from domain.entities.machine import Machine as eMachine
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data


class MachineRepository(BaseRepo):
    def _create_machine_models(self, results: List[models.Machine]) -> List[eMachine]:
        return [ eMachine(
            name=q.name, section=q.section, purpose=q.purpose, createdAt=q.createdAt
        ) for q in results ]

    def read_machines(self, filters: dict = None) -> List[eMachine]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Machine)

        if filters is None:
            return self._create_machine_models(query.all())
        if "section__eq" in filters:
            query = query.filter(models.Machine.section == filters["section__eq"])
        if "name__eq" in filters:
            query = query.filter(models.Machine.name == filters["name__eq"])
        if "purpose__eq" in filters:
            query = query.filter(models.Machine.purpose < filters["purpose__eq"])

        return self._create_machine_models(query.all())

    def create_machine(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        # DB 에 넣을 때 models 객체를 이용해 넣어야 한다!
        new_machine = models.Machine(section_id=1, purpose='temp', name='temp')
        session.add(new_machine)
        session.commit()

machineRepository = MachineRepository(connection_data)
