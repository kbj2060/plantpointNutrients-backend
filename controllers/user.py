from controllers.app import app
from repository.user_repo import userRepository


@app.get("/user")
def read_users():
    return userRepository.read_users()

@app.post("/user/create")
def create_user():
    return userRepository.create_user()