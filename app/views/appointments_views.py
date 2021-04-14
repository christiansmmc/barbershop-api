from flask import Blueprint,request

from app.models.appointments import Appointments

bp_appointments = Blueprint("appointments_views", __name__, url_prefix="/appointments")


@bp_appointments.route('/<int:barbershop_id>', methods=['GET'], )
def all_appointments(barbershop_id):
    query = f"""SELECT * FROM appointments WHERE barber_id = {str(barbershop_id)}"""

    return str(barbershop_id),201

@bp_appointments.route('/<int:barbershop_id>/<int:barber_id>', methods=['GET'])
def barber_appointments(barbershop_id, barber_id):
    ...

@bp_appointments.route('/', methods=['POST'])
def create_appointment():
    session = current_app.db_session

    data = request.get_json()

    appointment = Appointments(
        barber_id=data['barber_id'],
        services_id=data['services_id'],
        client_id=data['client_id'],
        date_time=data['date_time']
    )

    session.add(appointments)
    session.commit()

    return {'barber_id'}

@bp_appointments.route('/', methods=['PATCH'])
def update_appointment():
    ...

@bp_appointments.route('/', methods=['DELETE'])
def del_appointment():
    ...