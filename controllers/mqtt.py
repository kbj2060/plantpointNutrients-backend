from controllers.app import app
from controllers.humidity import create_humidity
from controllers.temperature import create_temperature
from fastapi_mqtt import FastMQTT, MQTTConfig
from config import SECTION

'''
section/switch/waterpump
section/environment/temperature
,,,
'''

mqtt_config = MQTTConfig(
    host = "localhost",
    port= 1883,
    keepalive = 60
)
mqtt = FastMQTT(
    config=mqtt_config
    )
mqtt.init_app(app)

@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe(f'{SECTION}/#')
    print("Connected: ", client, flags, rc, properties)

@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    topic= topic.split('/')[-1]
    if topic == 'temperature':
        create_temperature(payload)
    elif topic == 'humidity':
        create_humidity(payload)
