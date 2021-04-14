from flask import Blueprint, request, current_app
from app.models.client import Client

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

@bp_client.route("/update/<int:user_id>", methods=['PATCH'])
def update_client(user_id):
    session = current_app.db.session
    
    body = request.get_json()
    
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
