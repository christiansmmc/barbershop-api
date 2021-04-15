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