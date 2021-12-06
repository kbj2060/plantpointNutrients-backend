from datetime import datetime
from typing import Iterable, List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repository import schemas
from domain.entities.machine import Machine as eMachine
from domain.entities.sensor import Sensor as eSensor

from domain.interfaces.repository import Repository
from repository import models
from utils.remove_sa_state import remove_sa_state


class BaseRepo(Repository):
    def __init__(self, connection_data: dict) -> None:
        connection_string = "mysql+pymysql://{}:{}@{}/{}".format(
            connection_data["user"], connection_data["password"], connection_data["host"], connection_data["dbname"]
        )
        self.engine = create_engine(connection_string, echo=True)
        models.Base.metadata.bind = self.engine

    def _model2entity(self, models, entity):
        if models is None: return None
        elif not isinstance(models, list): return entity(**remove_sa_state(vars(models)))
        return [ entity(**remove_sa_state(vars(q))) for q in models ]
        
    def get_machines(self, filters: dict = None) -> List[eMachine]:
        pass

    def get_sensors(self, filters: dict = None) -> List[eSensor]:
        pass
