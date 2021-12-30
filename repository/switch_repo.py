from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from controllers.user import read_users
from domain.entities.switch import Switch as eSwitch
from domain.interfaces.RequestCreateSwitch import RequestCreateSwitch
from domain.interfaces.RequestFilters import RequestFilters
from repository.repo import BaseRepo
from repository import models
from sqlalchemy import func
from domain.entities.user import User as eUser
from utils.get_db import get_db


class SwitchRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.Switch
        self.entity = eSwitch

    def read(self, filters: RequestFilters, db=next(get_db())):
        if filters == None:
            return None
        elif filters.eachLast:
            sub = db.query(func.max(self.model.id).label('maxid')).group_by(self.model.machine_id).subquery('t2')
            query = db.query(self.model).join(sub, self.model.id == sub.c.maxid)
        elif filters.limit:
            query = db.query(
                self.model.status.label('status'),
                self.model.createdAt.label('createdAt'),
                models.User.name.label('username'),
                models.Machine.name.label('machinename')
            ).join(models.User, models.Machine).order_by(self.model.id.desc()).limit(filters.limit)
        elif filters.autoEachLast:
            sub = db.query(func.max(self.model.id).label('maxid'), models.User.name).join(models.User).filter(models.User.name == 'auto').group_by(self.model.machine_id).subquery('t2')
            query = db.query(self.model).join(sub, self.model.id == sub.c.maxid)
        return query.all()

    def create(self, data: RequestCreateSwitch, db=next(get_db())) -> eUser:
        if not data['controlledBy']: return
        user: eUser = read_users({"name__eq": data['controlledBy']})
        if not user: return
        new_switch: models.Switch = models.Switch(
            machine_id=data['machine_id'],
            status=data['status'],
            controlledBy_id=user.id
            )
        db.add(new_switch)
        db.commit()
        return user.to_dict()


switchRepository = SwitchRepository()
