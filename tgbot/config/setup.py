import os

from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class TelegramConfig:
    token: str
    section: str = 'telegram bot'

    def __post_init__(self, filename='config.ini'):
        if not os.path.isfile(filename):
            raise Exception('No config.ini file found')

        if self.section is None:
            raise Exception('You did not specify the section to parse')

        parser = ConfigParser()
        parser.read(filename)

        if not parser.has_section(self.section):
            raise Exception(f'File {filename} does not have section {self.section}')

        params = parser.items(self.section)

        try: 
            return self(**{i: k for i, k in params})

        except Exception as e:
            print(e)
            exit(1)

    # def __post_init__(self):
    #     if not self.token:
    #         raise ValueError('Bot token is missing')


@dataclass
class SheetsConfig:
    token: str

    def __post_init__(self):
        if not self.token:
            raise ValueError('Bot token is missing')



def setup(section, filename='config.ini'):
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
        return TelegramConfig(**{i: k for i, k in params})

    except Exception as e:
        print(e)
        exit(1)

