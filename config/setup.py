import os

from configparser import ConfigParser
from dataclasses import dataclass, field


@dataclass
class TelegramConfig:
    token: str


@dataclass
class BackendConfig:
    uri: str
    get_uri: str = field(init=False)
    post_uri: str = field(init=False)
    put_uri: str = field(init=False)

    def __post_init__(self):
        self.get_uri = f'http://{self.uri}/conferences'
        self.get_single_uri = f'http://{self.uri}/conferences/'
        self.post_uri = f'http://{self.uri}/conferences'
        self.put_uri = f'http://{self.uri}/conferences/'


@dataclass
class GoogleSheetsConfig:
    id: str
    list: str


@dataclass
class FastApiConfig:
    host: str
    port: int

    def __post_init__(self):
        if self.port.isdigit():
            self.port = int(self.port)


def setup(section, filename='config.ini'):
    return_object = None
    parser = ConfigParser()
    parser.read(filename)

    if not section:
        raise Exception('Section you specified is invalid')

    if not parser.has_section(section):
        raise Exception(f'File {filename} does not have section {section}')

    if section == 'telegram bot':
        return_object = TelegramConfig

    if section == 'backend':
        return_object = BackendConfig

    if section == 'google sheets':
        return_object = GoogleSheetsConfig

    if section == 'fastapi':
        return_object = FastApiConfig

    if not os.path.isfile(filename):
        raise Exception('No config.ini file found')

    params = parser.items(section)

    try: 
        return return_object(**{i: k for i, k in params})

    except Exception as e:
        print(e)
        exit(1)
