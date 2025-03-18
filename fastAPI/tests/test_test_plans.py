import pytest
from fastapi.testclient import TestClient

def test_get_all_test_plans(test_client: TestClient):
    """Test retrieving all test plans"""
    response = test_client.get("/test_plans/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_test_plan(test_client: TestClient):
    """Test creating a new test plan"""
    new_test_plan = {
        "name": "Sample Test Plan",
        "description": "A test plan for automation",
        "status": "draft"
    }
    response = test_client.post("/test_plans/", json=new_test_plan)
    assert response.status_code == 201
    assert response.json()["name"] == new_test_plan["name"]

def test_update_test_plan(test_client: TestClient):
    """Test updating a test plan"""
    test_plan_id = 1  # Assuming test plan ID 1 exists
    update_data = {"name": "Updated Test Plan"}
    response = test_client.put(f"/test_plans/{test_plan_id}", json=update_data)
    if response.status_code == 200:
        assert response.json()["name"] == "Updated Test Plan"
    else:
        assert response.status_code == 404

def test_delete_test_plan(test_client: TestClient):
    """Test deleting a test plan"""
    test_plan_id = 1  # Assuming test plan ID 1 exists
    response = test_client.delete(f"/test_plans/{test_plan_id}")
    assert response.status_code in [200, 404]  # Either deleted or not found
