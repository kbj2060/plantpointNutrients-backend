import json
from fastapi import Request
from domain.interfaces.RequestFilters import RequestFilters

async def validate_filters(req: Request):
    try:
        request = await req.json()
    except:
        req = await req.body()
        request = json.loads(req.decode('utf-8'))
    filters = RequestFilters(**(request['data']))
    return filters