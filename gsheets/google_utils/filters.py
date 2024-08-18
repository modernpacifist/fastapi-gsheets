from datetime import datetime


def _convert_string_to_datetime(date_str):
    try:
        return datetime.strptime(date_str, '%d.%m.%Y')

    except Exception as e:
        print(e)
        return None


def all_filter(conferences):
    return conferences


def active_filter(conferences):
    for i in conferences:
        print(i.model_dump())
        print(i)
        break
    # converted_date = _convert_string_to_datetime(x.conf_start_date)
    # if not converted_date:
    #     return 
    # return sorted(conferences, key=lambda x: _convert_string_to_datetime(x.conf_start_date))
    # res = []
    # for conf in conferences:
    #     if conf.
    #         res.append(conf)

    return conferences


def past_filter(conferences):
    return 'past_filter'


def future_filter(conferences):
    return 'future_filter'
