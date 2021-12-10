from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from repository.switch_repo import switchRepository


@app.post("/switch")
async def read_switches(req: Request):
    filters = await validate_filters(req=req)
    return switchRepository.read(filters)

@app.post("/switch/create")
def create_switch():
    return switchRepository.create()