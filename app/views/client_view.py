from flask import Blueprint, request, current_app
from flask_jwt_extended import get_jwt, jwt_required
from app.models.client import Client
from http import HTTPStatus

bp_client = Blueprint("bp_client", __name__, url_prefix='/client')


@bp_client.route("/register", methods=["POST"])
def create_client():
    session = current_app.db.session

    body = request.get_json()

    name = body.get("name")
    email = body.get("email")
    password = body.get("password")
    phone_number = body.get("phone_number")
    user_type = 'client'

    new_client = Client(
        name=name, email=email, password=password, phone_number=phone_number, user_type=user_type
    )

    session.add(new_client)
    session.commit()

    return {"name": new_client.name, "email": new_client.email}, 201


@bp_client.route("/login", methods=["POST"])
def login_client():
    body = request.get_json()
    
    login_client = Client.query.filter_by(email=body['email'], password=body['password']).first()
    
    if login_client != None:
        additional_claims = {
            "user_type": "client",
            "user_id": login_client.id,
        }
        access_token = create_access_token(
            identity=body['email'], additional_claims=additional_claims
        )
        
        return {'Acess token': access_token}, 201
    
    return {'data': "Wrong email or password"}, 403

@bp_client.route("/update/<int:user_id>", methods=['PATCH'])
def update_client(user_id):
    session = current_app.db.session
    
    body = request.get_json()
    
    body_keys = body.keys()
    keys_valid = ['name', 'email', 'password', 'phone_number']
    validation = [values for values in body_keys if values not in keys_valid]
    
    if len(validation) == 0:
    
        name = body.get('name') 
        email = body.get('email') 
        password = body.get("password")
        phone_number = body.get("phone_number")
        
        current_client: Client = Client.query.get(user_id)

        current_client.name = name if name != None else current_client.name
        current_client.email = email if email != None else current_client.email
        current_client.password = password if password != None else current_client.password
        current_client.phone_number = phone_number if phone_number != None else current_client.phone_number
        
        session.add(current_client)
        session.commit()
        
        return {"id": current_client.id, "name": current_client.name, "email": current_client.email, "phone_number": current_client.phone_number}, 202
    
    else:
        
        return {"msg": "valores inválidos"}, 400

@bp_client.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_client(user_id):
    current_user = get_jwt()    

    if (current_user["user_id"] == user_id and current_user["user_type"] == "client") :
        session = current_app.db.session
        Client.query.filter_by(id=user_id).delete()
        session.commit()
        return {}, 200

    else:
        return {"Data": "You don't have permission to do this"}, HTTPStatus.UNATHORIZED

    return {"Data": "Wrong barbershop ID"}, HTTPSTATUS.NOT_FOUND
