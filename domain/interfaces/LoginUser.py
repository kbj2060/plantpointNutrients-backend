from pydantic import BaseModel


class LoginUser(BaseModel):
    email__eq: str
    name__eq: str