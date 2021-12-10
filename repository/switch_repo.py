from domain.entities.switch import Switch as eSwitch
from domain.interfaces.RequestFilters import RequestFilters
from repository.repo import BaseRepo
from repository import models
from config import connection_data


class SwitchRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Switch
        self.entity = eSwitch

    def read(self, filters: RequestFilters):
        query = self.session.query(self.model, models.User.name).join(self.model).order_by(self.model.id.desc()).limit(filters.limit)
        print(query.all())
        return query.all()
        
    def create(self) -> None:
        new_switch = models.Switch(section_id=1, machine_id=1, status=0, controlledBy_id=1)
        self.session.add(new_switch)
        self.session.commit()


switchRepository = SwitchRepository(connection_data)
