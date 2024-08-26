import json
import requests as rq
import pytz
import datetime

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackContext
)

from config.setup import setup


TGCONFIG = setup('telegram bot')
BACKEND_ENDPOINT = setup('backend')


async def start(update, context):
    uid = update.message.chat.id
    uname = update.message.chat.first_name
    print(uid, uname)


async def get_conferences(update, context):
    # add filter to argument /get <filter>
    args = context.args
    if len(args) > 1:
        await update.message.reply_text('You can\'t specify more than one filter')
        return

    filter = 'active'
    if len(args) == 1:
        filter = args[0]

    try:
        params = {'filter': filter}
        resp = rq.get(BACKEND_ENDPOINT.get_uri, params=params, timeout=5)
        if resp.status_code != 200:
            raise Exception('Could not fetch data')

        pretty_json = json.dumps(resp.json(), ensure_ascii=False, indent=4)
        await update.message.reply_text(pretty_json)

    except Exception as e:
        print(e)
        await update.message.reply_text('Could not fetch data')


async def add_conference(update, context):
    uid = update.message.chat.id


async def get_conference_(update, context):
    uid = update.message.chat.id


async def notificate_users(context: CallbackContext):
    return None


async def help(update, context):
    help_message = """
/get <filter> - 
/add
/update
    """
    await update.message.reply_text(help_message)


def main():
    try:
        app = Application.builder().token(TGCONFIG.token).build()
    except Exception as e:
        print(e)
        exit(1)

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('get', get_conferences))
    app.add_handler(CommandHandler('add', add_conference))
    app.add_handler(CommandHandler('help', help))

    app.job_queue.run_daily(callback=notificate_users,
        time=datetime.time(
            hour=10,
            minute=2,
            second=0,
            tzinfo=pytz.timezone('Europe/Moscow')
        ),
        days=(0, 1, 2, 3, 4, 5, 6)
    )

    app.run_polling()


if __name__ == '__main__':
    print('Application started')
    main()