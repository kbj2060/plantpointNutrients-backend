from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.report_repo import reportRepository


@app.post("/report")
async def read_report(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return reportRepository.read(filters)

@app.post("/report/create")
async def create_report(req: Request):
    report = (await req.json())['data']
    return reportRepository.create(**report)
