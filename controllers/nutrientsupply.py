from controllers.app import app
from controllers.utils import validate_filters
from repository.nutrientsupply_repo import nutrientSupplyRepository
from fastapi import Request


@app.post("/nutrientsupply")
async def read_nutrientsupply(req: Request):
    filters = await validate_filters(req=req)
    return nutrientSupplyRepository.read(filters)

@app.post("/nutrientsupply/create")
def create_nutrientsupply():
    return nutrientSupplyRepository.create()