import json
import requests as rq

from telegram.ext import (
    Application,
    CommandHandler   
)

from config.setup import setup


TGCONFIG = setup('telegram bot')
SHEETS_ENDPOINT = setup('sheets')
print(SHEETS_ENDPOINT.get_single_uri.format(1))


async def start(update, context):
    uid = update.message.chat.id
    uname = update.message.chat.first_name
    print(uid, uname)


async def get_conferences(update, context):
    # add filter to argument /get <filter>

    try:
        resp = rq.get(SHEETS_ENDPOINT.get_uri, timeout=5)
        if resp.status_code != 200:
            raise Exception('Could not fetch data')

        pretty_json = json.dumps(resp.json(), indent=4)
        await update.message.reply_text(pretty_json)

    except Exception as e:
        print(e)
        await update.message.reply_text('Could not fetch data')


async def add_conference(update, context):
    uid = update.message.chat.id


def main():
    try:
        app = Application.builder().token(TGCONFIG.token).build()
    except Exception as e:
        print(e)
        exit(1)

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('get', get_conferences))
    app.add_handler(CommandHandler('add', add_conference))

    try:
        app.run_polling()

    except KeyboardInterrupt:
        print('Exited by user')
        exit(0)

    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
