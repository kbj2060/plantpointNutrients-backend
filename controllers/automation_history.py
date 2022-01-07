from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.automation_history_repo import automationHistoryRepository


@app.post("/automation_history")
async def read_automation_history(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return automationHistoryRepository.read(filters)

@app.post("/automation_history/create")
async def create_automation_history(req: Request):
    data  = (await req.json())['data']
    return automationHistoryRepository.create(**data)
