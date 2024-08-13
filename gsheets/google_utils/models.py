from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import datetime, date
from typing import Optional


class Conference(BaseModel):
    id: int
    google_spreadsheet: str
    google_drive_directory_id: str
    name_rus: str
    name_rus_short: str
    name_eng: Optional[str] = ""
    name_eng_short: Optional[str] = ""
    organized_by: str
    # registration_start_date: str
    # registration_end_date: str
    # submission_start_date: str
    # submission_end_date: str
    # conf_start_date: str
    # conf_end_date: str
    registration_start_date: datetime
    registration_end_date: datetime
    submission_start_date: datetime
    submission_end_date: datetime
    conf_start_date: datetime
    conf_end_date: datetime
    url: Optional[str] = ""
    email: EmailStr

    @field_validator(
            'registration_start_date',
            'registration_end_date',
            'submission_start_date',
            'submission_end_date',
            'conf_start_date',
            'conf_end_date',
            mode='before')
    def validate_date(cls, v):
        try:
            return datetime.strptime(v, '%d.%m.%Y')
        except ValueError:
            raise ValueError('Incorrect date format')

    def convert_for_spreadsheet(self):
        return list(self.model_dump().values())


class PostConference(Conference):
    id: int = Field(default=0, exclude=True)


class GetConference(Conference):
    id: int = Field(default=0)
    google_spreadsheet: str = Field(default="", exclude=True)
    google_drive_directory_id: str = Field(default="", exclude=True)


class GetConferenceShort(Conference):
    id: str
    name_rus: str = Field(exclude=True)
    name_eng: str = Field(exclude=True)
    google_spreadsheet: str = Field(exclude=True)
    google_drive_directory_id: str = Field(exclude=True)
    organized_by: str = Field(exclude=True)
    registration_start_date: str = Field(exclude=True)
    registration_end_date: str = Field(exclude=True)
    submission_start_date: str = Field(exclude=True)
    submission_end_date: str = Field(exclude=True)
    url: str = Field(exclude=True)
    email: EmailStr = Field(exclude=True)
