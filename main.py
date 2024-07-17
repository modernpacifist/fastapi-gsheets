import fastapi
import uvicorn
import asyncio

from dotenv import load_dotenv
from google_utils import auth, sheets


load_dotenv()
app = fastapi.FastAPI()


@app.get('/')
async def index():
    sheets.get_id()
    return 200


@app.get('/conferences')
async def conferences():
    r = auth.setup_account()
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


async def main():
    config = uvicorn.Config("main:app", host="0.0.0.0", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print(f"Exited by user {e}")
        exit(0)
