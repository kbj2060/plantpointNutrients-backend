from domain.entities.switch import Switch as eSwitch
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class SwitchRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Switch
        self.entity = eSwitch

    # def read_switches(self, filters: dict = None) -> eSwitch:
    #     DBSession = sessionmaker(bind=self.engine)
    #     session = DBSession()

    #     if filters is None:
    #         result_models = session.query(models.Switch).all()
    #     elif "limit" in filters:
    #         result_models = session.query(models.Switch).order_by(models.Switch.id.desc()).limit(filters.limit)
            
    #     return self._model2entity(models=result_models, entity=eSwitch)

    def create(self) -> None:
        new_switch = models.Switch(section_id=1, machine_id=1, status=0, controlledBy_id=1)
        self.session.add(new_switch)
        self.session.commit()


switchRepository = SwitchRepository(connection_data)
