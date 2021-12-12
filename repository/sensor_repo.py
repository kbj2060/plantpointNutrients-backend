# from typing import List
# from domain.entities.sensor import Sensor as eSensor
# from repository.repo import BaseRepo
# from repository import models
# from sqlalchemy.orm import sessionmaker
# from config import connection_data
# from utils.remove_sa_state import remove_sa_state


# class SensorRepository(BaseRepo):
#     def __init__(self, connection_data: dict) -> None:
#         super().__init__(connection_data)
#         self.model = models.Sensor
#         self.entity = eSensor

#     def read(self, filters: dict = None) -> List[eSensor]:
#         query = self.session.query(models.Sensor)

#         if filters is None:
#             return self._model2entity(models=query.all(), entity=eSensor)
#         if "section__eq" in filters:
#             result_models = query.filter(models.Sensor.section == filters["section__eq"]).all()
#         if "name__eq" in filters:
#             result_models = query.filter(models.Sensor.name == filters["name__eq"]).all()

#         return self._model2entity(models=result_models, entity=eSensor)

#     def create(self) -> None:
#         new_sensor = models.Sensor(section_id=1, name='temp')
#         self.session.add(new_sensor)
#         self.session.commit()

# sensorRepository = SensorRepository(connection_data)
