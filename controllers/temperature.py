from fastapi import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.temperature_repo import temperatureRepository


@app.post("/temperature")
async def read_temperature(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return temperatureRepository.read(filters)

@app.post("/temperature/create")
def create_temperature(value):
    return temperatureRepository.create(value)