from controllers.app import app
from repository.temperature_repo import temperatureRepository


@app.get("/temperature")
def read_temperature(filters: dict = None):
    return temperatureRepository.read_temperature(filters)

@app.post("/temperature/create")
def create_temperature():
    return temperatureRepository.create_temperature()