from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.address import Address
from app.serializers.address_serializer import AddressSchema
from flask_jwt_extended import get_jwt, jwt_required


bp_address = Blueprint("bp_address", __name__, url_prefix="/address")


@bp_address.route("/<int:barbershop_id>", methods=["GET"])
def address(barbershop_id):

    addresses_from_barbershop = Address.query.filter_by(barber_shop_id=barbershop_id)

    addresses_serialized = [
        AddressSchema().dump(address) for address in addresses_from_barbershop
    ]

    return {"Data": addresses_serialized}, HTTPStatus.OK


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

        serialized = AddressSchema().dump(address)

        return serialized, HTTPStatus.CREATED

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


@bp_address.route("/update/<int:address_id>", methods=["PATCH"])
@jwt_required()
def update_address(address_id):
    current_user = get_jwt()

    address_to_update = Address.query.filter_by(id=address_id).first()
    print(current_user["user_id"], address_to_update.barber_shop_id)
    print(current_user["user_type"])
    if (
        current_user["user_id"] == address_to_update.barber_shop_id
        and current_user["user_type"] == "barber_shop"
    ):

        session = current_app.db.session

        request_data = request.get_json()

        validation_keys = [
            "state",
            "city",
            "street_name",
            "building_number",
            "zip_code",
        ]

        validation = [
            value for value in request_data.keys() if value not in validation_keys
        ]

        if not validation:

            state = request_data.get("state") or address_to_update.state
            city = request_data.get("city") or address_to_update.city
            street_name = (
                request_data.get("street_name") or address_to_update.street_name
            )
            building_number = (
                request_data.get("building_number") or address_to_update.building_number
            )
            zip_code = request_data.get("zip_code") or address_to_update.zip_code

            address_to_update.state = state
            address_to_update.city = city
            address_to_update.street_name = street_name
            address_to_update.building_number = building_number
            address_to_update.zip_code = zip_code

            session.add(address_to_update)
            session.commit()

            serialized = AddressSchema().dump(address_to_update)

            return {"Data": serialized}, HTTPStatus.ACCEPTED

        else:

            return {"Data": "Verify the request body"}, HTTPStatus.BAD_REQUEST

    return {"Data": "Wrong address ID"}, HTTPStatus.NOT_FOUND