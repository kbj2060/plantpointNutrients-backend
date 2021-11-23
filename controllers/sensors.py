from controllers.app import app
from repository.repo import sRepo


@app.get("/sensors")
def read_machines():
    return sRepo.get_sensors()

@app.get("/sensors/name:{name}")
def read_sensors_by_name(name: str):
    return sRepo.get_sensors(filters={'name__eq': name})

@app.get("/sensors/section:{section}")
def read_sensors_by_section(section: str):
    return sRepo.get_sensors(filters={'section__eq': section})