from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from domain.entities.sprayterm import SprayTerm as eSprayTerm
from repository.repo import BaseRepo
from repository import models
from controllers.app import session


class SprayTermRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.SprayTerm
        self.entity = eSprayTerm

    def create(self, period):
        new_waterspray: models.SprayTerm = models.SprayTerm(period=period)
        session.add(new_waterspray)
        session.commit()

sprayTermRepository = SprayTermRepository()
