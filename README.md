# About

...


# Routes

The following routes do not need token to access:

/address/<barbershop id> - GET

/appointments/<barbershop id> - GET
/appointments/<barbershop id>/<barber id> - GET

/barber_shop - GET
/barber_shop/register - POST
/barber_shop/login - POST

/barber/<barbershop id> - GET

/client/register - POST
/client/login - POST


# Authenticated routes

The following routes needs a token to access:

/address/<address id> - PATCH

/appointments - POST
/appointments/<appointment id> - PATCH
/appointments/<appointment id> - PATCH

/barber_shop/<barbershop id> - DELETE
/barber_shop/<barbershop id> - PATCH

/barber/register/<barbershop id> - POST
/barber/<barber id> - DELETE

/client/<user_id> - POST
/client/<user_id> - DELETE

/services/<barber id> - POST
/services/<service id> - PATCH
/services/<service id> - DELETE

