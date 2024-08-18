from datetime import datetime
from enum import Enum


def _convert_string_to_datetime(date_str):
    try:
        return datetime.strptime(date_str, '%d.%m.%Y')

    except Exception as e:
        print(e)
        return None


def _all_filter(conferences):
    print('all filter called')
    return conferences


def _active_filter(conferences):
    print('active filter called')

    res = []
    for conference in conferences:
        print(conference)
        if conference.id == "1":
            continue
        res.append(conference)

    # for i in conferences:
    #     print(i.model_dump())
    #     print(i)
    #     break
    # converted_date = _convert_string_to_datetime(x.conf_start_date)
    # if not converted_date:
    #     return 
    # return sorted(conferences, key=lambda x: _convert_string_to_datetime(x.conf_start_date))
    # res = []
    # for conf in conferences:
    #     if conf.
    #         res.append(conf)

    return res


def _past_filter(conferences):
    print('past filter called')
    return 'past_filter'


def _future_filter(conferences):
    print('future filter called')
    return 'future_filter'


FILTERS_ENUM = {
    'all': _all_filter,
    'active': _active_filter,
    'past': _past_filter,
    'future': _future_filter,
}
