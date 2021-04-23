from . import ma
from app.models.barbers import Barbers


class BarbersSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Barbers

    id = ma.auto_field()
    name = ma.auto_field(data_key="barber_name")
