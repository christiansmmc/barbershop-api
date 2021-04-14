from . import ma
from app.models.barber_shop_model import Barber_shop


class BarberSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Barber_shop

    id = ma.auto_field()
    name = ma.auto_field()
    phone_number = ma.auto_field()
    cnpj = ma.auto_field()
    email = ma.auto_field()
