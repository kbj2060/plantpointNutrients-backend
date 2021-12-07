from typing import List
from config import TestConfig
from domain.entities.humidity import Humidity as eHumidity
import requests

class HumidityTester(TestConfig):
    def test_read_humidity(self):
        response = requests.get(f"{self.url}/humidity")
        result = response.json()
        if response.status_code == 200:
            if isinstance(result, list) and isinstance(result[0], eHumidity):
                return True
            elif isinstance(result, eHumidity):
                return True
            else:
                return "result are not valid!"
        else:
            return "response status is not OK!"
    
    def test_create_humidity(self):
        response = requests.post(f"{self.url}/humidity/create")
        print(response)
