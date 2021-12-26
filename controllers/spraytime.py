from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.spraytime_repo import sprayTimeRepository


@app.post("/spraytime")
async def read_spraytime(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return sprayTimeRepository.read(filters)

@app.post("/spraytime/create")
async def create_spraytime(req: Request):
    period = (await req.json())['data']
    return sprayTimeRepository.create(period)
    