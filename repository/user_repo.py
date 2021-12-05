from typing import List
from domain.entities.user import User as eUser
from repository.repo import BaseRepo
from repository import models
from sqlalchemy.orm import sessionmaker
from config import connection_data
from utils.remove_sa_state import remove_sa_state


class UserRepository(BaseRepo):
    def _create_user_models(self, results: List[models.User]) -> List[eUser]:
        return [ eUser(**remove_sa_state(vars(q))) for q in results ]

    def read_users(self, filters: dict = None) -> List[eUser]:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(models.User)

        if filters is None:
            return self._create_user_models(query.all())
        if "section__eq" in filters:
            query = query.filter(models.User.section == filters["section__eq"])
        if "name__eq" in filters:
            query = query.filter(models.User.name == filters["name__eq"])

        return self._create_user_models(query.all())

    def create_user(self) -> None:
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_user = models.User(name="llewyn", password='temp', type='admin')
        session.add(new_user)
        session.commit()

userRepository = UserRepository(connection_data)
