from marshmallow import Schema, fields


class Record(Schema):
    id = fields.Int()
    id_str = fields.Str()
    google_drive_directory = fields.Str()
    conference_title_full_ru = fields.Str()
    conference_title_short_ru = fields.Str()
    conference_title_full_en = fields.Str()
    conference_title_short_en = fields.Str()
    organization_name = fields.Str()
    applications_opening_date = fields.Date(format="%d.%m.%Y")
    applications_closing_date = fields.Date(format="%d.%m.%Y")
    articles_opening_date = fields.Date(format="%d.%m.%Y")
    articles_closing_date = fields.Date(format="%d.%m.%Y")
    conference_start_date = fields.Date(format="%d.%m.%Y")
    conference_end_date = fields.Date(format="%d.%m.%Y")
    conference_url = fields.URL()
    organizator_email = fields.Str()
