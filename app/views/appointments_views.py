from flask import Blueprint

bp_appointments = Blueprint("appointments_views", __name__)

@bp_appointments.route('/appointments/<barbershop_id:int>', methods=['GET'])
def all_appointments(barbershop_id):
    ...

@bp_appointments.route('/appointments/<barbershop_id:int>/<barber_id:int>', methods=['GET'])
def barber_appointments(barbershop_id, barber_id):
    ...

@bp_appointments.route('/appointments', methods=['POST'])
def create_appointment():
    ...

@bp_appointments.route('/appointments', methods=['PATCH'])
def update_appointment():
    ...

@bp_appointments.route('/appointments', methods=['DELETE'])
def del_appointment():
    ...