from typing import List, Union
from domain.entities.switch import Switch as eSwitch
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from utils.remove_sa_state import remove_sa_state


class SwitchRepository(BaseRepo):
    def read_switches(self, filters: dict = None) -> eSwitch:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        if filters is None:
            result_models = session.query(models.Switch).all()
        elif "limit" in filters:
            result_models = session.query(models.Switch).order_by(models.Switch.id.desc()).limit(filters.limit)
            
        return self._model2entity(models=result_models, entity=eSwitch)

    def create_switch(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_switch = models.Switch(section_id=1, machine_id=1, status=0, controlledBy_id=1)
        session.add(new_switch)
        session.commit()


switchRepository = SwitchRepository(connection_data)
