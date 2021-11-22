from fastapi import FastAPI

from domain.request_objects import origin_request as req
from domain.response_objects import origin_response as res


STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500,
}

app = FastAPI()