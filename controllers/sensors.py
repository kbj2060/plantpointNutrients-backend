from controllers.app import app
from repository.sensor_repo import sensorRepository


@app.get("/sensor")
def read_sensors():
    return sensorRepository.read()

@app.post("/sensor/create")
def create_sensor():
    return sensorRepository.create()