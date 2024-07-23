import fastapi
import uvicorn
import asyncio

# from dotenv import load_dotenv
from google_utils import sheets
from config import setup


app = fastapi.FastAPI()


@app.get('/')
async def index():
    sheets.get_id()
    return 200


@app.get('/conferences')
async def conferences():
    r = sheets.get_all_sheets()
    return {"status": r}


@app.get('/conferences/{conference_id}')
async def conferences():
    return {"info": "info"}


@app.post('/conferences')
async def conferences():
    return {"post": "post"}


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
