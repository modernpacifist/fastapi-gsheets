def get_fields(sacc, spreadsheet_id, spreadsheet_list):
    try:
        r = sacc.spreadsheets().values().batchGet(
            spreadsheetId=spreadsheet_id,
            ranges=f'{spreadsheet_list}!A1:P1').execute()
        value_ranges = r.get('valueRanges', [])
        values = value_ranges[0].get('values', [])
        return values[0]

    except Exception as e:
        print(e)
        return None


def get_last_empty_range(sacc, spreadsheet_id, spreadsheet_list):
    r = sacc.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f'{spreadsheet_list}!A2:A'
    ).execute()
    values = r.get('values', [])
    if not values:
        return 2

    try:
        return int(values[-1][0]) + 2

    except Exception as e:
        print(e)
        return None


def get_conference_row(sacc, spreadsheet_id, spreadsheet_list, conf_id):
    r = sacc.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f'{spreadsheet_list}!A2:P'
    ).execute()
    values = r.get('values', [])
    if not values:
        return 2

    ids = [i[0] for i in values if len(i) > 1]
    if not conf_id in ids:
        return None

    try:
        return int(conf_id) + 1

    except Exception as e:
        print(e)
        return None
