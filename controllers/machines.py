from controllers.app import app
from repository.repo import repo


@app.get("/machines")
def read_machines():
    return repo.get_machines()

@app.get("/machines/name:{name}")
def read_machines_by_name(name: str):
    return repo.get_machines(filters={'name__eq': name})

@app.get("/machines/section:{section}")
def read_machines_by_section(section: str):
    return repo.get_machines(filters={'section__eq': section})