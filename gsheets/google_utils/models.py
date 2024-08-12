from abc import abstractmethod
from marshmallow import Schema, fields
from pydantic import BaseModel, Field, HttpUrl, EmailStr, field_validator, field_serializer
from datetime import datetime, date
from typing import Optional


# class Record(Schema):
#     id = fields.Int(required=True)
#     users_table_id = fields.Str(required=True)
#     google_drive_directory_id = fields.Str(required=True)
#     conference_title_full_ru = fields.Str(required=True)
#     conference_title_short_ru = fields.Str(required=True)
#     conference_title_full_en = fields.Str()
#     conference_title_short_en = fields.Str()
#     organization_name = fields.Str(required=True)
#     applications_opening_date = fields.Date(required=True, format="%d.%m.%Y")
#     applications_closing_date = fields.Date(required=True, format="%d.%m.%Y")
#     articles_opening_date = fields.Date(required=True, format="%d.%m.%Y")
#     articles_closing_date = fields.Date(required=True, format="%d.%m.%Y")
#     conference_start_date = fields.Date(required=True, format="%d.%m.%Y")
#     conference_end_date = fields.Date(required=True, format="%d.%m.%Y")
#     conference_url = fields.URL()
#     organizator_email = fields.Str(required=True)


class GetConference(Schema):
    id = fields.Int(required=True)
    name_rus = fields.Str(required=True)
    name_rus_short = fields.Str(required=True)
    name_eng = fields.Str()
    name_eng_short = fields.Str()
    registration_start_date = fields.Date(required=True, format="%d.%m.%Y")
    registration_end_date = fields.Date(required=True, format="%d.%m.%Y")
    submission_start_date = fields.Date(required=True, format="%d.%m.%Y")
    submission_end_date = fields.Date(required=True, format="%d.%m.%Y")
    conf_start_date = fields.Date(required=True, format="%d.%m.%Y")
    conf_end_date = fields.Date(required=True, format="%d.%m.%Y")
    organized_by = fields.Str(required=True)
    url = fields.URL()
    email = fields.Email(required=True)


class ConferenceInfo(BaseModel):
    id: int
    google_spreadsheet: str
    google_drive_directory_id: str
    name_rus: str
    name_rus_short: str
    name_eng: Optional[str] = ""
    name_eng_short: Optional[str] = ""
    organized_by: str
    registration_start_date: str
    registration_end_date: str
    submission_start_date: str
    submission_end_date: str
    conf_start_date: str
    conf_end_date: str
    url: Optional[str] = ""
    email: EmailStr

    @abstractmethod
    def convert_to_list(self):
        raise NotImplementedError()


class PostConference(ConferenceInfo):
    id: int = Field(default=0, exclude=True)

    @field_validator(
            'registration_start_date',
            'registration_end_date',
            'submission_start_date',
            'submission_end_date',
            'conf_start_date',
            'conf_end_date')
    def validate_date(cls, v):
        try:
            datetime.strptime(v, '%d.%m.%Y')
        except ValueError:
            raise ValueError('Incorrect date format')
        return v

    def convert_to_list(self):
        return list(self.model_dump().values())


class GetConferenceShort(Schema):
    id = fields.Int(required=True)
    name_rus_short = fields.Str(required=True)
    name_end_short = fields.Str()
    conf_start_date = fields.Date(required=True, format="%d.%m.%Y")
    conf_end_date = fields.Date(required=True, format="%d.%m.%Y")
