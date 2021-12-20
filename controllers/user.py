from starlette.requests import Request
from controllers.app import app
from repository.user_repo import userRepository

@app.post("/user")
def read_users(req: Request):
    return userRepository.read(req)

@app.post("/user/create")
def create_user():
    return userRepository.create()