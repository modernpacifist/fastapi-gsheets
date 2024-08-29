import json
import requests as rq

from db import operations as db
from gdrive import operations as gdrive

from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    CallbackContext,
    filters
)

from config.setup import setup
from utils.conversations import ValuePasser


TGCONFIG = setup('telegram bot')
BACKEND_ENDPOINT = setup('backend')
DB_CONF = setup('database')
DRIVE_CONF = setup('google drive')

UPDATE_ID = ValuePasser()


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
        return ConversationHandler.END

    await update.message.reply_text("""
Adding new conference entry  
Specify data as following e g :  
```
{
    "google_spreadsheet": "example",
    "google_drive_directory_id": "example",
    "name_rus": "name",
    "name_rus_short": "short name",
    "registration_start_date": "01.08.2024",
    "registration_end_date": "01.10.2024",
    "submission_start_date": "01.08.2024",
    "submission_end_date": "01.10.2024",
    "conf_start_date": "01.10.2024",
    "conf_end_date": "10.10.2024",
    "organized_by": "SUAI",
    "url": "https://suai.com",
    "email": "suai@gmail.com"
}
```
""", parse_mode='MarkdownV2')
    return 0


async def backend_post(update, _):
    user_input = update.message.text
    if not user_input:
        return ConversationHandler.END

    await update.message.reply_text('Processing...')

    try:
        resp = rq.post(BACKEND_ENDPOINT.post_uri, data=user_input, timeout=5)
        if resp.status_code != 201:
            await update.message.reply_text('Invalid data submitted, check your input')
            raise Exception(f'Error: status code {resp.status_code}')

        await update.message.reply_text('Successfully added')

    except Exception as e:
        print(e)

    finally:
        return ConversationHandler.END


async def update_conference(update, context):
    uid = update.message.chat.id
    if not db.verify_user(DB_CONF, uid):
        await update.message.reply_text('Not registered, run /start')
        return ConversationHandler.END

    args = context.args
    if len(args) != 1:
        await update.message.reply_text('You need to specify id of the conference you want to update')
        return ConversationHandler.END

    try:
        UPDATE_ID.value = args[0]
    except Exception as e:
        await update.message.reply_text(f'Specified argument must be an int > 0\nFull error: {e}')
        return ConversationHandler.END

    await update.message.reply_text("""
Adding new conference entry  
Specify data as following e g :  
```
{
    "google_spreadsheet": "example",
    "google_drive_directory_id": "example",
    "name_rus": "name",
    "name_rus_short": "short name",
    "registration_start_date": "01.08.2024",
    "registration_end_date": "01.10.2024",
    "submission_start_date": "01.08.2024",
    "submission_end_date": "01.10.2024",
    "conf_start_date": "01.10.2024",
    "conf_end_date": "10.10.2024",
    "organized_by": "SUAI",
    "url": "https://suai.com",
    "email": "suai@gmail.com"
}
```
""", parse_mode='MarkdownV2')
    return 0


async def backend_put(update, context):
    user_input = update.message.text
    if not user_input:
        return ConversationHandler.END

    await update.message.reply_text('Processing...')

    try:
        resp = rq.put(f'{BACKEND_ENDPOINT.put_uri}{UPDATE_ID.value}', data=user_input, timeout=5)
        if resp.status_code != 200:
            await update.message.reply_text('Invalid data submitted, check your input')
            raise Exception(f'Error: status code {resp.status_code}')

        await update.message.reply_text(f'Successfully updated record with id {UPDATE_ID.value}')

    except Exception as e:
        print(e)

    finally:
        return ConversationHandler.END


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
    print(gdrive.get_files(DRIVE_CONF))

    exit(0)

    try:
        app = Application.builder().token(TGCONFIG.token).build()
    except Exception as e:
        print(f'Could not startup the application: {e}')
        exit(1)

    add_conference_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_conference)],
        states={
            0: [
                MessageHandler(
                    filters.ALL,
                    backend_post,
                )
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    update_conference_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('update', update_conference)],
        states={
            0: [
                MessageHandler(
                    filters.ALL,
                    backend_put,
                )
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('get', get_conferences))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(add_conference_conv_handler)
    app.add_handler(update_conference_conv_handler)

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
