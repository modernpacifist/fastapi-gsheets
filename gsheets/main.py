import uvicorn
import asyncio

from fastapi import FastAPI, status, HTTPException, Request
from google_utils import sheets_ops, models
from config import setup


app = FastAPI()


# TODO: make it work with fastapi.Query
@app.get('/conferences', status_code=status.HTTP_200_OK)
async def conferences(request: Request, filter: str = 'active'):
    conferences = sheets_ops.get_all_conferences(filter)
    if not conferences:
        raise HTTPException(status_code=404, detail='No conferences found')

    if len(request.query_params.getlist('filter')) > 1:
        raise HTTPException(status_code=400, detail='Filter can be specified only once')

    if not filter in ['all', 'active', 'past', 'future']:
        raise HTTPException(status_code=400, detail='Wrong filter specified')

    return conferences


@app.get('/conferences/{conference_id}')
async def conferences(conference_id: str = None):
    if not conference_id:
        raise HTTPException(status_code=400, detail='You must provide conference id')

    if not conference_id.isdigit():
        raise HTTPException(status_code=422, detail='Conference id of must be a integer')

    conference = sheets_ops.get_conference_by_id(conference_id)
    if not conference:
        raise HTTPException(status_code=404, detail=f'Could not find conference with id {conference_id}')

    return conference


@app.post('/conferences', status_code=status.HTTP_201_CREATED)
async def conferences(conference: models.PostConference):
    r = sheets_ops.add_conference(conference)
    if not r:
        raise HTTPException(status_code=500, detail='Could not add new conference')

    return conference


@app.put('/conferences/{conference_id}')
async def conferences(conference: models.UpdateConference, conference_id: int = None):
    if not conference_id:
        raise HTTPException(status=400, detail='You must provide conference id to update it')

    r = sheets_ops.update_conference(conference_id, conference)
    if not r:
        raise HTTPException(status_code=500, detail=f'Could not update conference with id {conference_id}')

    return {'put': 'put'}


async def main(params):
    config = uvicorn.Config('main:app', host=params['host'], port=params['port'], log_level='info')
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == '__main__':
    fastapi_config = setup.fastapi()

    try:
        asyncio.run(main(fastapi_config))
    except KeyboardInterrupt as e:
        print(f'Exited by user {e}')
        exit(0)
