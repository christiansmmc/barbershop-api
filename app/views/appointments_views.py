from flask import Blueprint,request, current_app
from flask_jwt_extended import jwt_required, get_jwt

from app.models.appointments import Appointments
from app.serializers.appointments_serializer import AppointmentsSchema
from http import HTTPStatus



bp_appointments = Blueprint("appointments_views", __name__, url_prefix="/appointments")

@bp_appointments.route('/<int:barbershop_id>', methods=['GET'], )
def all_barbershop_appointments(barbershop_id):
    result = Appointments.query.filter_by(barber_shop_id=barbershop_id).all()
    serialized = AppointmentsSchema().dump(result)
    return str(result), 200

@bp_appointments.route('/<int:barbershop_id>/<int:id_barber>', methods=['GET'])
def barber_appointments(barbershop_id, id_barber):
    result = Appointments.query.filter_by(barber_shop_id=barbershop_id, barber_id=id_barber).all()
    # result = Appointments.query.filter_by(barber_shop_id=barbershop_id).filter_by(barber_id=id_barber).all()
    serialized = AppointmentsSchema().dump(result)
    return str(result), 200

@bp_appointments.route('/', methods=['POST'])
def create_appointment():
    session = current_app.db.session

    data = request.get_json()

    appointment = Appointments(
        barber_id=data['barber_id'],
        barber_shop_id=data['barber_shop_id'],
        services_id=data['services_id'],
        client_id=data['client_id'],
        date_time=data['date_time']
    )

    session.add(appointment)
    session.commit()

    return {"date_time": appointment.date_time}, HTTPStatus.CREATED

# @bp_appointments.route('/', methods=['PATCH'])
# def update_appointment():
#     ...

@bp_appointments.route('/delete', methods=['DELETE'])
@jwt_required()
def del_appointment():
    current_user = get_jwt()

    if (
        current_user["user_id"] == barber_shop_id
        and current_user["user_type"] == "barber_shop"
    ):
        session = current_app.db.session
        Appointments.query.filter_by(id=barber_shop_id).delete()
        session.commit()

    else:
        return {"Data": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED

    return {}, HTTPStatus.NO_CONTENT
    