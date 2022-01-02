from fastapi.params import Depends
from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.CreateEnvironment import CreateEnvironment
from domain.interfaces.RequestFilters import RequestFilters
from repository.humidity_repo import humidityRepository
from sqlalchemy.orm.session import Session
from utils.get_db import get_db


@app.post("/humidity")
async def read_humidity(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return humidityRepository.read(filters)

@app.post("/humidity/create")
async def create_humidity(req: Request):
    data: CreateEnvironment = (await req.json())['data']
    return humidityRepository.create(data['value'])
