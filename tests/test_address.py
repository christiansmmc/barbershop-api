def test_get_address(client_and_db):
    client = client_and_db[0]
    response = client.get("/address/1")
    assert response.status_code == 200


def test_patch_without_header_address(client_and_db):
    client = client_and_db[0]
    response = client.patch("/address/1")
    assert response.status_code == 401