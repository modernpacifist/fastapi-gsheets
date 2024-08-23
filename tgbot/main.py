from telegram.ext import (
    Application,
    CommandHandler   
)

from config.setup import TelegramConfig, SheetsConfig


# TGCONFIG = TelegramConfig.setup()
TGCONFIG = TelegramConfig()
# SHEETS_ENDPOINT = setup.setup(section='backend')


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

    app.run_polling()


if __name__ == '__main__':
    main()