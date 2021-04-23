from flask import Blueprint, request, current_app
from app.models.client import Client
from http import HTTPStatus
from flask_jwt_extended import get_jwt, jwt_required, create_access_token
from app.models.client import Client
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError, DataError
import re

bp_client = Blueprint("bp_client", __name__, url_prefix="/client")


@bp_client.route("/register", methods=["POST"])
def create_client():
    try:
        session = current_app.db.session

        body = request.get_json()

        error_list = []

        if not Client.query.filter_by(email=body["email"]).first():
            email = body["email"]
        else:
            error_list.append("email")

        if not Client.query.filter_by(phone_number=body["phone_number"]).first():
            phone_number = body["phone_number"]
        else:
            error_list.append("phone_number")

        if error_list:
            raise NameError(error_list)

        name = body["name"]
        password = body["password"]
        user_type = "client"

        new_client = Client(
            name=name,
            email=email,
            phone_number=phone_number,
            user_type=user_type,
        )

        new_client.password = password

        session.add(new_client)
        session.commit()

        return {
            "id": new_client.id,
            "name": new_client.name,
            "email": new_client.email,
        }, HTTPStatus.CREATED

    except KeyError:
        return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST

    except DataError:
        return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST

    except NameError as e:
        unique = e.args[0]
        errors = ""
        for error in unique:
            errors = errors + f"{error}, "

        return {"msg": f"{errors}already registered"}, HTTPStatus.BAD_REQUEST


@bp_client.route("/login", methods=["POST"])
def login_client():
    try:
        body = request.get_json()

        login_client = Client.query.filter_by(email=body["email"]).first()

        if login_client != None:

            hash_validation = login_client.check_password(body.get("password"))

            if hash_validation:

                additional_claims = {
                    "user_type": "client",
                    "user_id": login_client.id,
                }
                access_token = create_access_token(
                    identity=body["email"], additional_claims=additional_claims
                )

                return {
                    "user ID": login_client.id,
                    "acess token": access_token,
                }, HTTPStatus.CREATED

        return {"data": "Wrong email or password"}, HTTPStatus.FORBIDDEN

    except KeyError:
        return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST

    except TypeError:
        return {"msg": "Verify BODY content"}, HTTPStatus.BAD_REQUEST


@bp_client.route("/<int:user_id>", methods=["PATCH"])
@jwt_required()
def update_client(user_id):
    session = current_app.db.session
    current_user = get_jwt()

    if current_user["user_id"] == user_id and current_user["user_type"] == "client":

        body = request.get_json()

        body_keys = body.keys()
        keys_valid = ["name", "email", "password", "phone_number"]
        validation = [values for values in body_keys if values not in keys_valid]

        if len(validation) == 0:

            current_client: Client = Client.query.get(user_id)

            if body.get("name"):
                current_client.name = body.get("name")
            if body.get("email"):
                current_client.email = body.get("email")
            if body.get("password"):
                current_client.password = body.get("password")
            if body.get("phone_number"):
                current_client.phone_number = body.get("phone_number")

            session.add(current_client)
            session.commit()

            return {
                "id": current_client.id,
                "name": current_client.name,
                "email": current_client.email,
                "phone_number": current_client.phone_number,
            }, HTTPStatus.ACCEPTED

        else:

            return {"msg": "valores inválidos"}, HTTPStatus.BAD_REQUEST
    else:
        return {"Data": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED


@bp_client.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_client(user_id):
    current_user = get_jwt()

    if current_user["user_id"] == user_id and current_user["user_type"] == "client":
        session = current_app.db.session
        Client.query.filter_by(id=user_id).delete()
        session.commit()
        return {}, HTTPStatus.NO_CONTENT
    else:
        return {"Data": "You don't have permission to do this"}, HTTPStatus.UNAUTHORIZED
