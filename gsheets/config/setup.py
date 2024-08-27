import os
import httplib2

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class GoogleSheetsConfig:
    id: str
    conferences_list: str
    users_list: str
    sacc: None = None
    fields: None = None

    def __post_init__(self):
        creds_json  = os.path.dirname(__file__) + '/credentials.json'
        scopes = ['https://www.googleapis.com/auth/spreadsheets']

        try:
            creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
            self.sacc = build('sheets', 'v4', http=creds_service)

        except Exception as e:
            print(f'config.setup: could not setup google service account: {e}')
            exit(1)


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
        print(f'config.setup error: {e}')
        exit(1)


# def setup_account():
#     creds_json  = os.path.dirname(__file__) + '/credentials.json'
#     scopes = ['https://www.googleapis.com/auth/spreadsheets']

#     try:
#         creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
#         return build('sheets', 'v4', http=creds_service)

#     except Exception as e:
#         print(f'Problem with setting up google service account: {e}')
#         exit(1)
