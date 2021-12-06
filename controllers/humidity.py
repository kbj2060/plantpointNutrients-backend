from controllers.app import app
from repository.humidity_repo import humidityRepository


@app.get("/humidity")
def read_humidity(filters: dict = None):
    return humidityRepository.read_humidity(filters)

@app.post("/humidity/create")
def create_humidity():
    return humidityRepository.create_humidity()