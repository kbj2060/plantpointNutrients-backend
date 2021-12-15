from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from repository.watersupply_repo import waterSupplyRepository


@app.post("/watersupply")
async def read_watersupply(req: Request):
    filters = await validate_filters(req=req)
    return waterSupplyRepository.read(filters)

@app.post("/watersupply/create")
async def create_watersupply(req: Request):
    req = await req.json()
    return waterSupplyRepository.create(req['data'])