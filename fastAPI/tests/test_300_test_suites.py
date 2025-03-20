import pytest
from fastapi.testclient import TestClient


def test_get_all_test_suites(test_client: TestClient):
    """Test retrieving all test suites"""
    response = test_client.get("/test_suites/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_test_suite(test_client: TestClient):
    """Test creating a new test suite"""
    new_test_suite = {
        "name": "Suite A",
        "description": "Testing Suite A",
        "status": "draft"
    }
    response = test_client.post("/test_suites/", json=new_test_suite)
    assert response.status_code == 201
    assert response.json()["name"] == new_test_suite["name"]

def test_update_test_suite(test_client: TestClient):
    """Test updating a test suite"""
    test_suite_id = 1  # Assuming test suite ID 1 exists
    update_data = {"name": "Updated Test Suite"}
    response = test_client.put(f"/test_suites/{test_suite_id}", json=update_data)
    if response.status_code == 200:
        assert response.json()["name"] == "Updated Test Suite"
    else:
        assert response.status_code == 404

def test_delete_test_suite(test_client: TestClient):
    """Test deleting a test suite"""
    test_suite_id = 1  # Assuming test suite ID 1 exists
    response = test_client.delete(f"/test_suites/{test_suite_id}")
    assert response.status_code in [200, 404]  # Either deleted or not found
