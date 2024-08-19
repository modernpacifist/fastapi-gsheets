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