from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from repository import models
from config import connection_data

def get_db():
    connection_string = "mysql+pymysql://{}:{}@{}/{}".format(
        connection_data["user"], connection_data["password"], connection_data["host"], connection_data["dbname"]
    )
    engine = create_engine(connection_string, echo=True)
    models.Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        print('DB opened!')
        yield session
    finally:
        print('DB closed!')
        session.close()