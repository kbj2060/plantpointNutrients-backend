from typing import List
from domain.entities.user import User as eUser
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from utils.remove_sa_state import remove_sa_state


class UserRepository(BaseRepo):
    def read(self, filters: dict = None) -> List[eUser]:
        query = self.session.query(models.User)

        if filters is None:
            return self._model2entity(models=query.all(), entity=eUser)
        if "section__eq" in filters:
            result_models = query.filter(models.User.section == filters["section__eq"]).all()
        if "name__eq" in filters:
            result_models = query.filter(models.User.name == filters["name__eq"]).all()

        return self._model2entity(models=result_models, entity=eUser)

    def create(self) -> None:
        new_user = models.User(name="llewyn", password='temp', type='admin')
        self.session.add(new_user)
        self.session.commit()

userRepository = UserRepository(connection_data)
