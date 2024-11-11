def test_create_payment():
    response = client.post(
        "/payments/",
        json={"user_id": 1, "amount": 100, "status": "completed"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "completed"

def test_get_payments():
    response = client.get("/payments/user/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
