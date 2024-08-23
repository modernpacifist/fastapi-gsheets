import os

from configparser import ConfigParser
from dataclasses import dataclass, asdict


# CONF_FILENAME = 'config.ini'


@dataclass
class TelegramConfig:
    token: str
    # section='telegram bot'

    def __post_init__(self):
        if not self.token:
            raise ValueError('Bot token is missing')

# ^
# |
# | must return this type
# |
# |
# |

def setup(filename='config.ini', section='telegram bot'):
    if not os.path.isfile(filename):
        raise Exception('No config.ini file found')

    if section is None:
        raise Exception('You did not specify the section to parse')

    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if not parser.has_section(section):
        raise Exception(f'File {filename} does not have ')

    params = parser.items(section)
    print(params)
        # for p in params:
        #     config[p[0]] = p[1]

    return config
