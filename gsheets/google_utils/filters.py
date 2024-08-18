from dataclasses import dataclass
from datetime import datetime
from enum import Enum


def _convert_string_to_datetime(date_str):
    try:
        return datetime.strptime(date_str, '%d.%m.%Y')

    except Exception as e:
        print(e)
        return None


@dataclass
class Filters:
    filter_type: str
    conferences: list
    f: callable = None

    def _all_filter(self):
        return self.conferences

    def _active_filter(self):
        res = []
        for conference in self.conferences:
            conference_reg_start = _convert_string_to_datetime(conference.registration_start_date)
            conference_reg_end = _convert_string_to_datetime(conference.registration_end_date)
            if not all([conference_reg_start, conference_reg_end]):
                continue
            if conference_reg_start < datetime.now() and datetime.now() < conference_reg_end:
                res.append(conference)
        return res

    def _past_filter(self):
        res = []
        for conference in self.conferences:
            conference_reg_end = _convert_string_to_datetime(conference.registration_end_date)
            if not conference_reg_end:
                continue
            if datetime.now() > conference_reg_end:
                res.append(conference)
        return res

    def _future_filter(self):
        res = []
        for conference in self.conferences:
            conference_reg_start = _convert_string_to_datetime(conference.registration_start_date)
            if not conference_reg_start:
                continue
            if conference_reg_start > datetime.now():
                res.append(conference)
        return res

    def exec(self):
        return self.f()

    def __post_init__(self):
        self.f = {
            'all': self._all_filter,
            'active': self._active_filter,
            'past': self._past_filter,
            'future': self._future_filter,
        }.get(self.filter_type)
