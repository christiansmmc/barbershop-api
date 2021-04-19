# About

...


# Routes
  
### The following routes do not need token to access:  
  
 
###### Address
  
/address/<barbershop_id> - GET  
Get all address from barbershop  
  
/appointments/<barbershop_id> - GET  
/appointments/<barbershop_id>/<barber_id> - GET  
  
/barber_shop - GET  
/barber_shop/register - POST  
/barber_shop/login - POST  
  
/barber/<barbershop_id> - GET  
  
/client/register - POST  
/client/login - POST  
  
  
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

