from controllers.app import app
from repository.machine_repo import machineRepository


@app.get("/machines")
def read_machines():
    return machineRepository.read_machines()

@app.post("/machines/create")
def create_machines():
    return machineRepository.create_machine()