from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Task Manager API is running"}


def test_create_task():
    response = client.post("/tasks/", json={"title": "Learn Docker", "description": "Study containers"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Learn Docker"
    assert data["completed"] is False


def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_task():
    response = client.get("/tasks/9999")
    assert response.status_code == 404


def test_update_task():
    create = client.post("/tasks/", json={"title": "Temp Task"})
    task_id = create.json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task():
    create = client.post("/tasks/", json={"title": "To be deleted"})
    task_id = create.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204