from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy
from sqlalchemy.orm.session import sessionmaker
from config import connection_data
from repository import models

from domain.request_objects import origin_request as req
from domain.response_objects import origin_response as res


STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
}

fastapi = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:3000",
    "http://mudeulro29.iptime.org:3001"
]


fastapi.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "mysql+pymysql://{}:{}@{}/{}".format(
    connection_data["user"], connection_data["password"], connection_data["host"], connection_data["dbname"]
)
engine = sqlalchemy.create_engine(
    DATABASE_URL
)
models.Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = fastapi