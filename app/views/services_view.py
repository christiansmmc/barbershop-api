from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.services import Services
from app.models.barbers import Barbers
from app.models.barber_shop_model import Barber_shop
from flask_jwt_extended import jwt_required, get_jwt
from app.serializers.service_serializer import ServicesSchema

bp_services = Blueprint("bp_services", __name__, url_prefix="/services")


@bp_services.route("/<int:barber_id>", methods=["POST"])  #
@jwt_required()
def register_services(barber_id):
    try:
        session = current_app.db.session
        current_user = get_jwt()
        body = request.get_json()
        get_barber: Barbers = Barbers.query.filter_by(id=barber_id).first()

        if (
            current_user["user_id"] == get_barber.barber_shop_id
            and current_user["user_type"] == "barber_shop"
        ):
            if "services" in body:
                for service in body["services"]:
                    new_service: Services = Services(
                        service_name=service["service_name"],
                        service_price=service["service_price"],
                    )

                    get_barber.service_list.append(new_service)

                session.add(get_barber)
                session.commit()

                services_serialized = [
                    ServicesSchema().dump(s) for s in get_barber.service_list
                ]

                return {
                    "data": {
                        "barber_name": get_barber.name,
                        "service": services_serialized,
                    }
                }

            else:
                return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST

        else:
            return {
                "msg": "You don't have permission to do this"
            }, HTTPStatus.UNAUTHORIZED

    except KeyError:
        return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST


@bp_services.route("/<int:service_id>", methods=["DELETE"])
@jwt_required()
def delete_service(service_id):
    session = current_app.db.session
    current_user = get_jwt()

    get_service: Services = Services.query.filter_by(id=service_id).first()

    if get_service == None:
        return {"msg": "Wrong service ID"}, HTTPStatus.BAD_REQUEST

    barber_id = get_service.barber_id
    get_barber: Barbers = Barbers.query.get(barber_id)
    barber_shop_id = get_barber.barber_shop_id

    if (
        current_user["user_id"] == barber_shop_id
        and current_user["user_type"] == "barber_shop"
    ):
        session.delete(get_service)
        session.commit()

        return {"msg": "Service delete"}, HTTPStatus.NO_CONTENT

    else:
        return {"msg": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED


@bp_services.route("/<int:service_id>", methods=["PATCH"])
@jwt_required()
def update_services(service_id):
    session = current_app.db.session
    body = request.get_json()
    current_user = get_jwt()

    get_service: Services = Services.query.get(service_id)

    if get_service == None:
        return {"msg": "Wrong service ID"}, HTTPStatus.BAD_REQUEST

    barber_id = get_service.barber_id
    get_barber: Barbers = Barbers.query.get(barber_id)
    barber_shop_id = get_barber.barber_shop_id

    if (
        current_user["user_id"] == barber_shop_id
        and current_user["user_type"] == "barber_shop"
    ):

        body_keys = body.keys()
        keys_valid = ["service_name", "service_price"]
        validation = [values for values in body_keys if values not in keys_valid]

        if len(validation) == 0:

            service_name = body.get("service_name")
            service_price = body.get("service_price")

            barbar_id = get_service.barber_id
            barber: Barbers = Barbers.query.get(barbar_id)

            get_service.service_name = (
                service_name if service_name != None else get_service.service_name
            )
            get_service.service_price = (
                service_price if service_price != None else get_service.service_price
            )

            session.add(get_service)
            session.commit()

            return {
                "name": barber.name,
                "service_name": get_service.service_name,
                "service_price": get_service.service_price,
            }, HTTPStatus.ACCEPTED

        else:

            return {"msg": "invalid values"}, HTTPStatus.BAD_REQUEST

    else:
        return {"msg": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED
