from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Date, cast
from domain.interfaces.RequestFilters import RequestFilters
from repository import models
from utils.remove_sa_state import remove_sa_state
from sqlalchemy.orm import sessionmaker


class BaseRepo:
    def __init__(self, connection_data: dict) -> None:
        connection_string = "mysql+pymysql://{}:{}@{}/{}".format(
            connection_data["user"], connection_data["password"], connection_data["host"], connection_data["dbname"]
        )
        self.engine = create_engine(connection_string, echo=True)
        models.Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        self.model = None
        self.entity = None

    def _model2entity(self, models, entity):
        if models is None: return None
        elif not isinstance(models, list): return entity(**remove_sa_state(vars(models)))
        return [ entity(**remove_sa_state(vars(q))) for q in models ]

    def _handle_filters(self, filters: RequestFilters):
        if filters.today:
            return self.session.query(self.model).filter(cast(self.model.createdAt, Date) == datetime.today())
        elif filters.limit > 0:
            return self.session.query(self.model).order_by(self.model.id.desc()).limit(filters.limit)
        else:
            return self.session.query(self.model)
    
    def read(self, filters: RequestFilters):
        if filters is None: return None
        query = self._handle_filters(filters=filters)
        return self._model2entity(models=query.all(), entity=self.entity)