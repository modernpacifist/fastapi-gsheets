import os
import httplib2

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def setup_account():
    creds_json  = os.path.dirname(__file__) + '/credentials.json'
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)
