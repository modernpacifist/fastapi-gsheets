from telegram.ext import (
    Application
)

from config import TelegramConfig


def main():
    try:
        app = Application.builder().token(TleegramConfig.pseudo_init()).build()
    except Exception as e:
        print(e)
        exit(1)