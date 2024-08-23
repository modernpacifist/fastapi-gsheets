from telegram.ext import (
    Application
)

from config import setup


def main():
    try:
        tgconfig = setup.setup()
        tgconfig.token
        # app = Application.builder().token(TleegramConfig.pseudo_init()).build()
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()