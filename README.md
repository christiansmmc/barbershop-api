# About

...


# Routes
  
### The following routes do not need token to access:  
  
 
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
  
### The following routes needs a token to access:  
  
/address/<address_id> - PATCH  
  
/appointments - POST  
/appointments/<appointment_id> - PATCH  
/appointments/<appointment_id> - PATCH  
  
/barber_shop/<barbershop_id> - DELETE  
/barber_shop/<barbershop_id> - PATCH  
  
/barber/register/<barbershop_id> - POST  
/barber/<barber_id> - DELETE  
  
/client/<user_id> - POST  
/client/<user_id> - DELETE  
  
/services/<barber_id> - POST  
/services/<service_id> - PATCH  
/services/<service_id> - DELETE  

