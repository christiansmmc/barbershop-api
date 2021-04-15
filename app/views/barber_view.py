from flask import Blueprint, request, current_app, jsonify
from app.models.barbers import Barbers
from app.models.services import Services
from app.models.barber_shop_model import Barber_shop
from flask_jwt_extended import jwt_required, get_jwt

bp_barber = Blueprint('bp_barber', __name__, url_prefix='/barber')

@bp_barber.route('/register/<int:barber_shop_id>', methods=['POST']) #@jwt_required
def register_barber(barber_shop_id):
    print('##########', type(barber_shop_id))
    # current_user = get_jwt()
    body = request.get_json()    
    name = body.get('name')
    
    # if current_user["user_id"] == barber_shop_id and current_user["user_type"] == "barber_shop":
    session = current_app.db.session

    new_barber = Barbers(name=name, barber_shop_id=barber_shop_id, user_type='barber')
    barber_shop = Barber_shop.query.filter_by(id=new_barber.barber_shop_id).first()
    
    if 'services' in body:
        
        for service in body['services']:
            
            new_service = Services(service_name=service['service_name'], service_price=service['service_price'], barber_id=new_barber.id)
            new_barber.service_list.append(new_service)
            
    session.add(new_barber)
    session.commit()
            
    return {"name_barber": new_barber.name, "name_barbershop": barber_shop.name}, 201

    # else:
    #     return {"Data": "You don't have permission to do this"}, 401
    

# @bp_barber.route('', methods=['GET'])
# def all_barbers():
#     session = current_app.db.session

#     barbers: Barbers = Barbers.query.all() 
                