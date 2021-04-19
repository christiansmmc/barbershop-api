# About

...


# Routes
  
## The following routes do not need authentication to access:  
  
 
#### Address

##### /address/<barbershop_id> - GET  
Get all address from barbershop  
  
  
#### Appointments

##### /appointments/<barbershop_id> - GET  
Get all appointments from barbershop  
  
##### /appointments/<barbershop_id>/<barber_id> - GET  
Get all appointments from barber  
  
  
#### Barbershop
##### /barber_shop - GET  
Get all barbershop registred on the database  
  
##### /barber_shop/register - POST  
Register as barbershop
  
##### /barber_shop/login - POST  
Login as barbershop  
  
  
#### Barber
##### /barber/<barbershop_id> - GET  
Get barbers from barbershop  
  
  
#### Client
##### /client/register - POST  
Register as costumer  
  
##### /client/login - POST  
Login as costumer  
  
  
# Authenticated routes
  
### The following routes need authentication to access:
  
#### Address

| Route | Method | Description |
| ---- | ---- | ---- |
| /address/<address_id> | PATCH | Updata data from address |

<!-- #### Appointments

| Route | Method | Description |
| /appointments | POST | Create appointment |
| /appointments/<appointment_id> | PATCH | Updata data from appointment |
| /appointments/<appointment_id> | PATCH | Updata data from appointment |

#### Appointments

| Route | Method | Description |
| /barber_shop/<barbershop_id | DELETE | Delete barbershop |
| /barber_shop/<barbershop_id | PATCH | Updata data from barbershop |
  
  
/barber/register/<barbershop_id> - POST  
/barber/<barber_id> - DELETE  
  
/client/<user_id> - POST  
/client/<user_id> - DELETE  
  
/services/<barber_id> - POST  
/services/<service_id> - PATCH  
/services/<service_id> - DELETE   -->

