from . import ma
from app.models.appointments import Appointments


class AppointmentsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Appointments

    id = ma.auto_field()
    barber_id = ma.auto_field()
    barber_shop_id = ma.auto_field()
    services_id = ma.auto_field()
    client_id = ma.auto_field()
    date_time = ma.auto_field()