from domain.entities.switch import Switch as eSwitch
from domain.interfaces.RequestFilters import RequestFilters
from repository.repo import BaseRepo
from repository import models
from config import connection_data
from sqlalchemy import func


class SwitchRepository(BaseRepo):
    def __init__(self, connection_data: dict) -> None:
        super().__init__(connection_data)
        self.model = models.Switch
        self.entity = eSwitch

    def read(self, filters: RequestFilters):
        if filters == None:
            return None
        elif filters.eachLast:
            sub = self.session.query(func.max(self.model.id).label('maxid')).group_by(self.model.machine_id).subquery('t2')
            query = self.session.query(self.model).join(sub, self.model.id == sub.c.maxid)
        elif filters.limit:
            query = self.session.query(self.model, models.User.name).join(self.model).order_by(self.model.id.desc()).limit(filters.limit)
        return query.all()
        
    def create(self, **kargs) -> None:
        print(kargs)
        new_switch = models.Switch(**kargs)
        self.session.add(new_switch)
        self.session.commit()


switchRepository = SwitchRepository(connection_data)
