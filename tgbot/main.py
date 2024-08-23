from telegram.ext import (
    Application,
    CommandHandler   
)

from config.setup import setup


# TGCONFIG = TelegramConfig.setup()
TGCONFIG = setup('telegram bot')
SHEETS_ENDPOINT = setup('sheets')


async def start(update, context):
    uid = update.message.chat.id
    uname = update.message.chat.first_name
    print(uid, uname)


def main():
    try:
        app = Application.builder().token(TGCONFIG.token).build()
    except Exception as e:
        print(e)
        exit(1)

    app.add_handler(CommandHandler('start', start))

    try:
        app.run_polling()
        print('application started')
    except KeyboardInterrupt:
        print('Exited by user')
        exit(0)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()