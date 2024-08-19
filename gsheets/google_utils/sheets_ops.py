from google_utils import models, auth
from google_utils.filters import ConferencesFilter
from config.setup import google_sheets
from itertools import zip_longest


SACC = auth.setup_account()
sheets_conf = google_sheets()

SPREADSHEET_ID = sheets_conf.get('id')
LIST = sheets_conf.get('list')


def get_all_conferences(filter_type):
    r = SACC.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=f'{LIST}!A1:P').execute()
    if not r:
        return None

    if not 'valueRanges' in r:
        return None

    values = r.get('valueRanges')[0].get('values', [])
    if not values:
        return None

    field_names = values[0]
    conferences = []
    for conference_data in values[1:]:
        dict_data = dict(zip_longest(field_names, conference_data, fillvalue=''))
        # conferences.append(models.GetConferenceShort.model_construct(**dict_data))
        dict_data['registration_start_date'] = datetime
        conferences.append(models.GetConferenceShort.model_validate(dict_data))
        print(dict_data)
        break

    print(type(conferences[0]))
    print(conferences[0])
    print(conferences[0].registration_start_date)
    print(type(conferences[0].registration_start_date))

    return ConferencesFilter(filter_type, conferences).exec()


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

    dict_data = dict(zip_longest(field_names, conference_data, fillvalue=''))

    try:
        return models.GetConference.model_construct(**dict_data)

    except Exception as e:
        print(f'sheets_ops.get_conference_by_id: {e}')
        return None


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


def add_conference(model):
    lr = _get_last_empty_range()
    if not lr:
        print('sheets_ops.add_conference: Could not retrieve last empty row from spreadsheet')
        return None

    body = {
        'values': [
            model.convert_for_spreadsheet()
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
