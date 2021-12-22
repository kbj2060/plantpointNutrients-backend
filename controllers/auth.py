import requests
from datetime import datetime, timedelta
from starlette.responses import JSONResponse
from controllers.user import create_user, read_users
from repository.schemas import User
import bcrypt
import jwt
from controllers.app import app
from starlette.requests import Request
from config import JWT_ALGORITHM, JWT_SECRET

@app.post("/register")
async def register(req: Request):
    request = await req.json()
    print(requests)
    reg_info = request['data']
    is_exist = await email_exist(reg_info['email'])
    if not (reg_info['email'] and reg_info['password']):
        return JSONResponse(status_code=400, content=dict(msg="Email and PW must be provided'"))
    if is_exist:
        return JSONResponse(status_code=400, content=dict(msg="EMAIL_EXISTS"))
    hash_pw = bcrypt.hashpw(reg_info['password'].encode("utf-8"), bcrypt.gensalt())
    user_dict = dict(id=None, password= hash_pw, email=reg_info['email'], name=reg_info['name'], createdAt=None)
    new_user = await create_user({"data": user_dict})
    token = dict(Authorization=f"Bearer {create_access_token(data=User.from_orm(new_user).dict(exclude={'password', 'createdAt'}))}")
    return token


@app.post("/login")
async def login(req: Request):
    request = await req.json()
    email = request['data']['email']
    pw = request['data']['password']
    db_user = await email_exist(email)
    if not email or not pw:
        return JSONResponse(status_code=400, content=dict(msg="Name and PW must be provided'"))
    if not db_user:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))
    is_verified = bcrypt.checkpw(pw.encode('utf-8'), db_user.password.encode('utf-8'))
    if not is_verified:
        return JSONResponse(status_code=400, content=dict(msg='NO_MATCH_USER'))
    token = dict(name=db_user.name, authorization=f"Bearer {create_access_token(data=User.from_orm(db_user).dict(exclude={'password', 'createdAt'}))}")
    return token

async def email_exist(email: str):
    get_user = read_users({"email__eq": email})
    if len(get_user) > 0:
        return get_user[0]
    return False

def create_access_token(*, data: dict = None, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + timedelta(hours=expires_delta)})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt