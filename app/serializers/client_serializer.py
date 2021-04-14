from . import ma
from app.models.client import Client


class ClientSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Client

    id = ma.auto_field()
    name = ma.auto_field()
    phone_number = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()