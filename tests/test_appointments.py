def test_get_client_appointments(client_and_db):
    client = client_and_db[0]
    response = client.get("/appointments/client/1")
    assert response.status_code == 401


def test_get_barbershop_appointments(client_and_db):
    client = client_and_db[0]
    response = client.get("/appointments/barbershop/1")
    assert response.status_code == 200


def test_get_barber_appointments(client_and_db):
    client = client_and_db[0]
    response = client.get("/appointments/barbershop/1/1")
    assert response.status_code == 200