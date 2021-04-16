from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.services import Services
from app.models.barbers import Barbers
from app.models.barber_shop_model import Barber_shop
from flask_jwt_extended import jwt_required, get_jwt
from app.serializers.service_serializer import ServicesSchema

bp_services = Blueprint('bp_services', __name__, url_prefix='/services')

@bp_services.route('/<int:barber_id>', methods=['POST']) #
@jwt_required()
def register_services(barber_id):
    session = current_app.db.session
    current_user = get_jwt()
    body = request.get_json()
    get_barber: Barbers = Barbers.query.filter_by(id=barber_id).first()
    
    if current_user["user_id"] == get_barber.barber_shop_id and current_user["user_type"] == "barber_shop":
        if 'service' in body:       
            for service in body['service']:
                new_service: Services = Services(
                    service_name=service["service_name"],
                    service_price=service["service_price"],
                )
                
                get_barber.service_list.append(new_service)
            
            session.add(get_barber)
            session.commit()
        
        services_serialized = [ServicesSchema().dump(s) for s in get_barber.service_list]
            
        return {'data': {
            'barber_name': get_barber.name,
            'service': services_serialized
        }}
                
    else:
        return {
            "msg": "You don't have permission to do this"
        }, HTTPStatus.UNAUTHORIZED
        
@bp_services.route('/<int:service_id>', methods=['DELETE'])
@jwt_required()
def delete_service(service_id):
    session = current_app.db.session
    current_user = get_jwt()
    
    get_service: Services = Services.query.filter_by(id=service_id).first()
    barber_id = get_service.barber_id
    get_barber: Barbers = Barbers.query.filter_by(id=barber_id).first()
    barber_shop_id = get_barber.barber_shop_id
    
    if current_user["user_id"] == barber_shop_id and current_user["user_type"] == "barber_shop":
        # print(f'SERVICE {get_service.barber_id} {get_service.service_name}')
        session.delete(get_service)
        session.commit()
    
        return {'msg': 'Service delete'}, HTTPStatus.OK
    
    else:
        return {
            "msg": "You don't have permission to do this"
        }, HTTPStatus.UNAUTHORIZED
        

    
    

            
    
            