# About

...

# Routes

## The following routes do not need authentication to access:

<br/>

### Address

| Route                    | Method | Description                     |
| ------------------------ | ------ | ------------------------------- |
| /address/<barbershop_id> | GET    | Get all address from barbershop |

<br/>

### Apointments

| Route                                     | Method | Description                          |
| ----------------------------------------- | ------ | ------------------------------------ |
| /appointments/<barbershop_id>             | GET    | Get all appointments from barbershop |
| /appointments/<barbershop_id>/<barber_id> | GET    | Get all appointments from barber     |

<br/>

### Barbershop

| Route                 | Method | Description                  |
| --------------------- | ------ | ---------------------------- |
| /barber_shop          | GET    | Get all barbershop registred |
| /barber_shop/register | POST   | Register as barbershop       |
| /barber_shop/login    | POST   | Login as barbershop          |

<br/>

### Barbershop

| Route                   | Method | Description                 |
| ----------------------- | ------ | --------------------------- |
| /barber/<barbershop_id> | GET    | Get barbers from barbershop |

<br/>

### Barbershop

| Route            | Method | Description          |
| ---------------- | ------ | -------------------- |
| /client/register | POST   | Register as customer |
| /client/login    | POST   | Login as customer    |

<br/>
<br/>
<br/>

# Authenticated routes

## The following routes need authentication to access:

<br/>

### Address

| Route                 | Method | Description              |
| --------------------- | ------ | ------------------------ |
| /address/<address_id> | PATCH  | Updata data from address |

<br/>

### Appointments

| Route                          | Method | Description                  |
| ------------------------------ | ------ | ---------------------------- |
| /appointments                  | POST   | Create appointment           |
| /appointments/<appointment_id> | PATCH  | Updata data from appointment |
| /appointments/<appointment_id> | PATCH  | Updata data from appointment |

<br/>

### Appointments

| Route                       | Method | Description                 |
| --------------------------- | ------ | --------------------------- |
| /barber_shop/<barbershop_id | DELETE | Delete barbershop           |
| /barber_shop/<barbershop_id | PATCH  | Updata data from barbershop |

<br/>

### Barber

| Route                            | Method | Description                   |
| -------------------------------- | ------ | ----------------------------- |
| /barber/register/<barbershop_id> | POST   | Create barber for barbershop  |
| /barber/<barber_id>              | DELETE | Delete barber from barbershop |

<br/>

### Client

| Route             | Method | Description               |
| ----------------- | ------ | ------------------------- |
| /client/<user_id> | PATCH  | Updata data from costumer |
| /client/<user_id> | DELETE | Delete costumer           |

<br/>

### Services

| Route                  | Method | Description                |
| ---------------------- | ------ | -------------------------- |
| /services/<barber_id>  | POST   | Create service for barber  |
| /services/<service_id> | PATCH  | Update service from barber |
| /services/<service_id> | DELETE | Delete service from barber |

<br/>
<br/>

# Examples

<br/>

## Register as barbershop

<br/>

```
{
  "name": <String, not null>,
  "phone_number": <String, not null>,
  "cnpj": <String, not null>,
  "email": <String, not null>,
  "password": <String, not null>,
  "address": {
      	  "state": <String, not null>,
  		  "city": <String, not null>,
  		  "street_name": <String, not null>",
  		  "building_number": <String, not null>,
  		  "zip_code": <String, not null>
    }
}
```

<br/>

## Register as costumer

<br/>

```
{
  "name": <String, not null>,
  "email": <String, not null>,
  "password": <String, not null>,
  "phone_number": <String, not null>
}
```

<br/>

## Register a barber

<br/>

```
{
  "name": <String, Not null>,
  "services": [{
      "service_name": <String, not null>,
      "service_price": <String, not null>
  },
  {
      "service_name": <String, not null>,
      "service_price": <String, not null>
  }]
}
```

<br/>

## Create a service

<br/>

```
{
  "services": [{
      "service_name": <String, not null>,
      "service_price": <String, not null>
  }]
}
```

<br/>

## Create an appointment

<br/>

```
{
  "barber_id": <String, not null>,
  "barber_shop_id": <String, not null>,
  "services_id": <String, not null>,
  "date_time": "%d-%m-%y %h:%m"
}

```

<br/>
