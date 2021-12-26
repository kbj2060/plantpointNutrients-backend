from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.sprayterm_repo import sprayTermRepository


@app.post("/sprayterm")
async def read_sprayterm(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return sprayTermRepository.read(filters)

@app.post("/sprayterm/create")
async def create_sprayterm(req: Request):
    period = (await req.json())['data']
    return sprayTermRepository.create(period)
