from starlette.requests import Request
from controllers.app import app
from controllers.utils import validate_filters
from domain.interfaces.RequestCreateSwitch import RequestCreateSwitch
from domain.interfaces.RequestFilters import RequestFilters
from repository.switch_repo import switchRepository
from controllers.mqtt import mqtt
from config import SECTION

@app.post("/switch")
async def read_switches(req: Request):
    filters: RequestFilters = await validate_filters(req=req)
    return switchRepository.read(filters)

@app.post("/switch/create")
async def create_switch(req: Request):
    res = await req.json()
    data: RequestCreateSwitch = res['data']
    mqtt.publish(f"{SECTION}/switch/{data['name']}", data['status']) #publishing mqtt topic
    return switchRepository.create(data)