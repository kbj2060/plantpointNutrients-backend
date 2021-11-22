from controllers.app import app
from repository.repo import repo


@app.get("/sensors")
def read_machines():
    return repo.get_sensors()

@app.get("/sensors/name:{name}")
def read_sensors_by_name(name: str):
    return repo.get_sensors(filters={'name__eq': name})

@app.get("/sensors/section:{section}")
def read_sensors_by_section(section: str):
    return repo.get_sensors(filters={'section__eq': section})