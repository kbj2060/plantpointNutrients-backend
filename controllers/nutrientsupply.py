from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.nutrientsupply_repo import nutrientSupplyRepository
from fastapi import Request


@app.post("/nutrientsupply")
async def read_nutrientsupply(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return nutrientSupplyRepository.read(filters)

@app.post("/nutrientsupply/create")
async def create_nutrientsupply(req: Request):
    quantity = (await req.json())['data']
    return nutrientSupplyRepository.create(quantity)