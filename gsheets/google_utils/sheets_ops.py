from google_utils import models
from google_utils import auth
from config.setup import google_sheets


SACC = auth.setup_account()
sheets_conf = google_sheets()

SPREADSHEET_ID = sheets_conf.get('id')
LIST = sheets_conf.get('list')
# RANGE = sheets_conf.get('range')


def _get_last_empty_range():
    r = SACC.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=f'{LIST}!A2:A').execute()
    values = r.get('values', [])
    if not values:
        return 2

    try:
        return int(values[-1][0]) + 2

    except Exception as e:
        print(e)
        return None


def get_all_conferences():
    r = SACC.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=f'{LIST}!A2:P').execute()
    if not r:
        return None

    if not 'valueRanges' in r:
        return None

    values = r.get('valueRanges')[0].get('values', [])
    if not values:
        return None

    return values


def get_conference_by_id(conference_id):
    r = SACC.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=f'{LIST}!A2:P').execute()
    if not r:
        return None

    if not 'valueRanges' in r:
        return None

    values = r.get('valueRanges')[0].get('values', [])
    if not values:
        return None

    # print(values)
    for record in values:
        if record[0] == conference_id:
            print(record)
            return values
            # continue
        

    return values


def add_conference():
    lr = _get_last_empty_range()
    if not lr:
        print('sheets.add_conference: Could not retrieve last empty row from spreadsheet')
        return None

    body = {
        'values': [
            ['sample', 'title']
        ]
    }

    r = SACC.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=f'{LIST}!B{lr}:P', valueInputOption="RAW", body=body).execute()
    res = r.get('updates', [])
    if not res:
        print('sheets.add_conference: Could not add conference to spreadsheet')
        return None

    return res


def update_conference():
    return None


def h():
    return None
