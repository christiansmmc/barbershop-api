def test_get_barber_shop(client_and_db):
    client = client_and_db[0]
    response = client.get("/barber_shop")
    assert response.status_code == 204


def test_post_register_barber_shop(client_and_db):
    client = client_and_db[0]
    payload = {
	    "name":"Jooaao4",
	    "phone_number":"11995877551",
	    "cnpj":"22456789015",
	    "email":"joaaoa4@barber.com",
	    "password":"12345678",
	    "address":{
	    	"state":"PR",
	    	"city":"Curitiba",
	    	"street_name":"Rua Marte",
	    	"building_number":"1234",
	    	"zip_code":"12345678"
	    }
    }

    response = client.post("/barber_shop/register", json=payload)
    assert response.status_code == 201


def test_get_barber_shop(client_and_db):
    client = client_and_db[0]
    payload = {
	    "name":"Jooaao4",
	    "phone_number":"11995877551",
	    "cnpj":"22456789015",
	    "email":"joaaoa4@barber.com",
	    "password":"12345678",
	    "address":{
	    	"state":"PR",
	    	"city":"Curitiba",
	    	"street_name":"Rua Marte",
	    	"building_number":"1234",
	    	"zip_code":"12345678"
	    }
    }

    client.post("/barber_shop/register", json=payload)
    response = client.get("/barber_shop")
    assert response.status_code == 200


def test_post_login_barber_shop(client_and_db):
    client = client_and_db[0]

    payload_login = {
	    "email":"joaaoa4@barber.com",
	    "password":"12345678"
    }

    payload = {
	    "name":"Jooaao4",
	    "phone_number":"11995877551",
	    "cnpj":"22456789015",
	    "email":"joaaoa4@barber.com",
	    "password":"12345678",
	    "address":{
	    	"state":"PR",
	    	"city":"Curitiba",
	    	"street_name":"Rua Marte",
	    	"building_number":"1234",
	    	"zip_code":"12345678"
	    }
    }

    client.post("/barber_shop/register", json=payload)
    response = client.post("/barber_shop/login", json=payload_login)
    assert response.status_code == 201


# def test_delete_barber_shop(client_and_db):
#     client = client_and_db[0]

#     payload_login = {
# 	    "email":"joaaoa4@barber.com",
# 	    "password":"12345678"
#     }

#     payload = {
# 	    "name":"Jooaao4",
# 	    "phone_number":"11995877551",
# 	    "cnpj":"22456789015",
# 	    "email":"joaaoa4@barber.com",
# 	    "password":"12345678",
# 	    "address":{
# 	    	"state":"PR",
# 	    	"city":"Curitiba",
# 	    	"street_name":"Rua Marte",
# 	    	"building_number":"1234",
# 	    	"zip_code":"12345678"
# 	    }
#     }

#     client.post("/barber_shop/register", json=payload)
#     login_response = client.post("/barber_shop/login", json=payload_login)
#     token = login_response.get_json()["data"]["access_token"]
#     barber_id = login_response.get_json()["data"]["barbershop_id"]
#     print(f"\n{barber_id}")
#     print(f"\n{token}")
#     response = client.delete("/barber_shop/1", headers={"BEARER": token})
#     assert response.status_code == 204