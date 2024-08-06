import fastapi
import uvicorn
import asyncio

# from dotenv import load_dotenv
from google_utils import sheets, models
from config import setup


app = fastapi.FastAPI()


@app.get('/conferences')
async def conferences():
    r = sheets.get_all_conferences()
    if not r:
        return 404, {"error": "No sheets found"}
    return {"data": r}


@app.get('/conferences/{conference_id}')
async def conferences():
    return {"info": "info"}


@app.post('/conferences')
async def conferences():
    r = sheets.add_conference()
    return {"post": r}


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
