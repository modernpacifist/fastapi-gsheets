from google_utils import models, auth, utils
from google_utils.filters import ConferencesFilter
from config.setup import google_sheets
from itertools import zip_longest


SACC = auth.setup_account()
sheets_conf = google_sheets()

SPREADSHEET_ID = sheets_conf.get('id')
LIST = sheets_conf.get('list')
FIELDS = utils.get_fields(SACC, SPREADSHEET_ID, LIST)


def get_all_conferences(filter_type):
    r = SACC.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f'{LIST}!A2:P'
    ).execute()
    if not r:
        return None

    values = r.get('values', [])
    if not values:
        return None

    conferences = []
    for conference_data in values:
        try:
            dict_data = dict(zip_longest(FIELDS, conference_data, fillvalue=''))
            utils.dict_string_to_datetime(dict_data, 'registration_start_date', 'registration_end_date')
            conferences.append(models.GetConferenceShort.model_validate(dict_data))

        except Exception as e:
            print(e)
            continue

    return ConferencesFilter(filter_type, conferences).exec()


def get_conference_by_id(conference_id):
    r = SACC.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f'{LIST}!A2:P'
    ).execute()
    if not r:
        print('sheets_ops.get_conference_by_id: Could not retrieve info from the spreadsheet')
        return None

    values = r.get('values', [])
    if not values:
        print('sheets_ops.get_conference_by_id: Values field is null in spreadsheet')
        return None

    conference_data = None
    for conference in values:
        if conference[0] == conference_id:
            conference_data = conference
            break

    if not conference_data:
        print('sheets_ops.get_conference_by_id: Could not find record with correct id in the spreadsheet')
        return None

    try:
        dict_data = dict(zip_longest(FIELDS, conference_data, fillvalue=''))
        return models.GetConference.model_validate(dict_data)

    except Exception as e:
        print(f'sheets_ops.get_conference_by_id: {e}')
        return None


def add_conference(model):
    lr = utils.get_last_empty_range(SACC, SPREADSHEET_ID, LIST)
    if not lr:
        print('sheets_ops.add_conference: Could not retrieve last empty row from spreadsheet')
        return None

    body = {
        'values': [
            model.convert_for_spreadsheet()
        ]
    }

    r = SACC.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=f'{LIST}!B{lr}:P',
        valueInputOption='RAW',
        body=body
    ).execute()

    updates = r.get('updates', [])
    if not updates:
        print('sheets_ops.add_conference: Could not add conference to spreadsheet')
        return None

    if updates.get('updatedRows', 0) < 1:
        return None

    return model


def update_conference(conference_id, model):
    cr = utils.get_conference_row(SACC, SPREADSHEET_ID, LIST, conference_id)
    if not cr:
        return -1

    body = {
        'values': [
            model.convert_for_spreadsheet()
        ]
    }

    r = SACC.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=f'{LIST}!B{cr}:P{cr}',
        valueInputOption='RAW',
        body=body
    ).execute()
    if not r:
        return None

    if r.get('updatedRows') < 1:
        return None

    r = SACC.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f'{LIST}!A{cr}:P{cr}'
    ).execute()

    conference_data = r.get('values', [])
    if not conference_data:
        return None

    try:
        dict_data = dict(zip_longest(FIELDS, conference_data[0], fillvalue=''))
        return models.UpdateConference.model_validate(dict_data)

    except Exception as e:
        print(e)
        return None
