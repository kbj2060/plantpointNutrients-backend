from typing import List
from fastapi.params import Depends

from sqlalchemy.orm.session import Session
from domain.entities.user import User as eUser
from domain.interfaces.CreateUser import CreateUser
from domain.interfaces.ReadUser import ReadUser
from repository.repo import BaseRepo
from repository import models
from controllers.app import session

class UserRepository(BaseRepo):
    def read(self, filters: ReadUser = None) -> List[eUser]:
        query = session.query(models.User)
        if filters is None:
            return None
        if "email__eq" in filters:
            result_models = query.filter(models.User.email == filters["email__eq"]).first()
        if "name__eq" in filters:
            result_models = query.filter(models.User.name == filters["name__eq"]).first()
        return self._model2entity(models=result_models, entity=eUser)

    def create(self, user: CreateUser) -> CreateUser:
        new_user: models.User = models.User(
            name=user.name, 
            email=user.email, 
            password=user.password
            )
        session.add(new_user)
        session.commit()
        return new_user

userRepository = UserRepository()
