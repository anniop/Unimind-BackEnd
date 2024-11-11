def test_login():
    response = client.post(
        "/auth/login",
        json={"email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_register():
    response = client.post(
        "/auth/register",
        json={"email": "newuser@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "newuser@example.com"
