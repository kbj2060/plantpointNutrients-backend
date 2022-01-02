from pydantic import BaseModel


class CreateEnvironment(BaseModel):
    value: float