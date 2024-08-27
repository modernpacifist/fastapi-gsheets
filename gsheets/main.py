import uvicorn
import asyncio

from fastapi import FastAPI, status, HTTPException, Request
from config.setup import setup
from sheets import conferences, models, utils


APP = FastAPI()
FASTAPI_CONF = setup('fastapi')
SHEETS_CONF = setup('google sheets')
SHEETS_CONF.fields = utils.get_fields()


@APP.get('/conferences', status_code=status.HTTP_200_OK)
async def conferences_handler(request: Request, filter: str = 'active'):
    res = conferences.get_all(SHEETS_CONF, filter)
    # res = conferences.get_all(filter)
    if not res:
        raise HTTPException(status_code=404, detail='No conferences found')

    if len(request.query_params.getlist('filter')) > 1:
        raise HTTPException(status_code=400, detail='Filter can be specified only once')

    if not filter in ['all', 'active', 'past', 'future']:
        raise HTTPException(status_code=400, detail='Wrong filter specified')

    return res


@APP.get('/conferences/{conference_id}')
async def conferences_handler(conference_id: str = None):
    if not conference_id:
        raise HTTPException(status_code=400, detail='You must provide conference id')

    if not conference_id.isdigit():
        raise HTTPException(status_code=422, detail='Conference id of must be a integer')

    res = conferences.get_by_id(conference_id)
    if not res:
        raise HTTPException(status_code=404, detail=f'Could not find conference with id {conference_id}')

    return res


@APP.post('/conferences', status_code=status.HTTP_201_CREATED)
async def conferences_handler(conference: models.PostConference):
    res = conferences.add(conference)
    if not res:
        raise HTTPException(status_code=500, detail='Could not add new conference')

    return res


@APP.put('/conferences/{conference_id}')
async def conferences_handler(conference: models.UpdateConference, conference_id: str = None):
    if not conference_id:
        raise HTTPException(status=400, detail='You must provide conference id to update it')

    res = conferences.update(conference_id, conference)
    if not res:
        raise HTTPException(status_code=500, detail=f'Could not update conference with id {conference_id}')

    if res == -1:
        raise HTTPException(status_code=404, detail=f'Conference with id {conference_id} does not exist')

    return res


async def main(conf):
    config = uvicorn.Config('main:APP', host=conf.host, port=conf.port, log_level='info')
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == '__main__':
    try:
        asyncio.run(main(FASTAPI_CONF))
    except KeyboardInterrupt as e:
        print(f'Exited by user {e}')
        exit(0)
