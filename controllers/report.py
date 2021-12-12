from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from repository.report_repo import reportRepository


@app.post("/report")
async def read_report(req: Request):
    filters = await validate_filters(req=req)
    return reportRepository.read(filters)

@app.post("/report/create")
def create_report():
    return reportRepository.create()
