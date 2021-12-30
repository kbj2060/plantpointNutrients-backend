from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from domain.entities.spraytime import SprayTime as eSprayTime
from repository.repo import BaseRepo
from repository import models
from utils.get_db import get_db


class SprayTimeRepository(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = models.SprayTime
        self.entity = eSprayTime

    def create(self, period, db=next(get_db())):
        new_spraytime: models.SprayTime = models.SprayTime(period=period)
        db.add(new_spraytime)
        db.commit()

sprayTimeRepository = SprayTimeRepository()
