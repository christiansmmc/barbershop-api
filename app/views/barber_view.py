from flask import Blueprint, request, current_app, jsonify
from http import HTTPStatus
from app.models.barbers import Barbers
from app.models.services import Services
from app.models.barber_shop_model import Barber_shop
from app.serializers.service_serializer import ServicesSchema
from flask_jwt_extended import jwt_required, get_jwt

bp_barber = Blueprint("bp_barber", __name__, url_prefix="/barber")


@bp_barber.route("/register/<int:barber_shop_id>", methods=["POST"])
@jwt_required()
def register_barber(barber_shop_id):
    try:
        current_user = get_jwt()
        body = request.get_json()

        if (
            current_user["user_id"] == barber_shop_id
            and current_user["user_type"] == "barber_shop"
        ):

            session = current_app.db.session

            name = body["name"]

            new_barber = Barbers(
                name=name, barber_shop_id=barber_shop_id, user_type="barber"
            )

            if "services" in body:

                for service in body["services"]:

                    new_service = Services(
                        service_name=service["service_name"],
                        service_price=service["service_price"],
                    )

                    new_barber.service_list.append(new_service)

            session.add(new_barber)
            session.commit()

            barbershop = Barber_shop.query.filter_by(id=barber_shop_id).first()

            return {
                "data": {"barber name": new_barber.name, "barbershop name": barbershop.name}
            }, HTTPStatus.CREATED

        else:
            return {
                "error": "You don't have permission to do this"
            }, HTTPStatus.UNAUTHORIZED
            
    except KeyError:
        return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST


@bp_barber.route("/<int:barber_id>", methods=["DELETE"])
@jwt_required()
def delete_barber(barber_id):

    current_user = get_jwt()

    barber = Barbers.query.filter_by(id=barber_id).first()

    if barber != None:

        if (
            current_user["user_id"] == barber.barber_shop_id
            and current_user["user_type"] == "barber_shop"
        ):
            session = current_app.db.session
            Barbers.query.filter_by(id=barber_id).delete()
            session.commit()

            return {}, HTTPStatus.NO_CONTENT

        else:
            return {
                "msg": "You don't have permission to do this"
            }, HTTPStatus.UNAUTHORIZED

    else:
        return {"msg": "Wrong barber ID"}, HTTPStatus.NOT_FOUND


@bp_barber.route("/<int:barbershop_id>", methods=["GET"])
def get_barbers(barbershop_id):

    barbershop_exist = Barber_shop.query.filter_by(id=barbershop_id).first()

    if barbershop_exist:

        barbers = Barbers.query.filter_by(barber_shop_id=barbershop_id)

        barbershop_name = Barber_shop.query.filter_by(id=barbershop_id).first().name

        barbers_data = []

        for barber in barbers:
            barber_data = {}

            barber_data["barber name"] = barber.name
            barber_data["barber id"] = barber.id

            barber_data["services"] = [
                ServicesSchema().dump(service) for service in barber.service_list
            ]
            barbers_data.append(barber_data)

        return {"data": barbers_data}

    return {"msg": "Wrong barbershop ID"}, HTTPStatus.NOT_FOUND