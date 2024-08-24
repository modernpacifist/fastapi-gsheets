import os

from configparser import ConfigParser
from dataclasses import dataclass


# CONF_FILENAME = 'config.ini'


# def fastapi(section='fastapi'):
#     if not os.path.isfile(CONF_FILENAME):
#         raise Exception('No config.ini file found')

#     if section is None:
#         raise Exception('You did not specify the section to parse')

#     parser = ConfigParser()
#     parser.read(CONF_FILENAME)

#     config = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for p in params:
#             if p[0] == 'port':
#                 config[p[0]] = int(p[1])
#                 continue
#             config[p[0]] = p[1]

#     if not all(k in config for k in ('host', 'port')):
#         raise Exception(f'Host or port values are not present in {CONF_FILENAME}')

#     return config


# def google_sheets(section='google_sheets'):
#     if not os.path.isfile(CONF_FILENAME):
#         raise Exception('No config.ini file found')

#     if section is None:
#         raise Exception('You did not specify the section to parse')

#     parser = ConfigParser()
#     parser.read(CONF_FILENAME)

#     config = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for p in params:
#             config[p[0]] = p[1]

#     return config


@dataclass
class FastApiConfig:
    host: str
    port: str

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
