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
    requests = req['data'] if type(req) is dict else (await req.json())['data']
    user = CreateUser(**requests)
    return userRepository.create(user)