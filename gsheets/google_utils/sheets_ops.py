from google_utils import models
from google_utils import auth
from config.setup import google_sheets
from itertools import 


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


# subroutine to parse data from the spreadsheet
def _extract_values_from_response():
    raise NotImplementedError("Damn")


def _extract_fieldnames_from_response():
    raise NotImplementedError("Damn")


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
    r = SACC.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=f'{LIST}!A1:P').execute()
    if not r:
        print('sheets_ops.get_conference_by_id: Could not retrieve info from the spreadsheet')
        return None

    if not 'valueRanges' in r:
        return None

    values = r.get('valueRanges')[0].get('values', [])
    if not values:
        print('sheets_ops.get_conference_by_id: Values field is null in spreadsheet')
        return None

    field_names = values[0]

    conference_data = None
    for conference in values:
        if conference[0] == conference_id:
            conference_data = conference
            break

    if not conference_data:
        print('sheets_ops.get_conference_by_id: Could not find record with correct id in the spreadsheet')
        return None

    # if len(field_names) != len(conference_data):
    #     print('sheets_ops.get_conference_by_id: Could not zip info')
    #     return None
    
    data = dict(zip(field_names, conference_data))
    print(data)

    return data


def add_conference():
    lr = _get_last_empty_range()
    if not lr:
        print('sheets_ops.add_conference: Could not retrieve last empty row from spreadsheet')
        return None

    body = {
        'values': [
            ['sample', 'title']
        ]
    }

    r = SACC.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=f'{LIST}!B{lr}:P', valueInputOption='RAW', body=body).execute()
    res = r.get('updates', [])
    if not res:
        print('sheets_ops.add_conference: Could not add conference to spreadsheet')
        return None

    return res


def update_conference():
    return None


def h():
    return None
