from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.watersupply_repo import waterSupplyRepository


@app.post("/watersupply")
async def read_watersupply(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return waterSupplyRepository.read(filters)

@app.post("/watersupply/create")
async def create_watersupply(req: Request):
    quantity = (await req.json())['data']
    return waterSupplyRepository.create(quantity)