from google_utils import auth


sacc = auth.setup_account()


def get_all_sheets():
    return str(sacc)
