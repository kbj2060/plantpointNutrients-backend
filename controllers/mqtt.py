from controllers.app import app, mqtt
from controllers.humidity import create_humidity
from controllers.temperature import create_temperature
from config import mqtt_sub

@mqtt.on_connect()
def connect(client, flags, rc, properties):
    for sub in mqtt_sub:
        mqtt.client.subscribe(sub)
    print("Connected: ", client, flags, rc, properties)

@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    [m_section, s_section, topic] = topic.split('/')
    if topic == 'temperature':
        print(m_section, s_section, topic)
        create_temperature(m_section, s_section, payload)
    elif topic == 'humidity':
        create_humidity(m_section, s_section, payload)
