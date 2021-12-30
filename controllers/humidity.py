from fastapi.params import Depends
from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.humidity_repo import humidityRepository
from sqlalchemy.orm.session import Session
from utils.get_db import get_db


@app.post("/humidity")
async def read_humidity(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return humidityRepository.read(filters)

@app.post("/humidity/create")
def create_humidity(value):
    return humidityRepository.create(value)
