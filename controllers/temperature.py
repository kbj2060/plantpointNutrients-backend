from fastapi import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.CreateEnvironment import CreateEnvironment
from domain.interfaces.RequestFilters import RequestFilters
from repository.temperature_repo import temperatureRepository


@app.post("/temperature")
async def read_temperature(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return temperatureRepository.read(filters)

@app.post("/temperature/create")
async def create_temperature(req: Request):
    data: CreateEnvironment = (await req.json())['data']
    return temperatureRepository.create(data['value'])