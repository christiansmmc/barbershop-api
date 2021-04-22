from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required, get_jwt

from app.models.appointments import Appointments
from app.models.services import Services
from app.models.client import Client
from app.models.barbers import Barbers
from app.models.barber_shop_model import Barber_shop
from app.serializers.appointments_serializer import AppointmentsSchema

from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt


bp_appointments = Blueprint("appointments_views", __name__, url_prefix="/appointments")


@bp_appointments.route(
    "/barbershop/<int:barbershop_id>",
    methods=["GET"],
)
def all_barbershop_appointments(barbershop_id):
    all_appointments = Appointments.query.filter_by(barber_shop_id=barbershop_id).all()
    
    result_list = []

    for appointment in all_appointments:
        appointment_data = {}
        client = {}
        current_client = Client.query.filter_by(id=appointment.client_id).first()
        client["id"] = current_client.id
        client["name"] = current_client.name
        client["phone_number"] = current_client.phone_number

        service = {}
        current_service = Services.query.filter_by(id=appointment.services_id).first()
        service["id"] = current_service.id
        service["service_name"] = current_service.service_name
        service["service_price"] = current_service.service_price

        barber = {}
        current_barber = Barbers.query.filter_by(id=appointment.barber_id).first()
        barber["id"] = current_barber.id
        barber["name"] = current_barber.name

        appointment_data["client"] = client
        appointment_data["service"] = service
        appointment_data["barber"] = barber
        appointment_data["date_time"] = appointment.date_time
        result_list.append(appointment_data)

    return {"data": result_list}, HTTPStatus.OK


@bp_appointments.route("/barbershop/<int:barbershop_id>/<int:id_barber>", methods=["GET"])
def barber_appointments(barbershop_id, id_barber):
    all_appointments = Appointments.query.filter_by(
        barber_shop_id=barbershop_id, barber_id=id_barber
    ).all()

    result_list = []

    for appointment in all_appointments:
        appointment_data = {}
        client = {}
        current_client = Client.query.filter_by(id=appointment.client_id).first()
        client["id"] = current_client.id
        client["name"] = current_client.name
        client["phone_number"] = current_client.phone_number

        service = {}
        current_service = Services.query.filter_by(id=appointment.services_id).first()
        service["id"] = current_service.id
        service["service_name"] = current_service.service_name
        service["service_price"] = current_service.service_price

        appointment_data["client"] = client
        appointment_data["service"] = service
        appointment_data["date_time"] = appointment.date_time
        result_list.append(appointment_data)

    return {"data": result_list}, HTTPStatus.OK


@bp_appointments.route("/client/<int:client_id>", methods=["GET"])
@jwt_required()
def client_appointments(client_id):
    current_user = get_jwt()
    
    if current_user["user_id"] == client_id and current_user["user_type"] == "client":     
        all_appointments = Appointments.query.filter_by(client_id=client_id).all()

        result_list = []

        for appointment in all_appointments:
            appointment_data = {}
            barber = {}
            current_barbershop: Barber_shop = Barber_shop.query.filter_by(id=appointment.barber_shop_id).first()
            current_barber = Barbers.query.filter_by(id=appointment.barber_id).first()
            barber["id"] = current_barber.id
            barber["name"] = current_barber.name

            service = {}
            current_service = Services.query.filter_by(id=appointment.services_id).first()
            service["id"] = current_service.id
            service["service_name"] = current_service.service_name
            service["service_price"] = current_service.service_price
            
            appointment_data["appointment_id"] = appointment.id
            appointment_data["barbershop"] = current_barbershop.name
            appointment_data["barber"] = barber
            appointment_data["service"] = service
            appointment_data["date_time"] = appointment.date_time
            result_list.append(appointment_data)

        return {"data": result_list}, HTTPStatus.OK
    
    else:
        return {
                "error": "You don't have permission to do this"
            }, HTTPStatus.UNAUTHORIZED


@bp_appointments.route("", methods=["POST"])
@jwt_required()
def create_appointment():
    try:
        current_user = get_jwt()
        data = request.get_json()

        if current_user["user_type"] == "client":
            session = current_app.db.session

            result = Services.query.filter_by(id=data["services_id"]).first()
            barber_shop = Barber_shop.query.filter_by(id=data["services_id"]).first()
            barber = Barbers.query.filter_by(id=data["services_id"]).first()
    
            appointment = Appointments(
                barber_id=data["barber_id"],
                barber_shop_id=data["barber_shop_id"],
                services_id=data["services_id"],
                client_id=current_user["user_id"],
                date_time=data["date_time"],
            )
    
            session.add(appointment)
            session.commit()
    
            return {
                "data": {
                    "date": appointment.date_time,
                    "service": result.service_name,
                    "price": result.service_price,
                    "barber_shop": barber_shop.name,
                    "barber": barber.name
                }
            }, HTTPStatus.CREATED

        else:
            return {
                "data": "You don't have permission to do this"
            }, HTTPStatus.UNAUTHORIZED
    except KeyError:
        return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST


@bp_appointments.route("/<int:appointment_id>", methods=["PATCH"])
@jwt_required()
def update_appointment(appointment_id):
    current_user = get_jwt()
    body = request.get_json()
    session = current_app.db.session
    result = Appointments.query.filter_by(id=appointment_id).first()

    if result:

        if (
            current_user["user_id"] == result.client_id
            and current_user["user_type"] == "client"
        ):

            current_appointment: Appointments = Appointments.query.get(appointment_id)

            if body.get("date_time"):

                date_time = body.get("date_time")

                current_appointment.date_time = date_time

                session.add(current_appointment)
                session.commit()

                return {"data": date_time}, HTTPStatus.OK

            else:
                return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST

        else:
            return {
                "data": "You don't have permission to do this"
            }, HTTPStatus.UNAUTHORIZED

    return {"msg": "Wrong appointment ID"}, HTTPStatus.BAD_REQUEST


@bp_appointments.route("/<int:appointment_id>", methods=["DELETE"])
@jwt_required()
def del_appointment(appointment_id):
    session = current_app.db.session

    current_user = get_jwt()
    result = Appointments.query.filter_by(id=appointment_id).first()

    if (
        current_user["user_id"] == result.client_id
        and current_user["user_type"] == "client"
    ):
        Appointments.query.filter_by(id=appointment_id).delete()
        session.commit()

    else:
        return {"data": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED

    return {}, HTTPStatus.NO_CONTENT