from starlette.requests import Request
from controllers.app import app, mqtt
from controllers.utils import validate_filters
from repository.humidity_repo import humidityRepository


@app.post("/humidity")
async def read_humidity(req: Request):
    filters = await validate_filters(req=req)
    return humidityRepository.read(filters)

@app.post("/humidity/create")
def create_humidity():
    return humidityRepository.create()

@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("mqtt")
    print("Connected: ", client, flags, rc, properties)

@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", properties)

@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ",topic, payload.decode())