from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.barber_shop_model import Barber_shop
from app.models.address import Address
from app.serializers.barber_shop_serializer import BarberSchema
from app.serializers.address_serializer import AddressSchema
from flask import jsonify
from flask_jwt_extended import get_jwt, jwt_required, create_access_token
from sqlalchemy.exc import IntegrityError
import re

bp_barber_shop = Blueprint("bp_barber_shop", __name__, url_prefix="/barber_shop")


@bp_barber_shop.route("", methods=["GET"])
def barber_shop():

    all_barbers_shop_db = Barber_shop.query.all()

    if all_barbers_shop_db:

        all_barbershops = []

        for barber_shop in all_barbers_shop_db:

            barber_shop_serialized = BarberSchema().dump(barber_shop)

            barber_shop_serialized["address"] = AddressSchema().dump(
                barber_shop.address_list
            )

            all_barbershops.append(barber_shop_serialized)

        return {"data": all_barbershops}

    return {}, HTTPStatus.NO_CONTENT


@bp_barber_shop.route("/register", methods=["POST"])
def register_barber_shop():
    try:
        session = current_app.db.session

        request_data = request.get_json()

        if request_data != None:

            barber_shop = Barber_shop(
                name=request_data["name"],
                phone_number=request_data["phone_number"],
                cnpj=request_data["cnpj"],
                email=request_data["email"],
                password=request_data["password"],
                user_type="barber_shop",
            )

            session.add(barber_shop)
            session.commit()

            barber_shop_serialized = BarberSchema().dump(barber_shop)

            if "address" in request_data:

                address = Address(
                    barber_shop_id=barber_shop.id,
                    state=request_data["address"]["state"],
                    city=request_data["address"]["city"],
                    street_name=request_data["address"]["street_name"],
                    building_number=request_data["address"]["building_number"],
                    zip_code=request_data["address"]["zip_code"],
                )

                session.add(address)
                session.commit()

                address_serializer = AddressSchema().dump(address)

                barber_shop_serialized["address"] = address_serializer

            return {"data": barber_shop_serialized}, HTTPStatus.CREATED

        else:
            return {"msg": "Verify BODY content"}

    except IntegrityError as e:

        error_origin = e.orig.diag.message_detail
        error = re.findall("\((.*?)\)", error_origin)

        return {"msg": f"{error[0].upper()} already registered"}, HTTPStatus.OK

    except KeyError:
        return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST


@bp_barber_shop.route("/<int:barber_shop_id>", methods=["DELETE"])
@jwt_required()
def delete_barber_shop(barber_shop_id):
    current_user = get_jwt()

    if (
        current_user["user_id"] == barber_shop_id
        and current_user["user_type"] == "barber_shop"
    ):
        session = current_app.db.session
        Barber_shop.query.filter_by(id=barber_shop_id).delete()
        session.commit()
        return {}, HTTPStatus.NO_CONTENT

    return {"msg": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED


@bp_barber_shop.route("/login", methods=["POST"])
def login_barber_shop():
    request_data = request.get_json()

    user_to_login = Barber_shop.query.filter_by(
        email=request_data["email"], password=request_data["password"]
    ).first()

    if user_to_login != None:

        additional_claims = {
            "user_type": "barber_shop",
            "user_id": user_to_login.id,
        }
        access_token = create_access_token(
            identity=request_data["email"], additional_claims=additional_claims
        )

        return {
            "Barber ID": user_to_login.id,
            "Acess token": access_token,
        }, HTTPStatus.CREATED

    return {"data": "Wrong email or password"}, HTTPStatus.FORBIDDEN


@bp_barber_shop.route("/<int:barbershop_id>", methods=["PATCH"])
@jwt_required()
def update_barber_Shop(barbershop_id):
    current_user = get_jwt()

    barbershop_to_update = Barber_shop.query.filter_by(id=barbershop_id).first()

    if barbershop_to_update != None:
        if (
            current_user["user_id"] == barbershop_to_update.id
            and current_user["user_type"] == "barber_shop"
        ):
            session = current_app.db.session

            request_data = request.get_json()

            validation_keys = [
                "name",
                "phone_number",
                "cnpj",
                "email",
                "password",
            ]

            validation = [
                value for value in request_data.keys() if value not in validation_keys
            ]

            if not validation:
                name = (
                    request_data.get("name")
                    if request_data.get("name")
                    else barbershop_to_update.name
                )
                phone_number = (
                    request_data.get("phone_number")
                    if request_data.get("phone_number")
                    else barbershop_to_update.phone_number
                )
                cnpj = (
                    request_data.get("cnpj")
                    if request_data.get("cnpj")
                    else barbershop_to_update.cnpj
                )
                email = (
                    request_data.get("email")
                    if request_data.get("email")
                    else barbershop_to_update.email
                )
                password = (
                    request_data.get("password")
                    if request_data.get("password")
                    else barbershop_to_update.password
                )

                barbershop_to_update.name = name
                barbershop_to_update.phone_number = phone_number
                barbershop_to_update.cnpj = cnpj
                barbershop_to_update.email = email
                barbershop_to_update.password = password

                session.add(barbershop_to_update)
                session.commit()

                barber_shop_serialized = BarberSchema().dump(barbershop_to_update)

                return {"data": barber_shop_serialized}, HTTPStatus.ACCEPTED

            else:
                return {"data": "Verify the request body"}, HTTPStatus.BAD_REQUEST

        else:
            return {
                "msg": "You do not have permission to do this"
            }, HTTPStatus.UNAUTHORIZED

    else:
        return {"msg": "Wrong barbershop ID"}, HTTPStatus.NOT_FOUND
