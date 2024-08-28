import json
import requests as rq
import pytz
import datetime

from db import operations as db
from models import backend

from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    CallbackContext,
    filters
)

from config.setup import setup


TGCONFIG = setup('telegram bot')
BACKEND_ENDPOINT = setup('backend')
DB_CONF = setup('database')


# @operations.authentication_decorator
async def start(update, context):
    uid = update.message.chat.id
    uname = update.message.chat.first_name

    if db.verify_user(DB_CONF, uid):
        await update.message.reply_text('You are already registered')
        return

    db.add_user(DB_CONF, uid, uname)


# @db.authentication_decorator
async def get_conferences(update, context):
    uid = update.message.chat.id
    if not db.verify_user(DB_CONF, uid):
        await update.message.reply_text('Not registered, run /start')
        return

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
    if not db.verify_user(DB_CONF, uid):
        await update.message.reply_text('Not registered, run /start')
        return

    await update.message.reply_text("""
Adding new conference entry  
Specify data in following format:  
```
google_spreadsheet: what's up,
google_drive_directory_id: google 5,
name_rus: full rus name 5,
name_rus_short: short rus name 5,
registration_start_date: 01.02.2023,
registration_end_date: 02.09.2025,
submission_start_date: 03.09.2013,
submission_end_date: 04.09.2013,
conf_start_date: 05.09.2013,
conf_end_date: 06.09.2013,
organized_by: SUAI,
url: https://google.com,
email: hehexd@gmail.com
```
""", parse_mode='MarkdownV2')

    return 0

    model = backend.PostConference()

    try:
        rq.post(BACKEND_ENDPOINT.post_uri, data=model, timeout=5)

    except Exception as e:
        print(e)


async def getting_model(update, context):
    print('getting_model')

    user_input = update.message.text

    print(user_input)


    return ConversationHandler.END


async def get_conference(update, context):
    uid = update.message.chat.id


async def update_conference(update, context):
    uid = update.message.chat.id


async def send_applications_report_document(update, context):
    uid = update.message.chat.id


async def send_conference_report_document(update, context):
    uid = update.message.chat.id


async def send_publications_report_document(update, context):
    uid = update.message.chat.id


async def notificate_users(context: CallbackContext):
    """
    Check if any conferences are active today and notificate users
    """
    print(db.get_all_users(DB_CONF))


async def cancel(update, _):
    await update.message.replly_text('cancelled')
    return ConversationHandler.END


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
        print(f'Could not startup the application: {e}')
        exit(1)

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('get', get_conferences))
    app.add_handler(CommandHandler('help', help))


    add_conference_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_conference)],
        states={
            0: [
                MessageHandler(
                    filters.ALL,
                    getting_model,
                )
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    app.add_handler(add_conference_conv_handler)


    # app.job_queue.run_daily(
    #     callback=notificate_users,
    #     time=datetime.time(
    #         hour=10,
    #         minute=2,
    #         second=0,
    #         tzinfo=pytz.timezone('Europe/Moscow')
    #     ),
    #     days=(0, 1, 2, 3, 4, 5, 6)
    # )
    # app.job_queue.run_repeating(
    #     callback=notificate_users,
    #     interval=2,
    # )

    app.run_polling()


if __name__ == '__main__':
    print('Application started')
    main()