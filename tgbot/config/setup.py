import os

from configparser import ConfigParser


CONF_FILENAME = 'config.ini'


def fastapi(section='fastapi'):
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
            if p[0] == 'port':
                config[p[0]] = int(p[1])
                continue
            config[p[0]] = p[1]

    if not all(k in config for k in ('host', 'port')):
        raise Exception(f'Host or port values are not present in {CONF_FILENAME}')

    return config
