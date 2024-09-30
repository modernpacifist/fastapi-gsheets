# fastapi-gsheets
Pet project developed during bachelor computer science course at [SUAI](https://guap.ru/en/) university.  

### What its for: 
- Organize conferences
- Notify users about upcoming events
- Upload files for conferences to google drive
- Google sheets used as main database
- Telegram bot is used by organizers

### Stack:
- fastapi
- python-telegram-bot
- google sheets
- google drive
- sqlite

### Set up:
Before running, you need to get `credentials.json` file from google, [e.g.](https://developers.google.com/workspace/guides/create-credentials), and put it in `./gsheets/config` and `./tgbot/config` directories.

### Run via docker
```sh
docker-compose up
```