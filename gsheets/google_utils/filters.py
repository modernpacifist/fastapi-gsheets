from datetime import datetime
from enum import Enum


def _convert_string_to_datetime(date_str):
    try:
        return datetime.strptime(date_str, '%d.%m.%Y')

    except Exception as e:
        print(e)
        return None


def all_filter(conferences):
    print('all filter called')
    return conferences


def active_filter(conference):
    print('active filter called')
    if conference.id == "1":
        del conference
        return {}
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

    return conference


def past_filter(conferences):
    print('past filter called')
    return 'past_filter'


def future_filter(conferences):
    print('future filter called')
    return 'future_filter'


# FILTERS_ENUM = {
#     'all': all_filter,
#     'active': active_filter,
#     'past': past_filter,
#     'future': future_filter,
# }


class Filters(Enum):
    def __init__(self, filter_name):
        self.filter_name = filter_name

    all: all_filter
    active: active_filter
    past: past_filter
    future: future_filter
