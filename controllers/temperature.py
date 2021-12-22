from fastapi import Request
from controllers.app import app
from controllers.utils import validate_filters
from repository.temperature_repo import temperatureRepository


@app.post("/temperature")
async def read_temperature(req: Request):
    print(await req.json())
    filters = await validate_filters(req=req)
    return temperatureRepository.read(filters)

@app.post("/temperature/create")
def create_temperature(value):
    return temperatureRepository.create(value)