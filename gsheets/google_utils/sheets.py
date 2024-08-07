from google_utils import auth
from config.setup import google_sheets


SACC = auth.setup_account()
sheets_conf = google_sheets()
print(sheets_conf)

SPREADSHEET_ID = sheets_conf.get('id')
RANGE = f"{sheets_conf.get('list_id')}!{sheets_conf.get('range')}"


def get_all_conferences():
    return SACC.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=RANGE).execute()


def add_conference():
    body = {
        'values': [
            ['sample', 'title'],
        ]
    }
    r = SACC.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE, insertDataOption="INSERT_ROWS", valueInputOption="RAW", body=body).execute()
    return r


def update_conference():
    return None


def h():
    return None
