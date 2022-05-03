from starlette.requests import Request
from controllers.app import app
from repository.automation_repo import *


@app.post("/automation_history")
async def read_automation_history(req: Request):
    request = await req.json()
    return automationHistoryRepository.read(request['data'])

@app.post("/automation_history/create")
async def create_automation_history(req: Request):
    data  = (await req.json())['data']
    return automationHistoryRepository.create(**data)

@app.post("/automation_led")
async def read_automation_led(req: Request):
    return automationLedRepository.read()

@app.post("/automation_led/create")
async def create_automation_led(req: Request):
    data  = (await req.json())['data']
    return automationLedRepository.create(**data)

@app.post("/automation_ac")
async def read_automation_ac(req: Request):
    return automationACRepository.read()

@app.post("/automation_ac/create")
async def create_automation_ac(req: Request):
    data  = (await req.json())['data']
    return automationACRepository.create(**data)

@app.post("/automation_fan")
async def read_automation_fan(req: Request):
    return automationFanRepository.read()

@app.post("/automation_fan/create")
async def create_automation_fan(req: Request):
    data  = (await req.json())['data']
    return automationFanRepository.create(**data)

@app.post("/automation_rooffan")
async def read_automation_rooffan(req: Request):
    return automationRoofFanRepository.read()

@app.post("/automation_rooffan/create")
async def create_automation_rooffan(req: Request):
    data  = (await req.json())['data']
    return automationRoofFanRepository.create(**data)


