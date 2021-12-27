from starlette.requests import Request
from controllers.app import app
from domain.interfaces.CreateUser import CreateUser
from domain.entities.user import User as eUser
from repository.user_repo import userRepository

@app.post("/user")
def read_users(req: Request) -> eUser:
    return userRepository.read(req)

@app.post("/user/create")
async def create_user(req):
    requests = req['data'] if type(req) is dict else (await req.json())['data']
    user = CreateUser(**requests)
    return userRepository.create(user)