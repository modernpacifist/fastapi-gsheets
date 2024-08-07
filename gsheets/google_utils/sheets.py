from google_utils import auth
from config.setup import google_sheets


SACC = auth.setup_account()
sheets_conf = google_sheets()

SPREADSHEET_ID = sheets_conf.get('id')
RANGE = sheets_conf.get('range')


def get_all_conferences():
    return SACC.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=RANGE).execute()


def add_conference():
    body = {
        'values': [
            ['sample', 'title'],
        ]
    }
    # r = SACC.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range="main!B:P", insertDataOption="INSERT_ROWS", valueInputOption="RAW", body=body).execute()
    # r = SACC.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE, insertDataOption="INSERT_ROWS", valueInputOption="RAW", body=body).execute()
    r = SACC.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE, valueInputOption="RAW", body=body).execute()
    return r


def update_conference():
    return None


def h():
    return None
