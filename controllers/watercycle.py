from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from repository.watercycle_repo import waterCycleRepository


@app.post("/watercycle")
async def read_watercycle(req: Request):
    filters = await validate_filters(req=req)
    return waterCycleRepository.read(filters)

@app.post("/watercycle/create")
def create_watercycle():
    return waterCycleRepository.create()
    