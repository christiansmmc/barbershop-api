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

    if addresses_serialized:

        return {"data": addresses_serialized}, HTTPStatus.OK

    else:

        return {"msg": "Wrong id or barbershop has no address registered"}


@bp_address.route("/<int:address_id>", methods=["PATCH"])
@jwt_required()
def update_address(address_id):
    current_user = get_jwt()

    address_to_update = Address.query.filter_by(id=address_id).first()

    if address_to_update:
        if (
            current_user["user_id"] == address_to_update.barber_shop_id
            and current_user["user_type"] == "barber_shop"
        ):

            session = current_app.db.session

            request_data = request.get_json()

            if request_data.get("state"):
                address_to_update.state = request_data["state"]
            if request_data.get("city"):
                address_to_update.city = request_data["city"]
            if request_data.get("street_name"):
                address_to_update.street_name = request_data["street_name"]
            if request_data.get("building_number"):
                address_to_update.building_number = request_data["building_number"]
            if request_data.get("zip_code"):
                address_to_update.zip_code = request_data["zip_code"]

            session.add(address_to_update)
            session.commit()

            address_serialized = AddressSchema().dump(address_to_update)
            return {"data": address_serialized}, HTTPStatus.ACCEPTED

        else:
            return {
                "error": "You do not have permission to do this"
            }, HTTPStatus.UNAUTHORIZED

    return {"msg": "Wrong address ID or token"}, HTTPStatus.FORBIDDEN


# @bp_address.route("/<int:barber_shop_id>", methods=["POST"])
# @jwt_required()
# def create_address(barber_shop_id):
#     current_user = get_jwt()

#     if (
#         current_user["user_id"] == barber_shop_id
#         and current_user["user_type"] == "barber_shop"
#     ):
#         session = current_app.db.session

#         request_data = request.get_json()

#         address = Address(
#             barber_shop_id=barber_shop_id,
#             state=request_data["state"],
#             city=request_data["city"],
#             street_name=request_data["street_name"],
#             building_number=request_data["building_number"],
#             zip_code=request_data["zip_code"],
#         )

#         session.add(address)
#         session.commit()

#         serialized = AddressSchema().dump(address)

#         return serialized, HTTPStatus.CREATED

#     else:
#         return {"data": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED


# @bp_address.route("/<int:address_id>", methods=["DELETE"])
# @jwt_required()
# def delete_address(address_id):
#     current_user = get_jwt()

#     address_to_delete = Address.query.filter_by(id=address_id).first()

#     if address_to_delete != None:

#         if (
#             current_user["user_id"] == address_to_delete.barber_shop_id
#             and current_user["user_type"] == "barber_shop"
#         ):

#             session = current_app.db.session
#             Address.query.filter_by(id=address_id).delete()
#             session.commit()

#             return {}, HTTPStatus.NO_CONTENT

#     return {"data": "Wrong address ID"}, HTTPStatus.NOT_FOUND