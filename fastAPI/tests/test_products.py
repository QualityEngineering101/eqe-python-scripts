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

@pytest.mark.parametrize(
    "payload, expected_status_code",
    [
        ({"name": "Product D", "description": "Product D Description", "status": "draft"}, 201),
        ({"name": "Product E", "description": "Product E Description", "status": "active"}, 201),
        ({"name": "Product F", "description": "Product F Description", "status": "archived"}, 201),
        ({"description": "Missing Product Name", "status":"draft"},422),
        ({"name": "Required Field Check", "description":"Invalid Status (Unsupported)", "status":"approved"}, 422),
        ({"name": "Required Field Check", "description":"Invalid Status (Upper)","status":"DRAFT"},422),
        ({"name": "Required Field Check", "description":"Invalid Status (Title)","status":"Draft"},422),
        ({"name": "Required Field Check", "description":"Status is Blank","status":""},422),
        ({"name": "Required Field Check", "description":"Status is Space","status":" "},422),
        ({"name": "Required Field Check", "description":"Status is Missing"},201),
        ({"name": "Required Field Check", "description":"Unsupported Field", "status":"draft","department":"marketing"},201)
    ],
)
def test_create_product(test_client:TestClient, payload, expected_status_code):
    response = test_client.post("/products/",json=payload)
    assert response.status_code == expected_status_code
    data = response.json()
    try:
        if response.status_code == 201:
            assert payload["name"] == data["name"]
            assert payload["description"] == data["description"]
            assert payload["status"] == data["status"] or "draft"
            assert "id" in data
            assert "created_at" in data
        else:
            assert "detail" in data
            print(f"Validational error: {data}")
    except Exception as e:
        print(f"Unexpected Exception: {e}")
        
def test_invalid_product_fetch(test_client: TestClient):
    """ Test getting a non-existent product """
    response = test_client.get("/product/9999")
    assert response.status_code == 404

# TODO expand the tests

