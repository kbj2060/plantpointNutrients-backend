from datetime import date
from sqlalchemy import Date, cast
from sqlalchemy.orm.session import Session
from controllers.app import database
from domain.interfaces.RequestFilters import RequestFilters
from utils.get_db import get_db
from utils.remove_sa_state import remove_sa_state
from fastapi.params import Depends

class BaseRepo:
    def __init__(self) -> None:
        self.model = None
        self.entity = None
        self.db = get_db()

    def _model2entity(self, models, entity):
        if models is None: return None
        elif not isinstance(models, list): return entity(**remove_sa_state(vars(models)))
        return [ entity(**remove_sa_state(vars(q))) for q in models ]

    def _handle_filters(self, filters: RequestFilters, db: Session):
        if filters.today:
            return self.db.query(self.model).filter(cast(self.model.createdAt, Date) == date.today())
        elif filters.limit > 0:
            return self.db.query(self.model).order_by(self.model.id.desc()).limit(filters.limit)
    
    def read(self, filters: RequestFilters, db=next(get_db())):
        if filters is None: return None
        query = self._handle_filters(filters=filters, db=db)
        if query is not None: return self._model2entity(models=query.all(), entity=self.entity)
        else: print('Error report is written.')