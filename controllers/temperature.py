from controllers.app import app
from repository.temperature_repo import temperatureRepository


@app.get("/temperature")
def read_temperature():
    return temperatureRepository.read_temperature()

@app.post("/temperature/create")
def create_temperature():
    return temperatureRepository.create_temperature()