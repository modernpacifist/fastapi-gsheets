import os

from configparser import ConfigParser
from dataclasses import dataclass


CONF_FILENAME = 'config.ini'


class TelegramConfig:
    token: str
    section='telegram bot'

    def __post_init__(self):
        if not self.token:
            raise ValueError('Bot token is missing')

# ^
# |
# | must return this type
# |
# |
# |

def setup(section='telegram bot'):
    if not os.path.isfile(CONF_FILENAME):
        raise Exception('No config.ini file found')

    if section is None:
        raise Exception('You did not specify the section to parse')

    parser = ConfigParser()
    parser.read(CONF_FILENAME)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for p in params:
            config[p[0]] = p[1]

    return config
