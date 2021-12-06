from controllers.app import app
from repository.switch_repo import switchRepository


@app.get("/switch")
def read_switches(filters: dict = None):
    return switchRepository.read_switches(filters)

# @app.get("/switch/history")
# def read_switch_history(num: int = 5):
#     return switchRepository.read_switch_history(num)

@app.post("/switch/create")
def create_switch():
    return switchRepository.create_switch()