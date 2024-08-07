from google_utils import auth
from config.setup import google_sheets


SACC = auth.setup_account()
sheets_conf = google_sheets()

SPREADSHEET_ID = sheets_conf.get('id')
LIST = sheets_conf.get('list')
RANGE = sheets_conf.get('range')


def _get_last_empty_range():
    r = SACC.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=f'{LIST}!A2:A').execute()
    if not r:
        return None
    
    if not 'values' in r:
        return None

    return r['values'][-1][0]


def get_all_conferences():
    # return SACC.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=RANGE).execute()
    return _get_last_empty_range()


def add_conference():
    lr = _get_last_empty_range()
    if not lr:
        return None
    
    print(lr)
    return None

    body = {
        'values': [
            ['sample', 'title']
        ]
    }

    r = SACC.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=f'{LIST}!{RANGE}', valueInputOption="RAW", body=body).execute()
    return r


def update_conference():
    return None


def h():
    return None
