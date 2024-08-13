from datetime import datetime


def _convert_string_to_datetime(date_str):
    return datetime.strptime(date_str, '%d.%m.%Y')


def active_filter(conferences):
    # return sorted(conferences, key=lambda x: _convert_string_to_datetime(x['conf_start_date']))
    return sorted(conferences, key=lambda x: _convert_string_to_datetime(x.conf_start_date))


def past_filter(conferences):
    return 'past_filter'


def future_filter(conferences):
    return 'future_filter'
