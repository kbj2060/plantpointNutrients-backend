from typing import Optional
from fastapi import Request
from controllers.app import app
from repository.schemas import RequestFilters
from repository.temperature_repo import temperatureRepository

@app.post("/temperature")
async def read_temperature(req: Request):
    try:
        req = await req.json()
        data = RequestFilters(**req['data'])
        return temperatureRepository.read_temperature(data)
    except:
        print("Reading temperature has a problem in communication with front!")

@app.post("/temperature/create")
def create_temperature():
    return temperatureRepository.create_temperature()