from controllers.app import app
from repository.machine_repo import machineRepository


@app.get("/machines")
def read_machines(filters: dict = None):
    return machineRepository.read_machines(filters)

@app.post("/machines/create")
def create_machines():
    return machineRepository.create_machine()