def test_create_enrollment():
    response = client.post(
        "/enrollments/",
        json={"course_id": 1, "user_id": 1}
    )
    assert response.status_code == 200
    assert response.json()["course_id"] == 1

def test_get_enrollments():
    response = client.get("/enrollments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
