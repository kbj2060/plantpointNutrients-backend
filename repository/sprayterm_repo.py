from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from domain.entities.sprayterm import SprayTerm as eSprayTerm
from repository.repo import BaseRepo
from repository import models
from utils.get_db import get_db


class SprayTermRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.SprayTerm
        self.entity = eSprayTerm

    def create(self, period, db=next(get_db())):
        new_waterspray: models.SprayTerm = models.SprayTerm(period=period)
        db.add(new_waterspray)
        db.commit()

sprayTermRepository = SprayTermRepository()
