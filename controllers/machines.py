from controllers.app import app
from repository.repo import mRepo


@app.get("/machines")
def read_machines():
    return mRepo.get_machines()

@app.get("/machines/name:{name}")
def read_machines_by_name(name: str):
    return mRepo.get_machines(filters={'name__eq': name})

@app.get("/machines/section:{section}")
def read_machines_by_section(section: str):
    return mRepo.get_machines(filters={'section__eq': section})

@app.post("/machines/add")
def create_machines():
    return mRepo.add_machine()