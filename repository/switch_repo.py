from controllers.user import read_users
from domain.entities.switch import Switch as eSwitch
from domain.interfaces.RequestCreateSwitch import RequestCreateSwitch
from domain.interfaces.RequestFilters import RequestFilters
from repository.repo import BaseRepo
from repository import models
from config import connection_data
from sqlalchemy import func
from domain.entities.user import User as eUser


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
            query = self.session.query(
                self.model.status.label('status'),
                self.model.createdAt.label('createdAt'),
                models.User.name.label('username'),
                models.Machine.name.label('machinename')
            ).join(models.User, models.Machine).order_by(self.model.id.desc()).limit(filters.limit)
        elif filters.autoEachLast:
            sub = self.session.query(func.max(self.model.id).label('maxid'), models.User.name).join(models.User).filter(models.User.name == 'auto').group_by(self.model.machine_id).subquery('t2')
            query = self.session.query(self.model).join(sub, self.model.id == sub.c.maxid)
        return query.all()

    def create(self, data: RequestCreateSwitch) -> eUser:
        if not data['controlledBy']: return
        user: eUser = read_users({"name__eq": data['controlledBy']})
        if not user: return
        new_switch: models.Switch = models.Switch(
            machine_id=data['machine_id'],
            status=data['status'],
            controlledBy_id=user.id
            )
        self.session.add(new_switch)
        self.session.commit()
        return user.to_dict()


switchRepository = SwitchRepository(connection_data)
