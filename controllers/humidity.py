from controllers.app import app
from repository.humidity_repo import humidityRepository


@app.get("/humidity")
def read_humidity():
    return humidityRepository.read_humidity()

@app.get("/humidity/today")
def read_today_humidity():
    return humidityRepository.read_today_humidity()
    
@app.post("/humidity/create")
def create_humidity():
    return humidityRepository.create_humidity()