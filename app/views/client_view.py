from flask import Blueprint, request, current_app
from app.models.client import Client

bp_client = Blueprint("bp_client", __name__)


@bp_client.route("/client", methods=["POST"])
def create_client():
    session = current_app.db.session

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    phone_number = data.get("phone_number")

    new_client = Client(
        name=name, email=email, password=password, phone_number=phone_number
    )

    session.add(new_client)
    session.commit()

    return {"name": new_client.name, "email": new_client.email}, 201
