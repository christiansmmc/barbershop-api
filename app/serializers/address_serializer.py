from . import ma
from app.models.address import Address


class AddressSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Address

    id = ma.auto_field()
    state = ma.auto_field()
    city = ma.auto_field()
    street_name = ma.auto_field()
    building_number = ma.auto_field()
    zip_code = ma.auto_field()