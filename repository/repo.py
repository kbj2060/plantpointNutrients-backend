from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.entities import machine, sensor
from domain.interfaces.repository import Repository
from repository import db_objects
from config import connection_data


class BaseRepo(Repository):
    def __init__(self, connection_data: dict) -> None:
        connection_string = "mysql+pymysql://{}:{}@{}/{}".format(
            connection_data["user"], connection_data["password"], connection_data["host"], connection_data["dbname"]
        )
        self.engine = create_engine(connection_string)
        db_objects.Base.metadata.bind = self.engine

    def get_machines(self, filters: dict = None) -> List[machine.Machine]:
        pass

    def get_sensors(self, filters: dict = None) -> List[sensor.Sensor]:
        pass


class MachineRepository(BaseRepo):
    def _create_machine_db_objects(self, results: List[db_objects.Machine]) -> List[machine.Machine]:
        return [ machine.Machine(
            name=q.name, section=q.section, purpose=q.purpose, created=q.created
        ) for q in results ]

    def get_machines(self, filters: dict = None) -> List[machine.Machine]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(db_objects.Machine)

        if filters is None:
            return self._create_machine_db_objects(query.all())
        if "section__eq" in filters:
            query = query.filter(db_objects.Machine.section == filters["section__eq"])
        if "name__eq" in filters:
            query = query.filter(db_objects.Machine.name == filters["name__eq"])
        if "purpose__eq" in filters:
            query = query.filter(db_objects.Machine.purpose < filters["purpose__eq"])

        return self._create_machine_db_objects(query.all())


class SensorRepository(BaseRepo):
    def _create_sensor_db_objects(self, results: List[db_objects.Sensor]) -> List[sensor.Sensor]:
        return [ sensor.Sensor(
            name=q.name, section=q.section, created=q.created
        ) for q in results ]

    def get_sensors(self, filters: dict = None) -> List[sensor.Sensor]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(db_objects.Sensor)

        if filters is None:
            return self._create_sensor_db_objects(query.all())
        if "section__eq" in filters:
            query = query.filter(db_objects.Sensor.section == filters["section__eq"])
        if "name__eq" in filters:
            query = query.filter(db_objects.Sensor.name == filters["name__eq"])

        return self._create_sensor_db_objects(query.all())


mRepo = MachineRepository(connection_data)
sRepo = SensorRepository(connection_data)