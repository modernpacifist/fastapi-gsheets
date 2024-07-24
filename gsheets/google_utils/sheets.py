from google_utils import auth
from config.setup import google_sheets


sacc = auth.setup_account()
conf = google_sheets()

SPREADSHEET_ID = conf.get('id')
RANGE = f"{conf.get('list_id')}!{conf.get('range')}"


def get_all_sheets():
    # return sacc.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
    return sacc.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=RANGE).execute()


def add_conference():
    return None

