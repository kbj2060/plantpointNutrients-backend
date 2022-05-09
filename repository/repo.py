from datetime import date
from sqlalchemy import Date, cast
from domain.interfaces.RequestFilters import RequestFilters
from utils.remove_sa_state import remove_sa_state
from controllers.app import session

class BaseRepo:
    def __init__(self) -> None:
        self.model = None
        self.entity = None

    def _model2entity(self, models, entity):
        if models is None: return None
        elif not isinstance(models, list): return entity(**remove_sa_state(vars(models)))
        return [ entity(**remove_sa_state(vars(q))) for q in models ]

    def _handle_filters(self, filters: RequestFilters):
        if filters.today:
            return session.query(self.model).filter(cast(self.model.createdAt, Date) == date.today())
        elif filters.limit > 0:
            return session.query(self.model).order_by(self.model.id.desc()).limit(filters.limit)
    
    def read(self, filters: RequestFilters):
        if filters is None: 
            return None
        query = self._handle_filters(filters=filters)
        if query is not None: 
            return self._model2entity(models=query.all(), entity=self.entity)
        else: print('Error report is written.')