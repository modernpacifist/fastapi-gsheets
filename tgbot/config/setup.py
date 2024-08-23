import os

from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class TelegramConfig:
    token: str


@dataclass
class SheetsConfig:
    uri: str


def setup(section, filename='config.ini'):
    return_object = None
    if section == 'telegram bot':
        return_object = TelegramConfig

    if section == 'sheets':
        return_object = SheetsConfig

    if not return_object:
        raise Exception('No such config available')

    if not os.path.isfile(filename):
        raise Exception('No config.ini file found')

    if section is None:
        raise Exception('You did not specify the section to parse')

    parser = ConfigParser()
    parser.read(filename)

    if not parser.has_section(section):
        raise Exception(f'File {filename} does not have section {section}')

    params = parser.items(section)

    try: 
        return return_object(**{i: k for i, k in params})

    except Exception as e:
        print(e)
        exit(1)

