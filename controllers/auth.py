from starlette.responses import JSONResponse
from repository.schemas import User
import bcrypt
import jwt
from fastapi import APIRouter, Depends, applications
from controllers.app import app
from starlette.requests import Request

# https://velog.io/@hyeseong-dev/FastAPI-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-endpoint
@app.post("/login")
async def login(req: Request):
    name = None
    pw = None
    is_exist = await is_name_exist(name)
    if not name or not pw:
        return JSONResponse(status_code=400, content=dict(msg="Name and PW must be provided'"))
    if not is_exist:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))
    user = User.get(name=name)
    print(user)
    is_verified = bcrypt.checkpw(pw.encode("utf-8"), user.pw.encode('utf-8'))
    if not is_verified:
        return JSONResponse(status_code=400, content=dict(msg='NO_MATCH_USER'))
    token = dict(Authorization=f"Bearer {create_access_token(data=UserToken.from_orm(user).dict(exclude={'pw', 'marketig_agree'}),)}")
    return token
    return JSONResponse(status_code=400, content=dict(msg="NOT_SUPPORTED"))

async def is_name_exist(name: str):
    get_name = User.get(name=name)
    if get_name:
        return True
    return False