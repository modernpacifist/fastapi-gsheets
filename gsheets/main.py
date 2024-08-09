import uvicorn
import asyncio

# from dotenv import load_dotenv
from fastapi import FastAPI, Response, status, HTTPException
from google_utils import sheets_ops, models
from config import setup


app = FastAPI()


@app.get('/conferences', status_code=status.HTTP_200_OK)
async def conferences(filter: str = None):
    r = sheets_ops.get_all_conferences()
    if not r:
        raise HTTPException(status_code=404, detail='No conferences found')

    return {"data": r}


@app.get('/conferences/{conference_id}', status_code=status.HTTP_200_OK)
async def conferences(conference_id: int = None):
    if not conference_id:
        return {'info': 'You must provide a conference id'}

    r = sheets_ops.get_conference_by_id(conference_id)
    if not r:
        return {'info': f'Could not find conference with id {conference_id}'}

    return {'info': conference_id}


@app.post('/conferences', status_code=status.HTTP_201_CREATED)
async def conferences():
    r = sheets_ops.add_conference()
    if not r:
        raise HTTPException(status_code=500, detail='Could not add new conference')
        # return {'Error': 'Could not add new conference'}

    return {'data': r}


@app.put('/conferences/{conference_id}')
async def conferences():
    return {"put": "put"}


async def main(params):
    config = uvicorn.Config("main:app", host=params['host'], port=params['port'], log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    fastapi_config = setup.fastapi()

    try:
        asyncio.run(main(fastapi_config))
    except KeyboardInterrupt as e:
        print(f"Exited by user {e}")
        exit(0)
