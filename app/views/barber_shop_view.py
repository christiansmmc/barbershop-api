from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.barber_shop_model import Barber_shop
from app.serializers.barber_shop_serializer import BarberSchema
from flask import jsonify


bp_barber_shop = Blueprint("bp_barber_shop", __name__)


@bp_barber_shop.route("/barber_shop", methods=["GET"])
def barber_shop():

    enderecos = Barber_shop.query.all()

    all_barbers = []

    for i in enderecos:
        serialized = BarberSchema().dump(i)
        all_barbers.append(serialized)

    return jsonify(all_barbers)
