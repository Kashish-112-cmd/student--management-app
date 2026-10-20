from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_students():
    response = app.test_client().get("/students")
    assert response.status_code == 200
    assert len(response.json["students"]) == 2