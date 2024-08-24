import os

from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class FastApiConfig:
    host: str
    port: int

    def __post_init__(self):
        if self.port.isdigit():
            self.port = int(self.port)


@dataclass
class GoogleSheetsConfig:
    id: str
    list: str


def setup(section, filename='config.ini'):
    return_object = None
    if section == 'fastapi':
        return_object = FastApiConfig

    if section == 'google sheets':
        return_object = GoogleSheetsConfig

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
