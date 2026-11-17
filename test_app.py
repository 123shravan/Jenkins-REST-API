
from app import app

def test_home():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200

def test_get_students():
    with app.test_client() as client:
        response = client.get("/students")
        assert response.status_code == 200

def test_add_student():
    with app.test_client() as client:
        response = client.post(
            "/students",
            json={"name": "Amit", "course": "CSE"}
        )
        assert response.status_code == 201
        assert response.json["name"] == "Amit"

def test_student_not_found():
    with app.test_client() as client:
        response = client.get("/students/999")
        assert response.status_code == 404
