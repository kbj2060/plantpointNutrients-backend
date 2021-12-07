from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from repository.humidity_repo import humidityRepository


@app.post("/humidity")
async def read_humidity(req: Request):
    filters = await validate_filters(req=req)
    return humidityRepository.read(filters)

@app.post("/humidity/create")
def create_humidity():
    return humidityRepository.create()