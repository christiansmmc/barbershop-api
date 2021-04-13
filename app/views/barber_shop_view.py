from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.barber_shop_model import Barber_shop
from app.serializers.barber_shop_serializer import BarberSchema
from flask import jsonify

from flask_jwt_extended import create_access_token


bp_barber_shop = Blueprint("bp_barber_shop", __name__)


@bp_barber_shop.route("/barber_shop", methods=["GET"])
def barber_shop():

    enderecos = Barber_shop.query.all()

    all_barbers = []

    for i in enderecos:
        serialized = BarberSchema().dump(i)
        all_barbers.append(serialized)

    return jsonify(all_barbers)


@bp_barber_shop.route("/barber_shop", methods=["POST"])
def create_barber_shop():

    session = current_app.db.session

    request_data = request.get_json()
    barber_shop = Barber_shop(
        name=request_data["name"],
        phone_number=request_data["phone_number"],
        cnpj=request_data["cnpj"],
        email=request_data["email"],
        password=request_data["password"],
        user_type="barber_shop",
    )

    access_token = create_access_token(identity=request_data["email"])

    session.add(barber_shop)
    session.commit()

    serialized = BarberSchema().dump(barber_shop)

    return {"Data": serialized, "access_token": access_token}
