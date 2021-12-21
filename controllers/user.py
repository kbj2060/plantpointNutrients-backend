from typing import Union
from starlette.requests import Request
from controllers.app import app
from domain.interfaces.CreateUser import CreateUser
from repository.user_repo import userRepository
from operator import itemgetter

@app.post("/user")
def read_users(req: Request):
    return userRepository.read(req)

@app.post("/user/create")
async def create_user(req):
    if type(req) is dict:
        requests = req['data']
    else:
        requests = (await req.json())['data']
    print(requests)
    user = CreateUser(**requests)
    return userRepository.create(user)