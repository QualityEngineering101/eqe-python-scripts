import pytest
from fastapi.testclient import TestClient

def test_get_all_products(test_client:TestClient):
    """ Testing the retrieval of all products """
    response = test_client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(),list)

def test_get_product_by_id(test_client:TestClient):
    """ Test retrieving a product by ID """
    product_id = 1
    response = test_client.get(f"/products/{product_id}")
    if response.status_code == 200:
        data = response.json()
        assert data["id"] == product_id
    else:
        assert response.status_code == 404

# def test_create_product(test_client:TestClient):
#     new_product = {
#         "name":"Test Product",
#         "description":"A Test Product",
#         "status":"draft"
#     }
#     response = test_client.post("/products/",json=new_product)
#     assert response.status_code == 201
#     assert response.json()["name"] == new_product["name"]

def test_invalid_product_fetch(test_client: TestClient):
    """ Test getting a non-existent product """
    response = test_client.get("/product/9999")
    assert response.status_code == 404

# TODO expand the tests

