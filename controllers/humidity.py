from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestFilters import RequestFilters
from repository.humidity_repo import humidityRepository


@app.post("/humidity")
async def read_humidity(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return humidityRepository.read(filters)

@app.post("/humidity/create")
def create_humidity(value):
    '''
        온도 및 습도 추가는 mqtt로 가능하기 때문에 
        http 통신을 이용한 Request 필요없음
    '''
    return humidityRepository.create(value)
