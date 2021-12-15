from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from repository.waterspray_repo import waterSprayRepository


@app.post("/waterspray")
async def read_waterspray(req: Request):
    filters = await validate_filters(req=req)
    return waterSprayRepository.read(filters)

@app.post("/waterspray/create")
async def create_waterspray(req: Request):
    req = await req.json()
    return waterSprayRepository.create(req['data'])
    