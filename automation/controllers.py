import requests

async def getLastAutomation(label):
    response = requests.post(f"localhost/{label}", {"limit": 1})
    return response