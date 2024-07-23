import os
# import google
import googleapiclient
from google.auth.transport.requests import Request
from google.oauth2.credentials import ServiceAccountCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



def setup_account():
    creds_json  = os.path.dirname(__file__) + './credentials.json'
    print(creds_json)
    # scopes = ['https://www.googleapis.com/auth/spreadsheets']
    # creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    # return build('sheets', 'v4', http=creds_service)
