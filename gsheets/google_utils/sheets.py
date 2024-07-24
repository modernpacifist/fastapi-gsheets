from google_utils import auth
from config.setup import google_sheets


sacc = auth.setup_account()
conf = google_sheets()

SPREADSHEET_ID = conf.get('id')
RANGE = f"{conf.get('list_id')}!{conf.get('range')}"


def get_all_conferences():
    return sacc.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=RANGE).execute()


def add_conference():
    body = {
        'values': [
            ['1', 'name', 'title']
        ]
    }
    r = sacc.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE, valueInputOption="RAW", body=body).execute()
    return r


def update_conference():
    return None


def h():
    return None