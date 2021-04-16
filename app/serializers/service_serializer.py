from . import ma
from app.models.services import Services


class ServicesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Services

    id = ma.auto_field()
    service_name = ma.auto_field(data_key="service name")
    service_price = ma.auto_field(data_key="service price")
