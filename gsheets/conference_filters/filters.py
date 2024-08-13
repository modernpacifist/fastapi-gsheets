from datetime import datetime


def _convert_string_to_datetime(date_str):
    try:
        return datetime.strptime(date_str, '%d.%m.%Y')

    except Exception as e:
        print(e)
        return ""


def active_filter(conferences):
    # converted_date = _convert_string_to_datetime(x.conf_start_date)
    # if not converted_date:
    #     return 
    return sorted(conferences, key=lambda x: _convert_string_to_datetime(x.conf_start_date))


def past_filter(conferences):
    return 'past_filter'


def future_filter(conferences):
    return 'future_filter'
