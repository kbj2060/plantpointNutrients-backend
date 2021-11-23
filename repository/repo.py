from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repository import schemas
from domain.entities import machine, sensor
from domain.interfaces.repository import Repository
from repository import models
from config import connection_data


class BaseRepo(Repository):
    def __init__(self, connection_data: dict) -> None:
        connection_string = "mysql+pymysql://{}:{}@{}/{}".format(
            connection_data["user"], connection_data["password"], connection_data["host"], connection_data["dbname"]
        )
        self.engine = create_engine(connection_string, echo=True)
        models.Base.metadata.bind = self.engine

    def get_machines(self, filters: dict = None) -> List[machine.Machine]:
        pass

    def get_sensors(self, filters: dict = None) -> List[sensor.Sensor]:
        pass


class MachineRepository(BaseRepo):
    def _create_machine_models(self, results: List[models.Machine]) -> List[machine.Machine]:
        return [ machine.Machine(
            name=q.name, section=q.section, purpose=q.purpose, created=q.created
        ) for q in results ]

    def get_machines(self, filters: dict = None) -> List[machine.Machine]:
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

    def add_machine(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        # DB 에 넣을 때 models 객체를 이용해 넣어야 한다!
        new_machine = models.Machine(section='s1/d1', purpose='temp', name='temp')
        session.add(new_machine)
        session.commit()


class SensorRepository(BaseRepo):
    def _create_sensor_models(self, results: List[models.Sensor]) -> List[sensor.Sensor]:
        return [ sensor.Sensor(
            name=q.name, section=q.section, created=q.created
        ) for q in results ]

    def get_sensors(self, filters: dict = None) -> List[sensor.Sensor]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.Sensor)

        if filters is None:
            return self._create_sensor_models(query.all())
        if "section__eq" in filters:
            query = query.filter(models.Sensor.section == filters["section__eq"])
        if "name__eq" in filters:
            query = query.filter(models.Sensor.name == filters["name__eq"])

        return self._create_sensor_models(query.all())


mRepo = MachineRepository(connection_data)
sRepo = SensorRepository(connection_data)