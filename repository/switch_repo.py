from typing import List
from domain.entities.switch import Switch as eSwitch
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from utils.remove_sa_state import remove_sa_state


class SwitchRepository(BaseRepo):
    def _create_switch_models(self, results: List[models.Switch]) -> List[eSwitch]:
        return [ eSwitch(**remove_sa_state(vars(q))) for q in results ]

    def read_switch(self) -> eSwitch:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        last_switch = session.query(models.Switch).order_by(models.Switch.id.desc()).first()
        return eSwitch(**remove_sa_state(vars(last_switch))) if last_switch != None else None

    def read_switch_history(self, num: int) -> List[eSwitch]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        switch_history = session.query(models.Switch).order_by(models.Switch.id.desc()).limit(num)
        return self._create_switch_models(switch_history) if switch_history != None else None

    def create_switch(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_switch = models.Switch(section_id=1, machine_id=1, status=0, controlledBy_id=1)
        session.add(new_switch)
        session.commit()


switchRepository = SwitchRepository(connection_data)
