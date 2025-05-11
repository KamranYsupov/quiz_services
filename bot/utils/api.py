from http.client import HTTPException

from aiohttp import ClientResponse


async def get_response_data_or_raise_exception(
        response: ClientResponse
):
    if response.ok:
        return await response.json()
    else:
        e = f'{await response.text()}\nstatus code: {response.status}'
        raise HTTPException(e)
