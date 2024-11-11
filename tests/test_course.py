import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test Case: Create a new course
def test_create_course():
    response = client.post(
        "/courses/",
        json={
            "title": "New Course",
            "description": "This is a new course.",
            "price": 100,
        }
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New Course"

# Test Case: Get a list of courses
def test_get_courses():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test Case: Get a specific course by ID
def test_get_course():
    # Assuming you know course_id 1 exists
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["title"] == "New Course"

# Test Case: Update a course
def test_update_course():
    response = client.put(
        "/courses/1",
        json={
            "title": "Updated Course Title",
            "description": "Updated description",
            "price": 150,
        }
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Course Title"

# Test Case: Delete a course
def test_delete_course():
    response = client.delete("/courses/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Course deleted successfully"}
