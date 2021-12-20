import requests
from datetime import datetime, timedelta
from starlette.responses import JSONResponse
from controllers.user import read_users
from repository.schemas import User
import bcrypt
import jwt
from controllers.app import app
from starlette.requests import Request
from config import JWT_ALGORITHM, JWT_SECRET


@app.post("/login")
async def login(req: Request):
    request = await req.json()
    name = request['data']['email']
    pw = request['data']['password'].encode('utf-8')
    db_user = await name_exist(name)
    # DB에 넣을 때 회원가입할 때 salting을 하지 않고 넣었기 때문에 checkpw 에러 발생!
    if not name or not pw:
        return JSONResponse(status_code=400, content=dict(msg="Name and PW must be provided'"))
    if not db_user:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))
    is_verified = bcrypt.checkpw(pw, db_user.password.encode('utf-8'))
    if not is_verified:
        return JSONResponse(status_code=400, content=dict(msg='NO_MATCH_USER'))
    token = dict(Authorization=f"Bearer {create_access_token(data=User.from_orm(db_user).dict(exclude={'password', 'marketig_agree'}),)}")
    return token

async def name_exist(name: str):
    get_name = read_users({"name__eq": name})
    if len(get_name) > 0:
        return get_name[0]
    return False

def create_access_token(*, data: dict = None, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + timedelta(hours=expires_delta)})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt