from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.address import Address
from app.serializers.address_serializer import AddressSchema
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required


bp_address = Blueprint("bp_address", __name__, url_prefix="/address")


@bp_address.route("/<int:barber_shop_id>", methods=["POST"])
@jwt_required()
def create_address(barber_shop_id):
    current_user = get_jwt()

    if (
        current_user["user_id"] == barber_shop_id
        and current_user["user_type"] == "barber_shop"
    ):
        session = current_app.db.session

        request_data = request.get_json()

        address = Address(
            barber_shop_id=barber_shop_id,
            state=request_data["state"],
            city=request_data["city"],
            street_name=request_data["street_name"],
            building_number=request_data["building_number"],
            zip_code=request_data["zip_code"],
        )

        session.add(address)
        session.commit()

        serializers = AddressSchema().dump(address)

        return serializers, HTTPStatus.CREATED

    else:
        return {"Data": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED


@bp_address.route("/<int:address_id>", methods=["DELETE"])
@jwt_required()
def delete_address(address_id):
    current_user = get_jwt()

    address_to_delete = Address.query.filter_by(id=address_id).first()

    if address_to_delete != None:

        if (
            current_user["user_id"] == address_to_delete.barber_shop_id
            and current_user["user_type"] == "barber_shop"
        ):

            session = current_app.db.session
            Address.query.filter_by(id=address_id).delete()
            session.commit()

            return {}, HTTPStatus.NO_CONTENT

    return {"Data": "Wrong address ID"}, HTTPStatus.NOT_FOUND


@bp_address.route("/<int:barbershop_id>", methods=["GET"])
def address(barbershop_id):

    addresses_from_barbershop = Address.query.filter_by(barber_shop_id=barbershop_id)

    addresses_serialized = [
        AddressSchema().dump(address) for address in addresses_from_barbershop
    ]

    return {"Data": addresses_serialized}, HTTPStatus.OK