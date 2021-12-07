import sys
sys.path.append('c:\\Users\\kbj20\\OneDrive\\바탕 화면\\github\\plantpointNutrients-backend')

from fastapi.testclient import TestClient
from controllers.app import app

class TestConfig:
  def __init__(self) -> None:
    self.address = "127.0.0.1"
    self.port = 8000
    self.url = f"http://{self.address}:{self.port}"
    self.client = TestClient(app)

  def get_url(self):
    return self.url
