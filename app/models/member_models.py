import datetime
from mongoengine import Document, StringField, BooleanField, DateField, DateTimeField


class MembersAccount(Document):
    name = StringField(required=True)
    full_name = StringField(required=False)
    username = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    disabled = BooleanField(required=False)
    date_of_birth = DateField(required=False)
    phone_number = StringField(required=False, max_length=20)
    address_line1 = StringField(required=False, max_length=200)
    address_line2 = StringField(required=False, max_length=200)
    city = StringField(required=False, max_length=100)
    state_province_region = StringField(required=False, max_length=100)
    postal_code = StringField(required=False, max_length=20)
    country = StringField(required=False, max_length=50)
    registration_date = DateTimeField(required=True, default=datetime.datetime.utcnow)


