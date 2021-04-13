from flask import Blueprint

bp_appointments = Blueprint("appointments_views", __name__, url_prefix="/appointments")


@bp_appointments.route('/<int:barbershop_id>', methods=['GET'], )
def all_appointments(barbershop_id):
    # query = f"""SELECT * FROM appointments WHERE barber_id = {str(barbershop_id)}"""

    return str(barbershop_id),201

@bp_appointments.route('/<int:barbershop_id>/<int:barber_id>', methods=['GET'])
def barber_appointments(barbershop_id, barber_id):
    ...

@bp_appointments.route('/', methods=['POST'])
def create_appointment():
    ...

@bp_appointments.route('/', methods=['PATCH'])
def update_appointment():
    ...

@bp_appointments.route('/', methods=['DELETE'])
def del_appointment():
    ...