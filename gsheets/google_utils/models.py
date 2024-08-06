from marshmallow import Schema, fields


class Record(Schema):
    id = fields.Int(required=True)
    users_table_id = fields.Str(required=True)
    google_drive_directory_id = fields.Str(required=True)
    conference_title_full_ru = fields.Str(required=True)
    conference_title_short_ru = fields.Str(required=True)
    conference_title_full_en = fields.Str()
    conference_title_short_en = fields.Str()
    organization_name = fields.Str(required=True)
    applications_opening_date = fields.Date(required=True, format="%d.%m.%Y")
    applications_closing_date = fields.Date(required=True, format="%d.%m.%Y")
    articles_opening_date = fields.Date(required=True, format="%d.%m.%Y")
    articles_closing_date = fields.Date(required=True, format="%d.%m.%Y")
    conference_start_date = fields.Date(required=True, format="%d.%m.%Y")
    conference_end_date = fields.Date(required=True, format="%d.%m.%Y")
    conference_url = fields.URL()
    organizator_email = fields.Str(required=True)
