from telegram.ext import (
    Application,
    CommandHandler   
)

from config import setup


def start():



def main():
    try:
        tgconfig = setup.setup()
        app = Application.builder().token(tgconfig.token).build()
    except Exception as e:
        print(e)
        exit(1)

    app.add_handler(CommandHandler('start', start))

    app.run_polling()


if __name__ == '__main__':
    main()