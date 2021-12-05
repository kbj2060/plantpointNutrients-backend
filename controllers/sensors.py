from controllers.app import app
from repository.sensor_repo import sensorRepository


@app.get("/sensors")
def read_machines():
    return sensorRepository.get_sensors()

# @app.get("/sensors/name:{name}")
# def read_sensors_by_name(name: str):
#     return sensorRepository.get_sensors(filters={'name__eq': name})

# @app.get("/sensors/section:{section}")
# def read_sensors_by_section(section: str):
#     return sensorRepository.get_sensors(filters={'section__eq': section})