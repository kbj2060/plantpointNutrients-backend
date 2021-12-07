from fastapi import Request
from domain.interfaces.RequestFilters import RequestFilters

async def validate_filters(req: Request):
    try:
        request = await req.json()
        filters = RequestFilters(**(request['data']))
        return filters
    except:
        print("Reading data has a problem in communication with front!")
        return None