import pytest
from fastapi.testclient import TestClient
from datetime import datetime

# Assumes the existing products are those created by the seed_db.py refresh
# Should  probably move this to later in the tests but other tests are already validating
# API responses so this is fine here for now.
class TestProducts:
    @classmethod
    def setup_class(cls):
        # Load Test Data
        pass
    expected_products = [
            {"name":"Product A", "description":"Product A Description", "status":"draft"},
            {"name":"Product B", "description":"Product B Description", "status":"draft"},
            {"name":"Product C", "description":"Product C Description", "status":"draft"},    
    ]
    @pytest.mark.parametrize("expected", [expected_products])
    def test_get_all_products(self,test_client:TestClient, expected):
        """ Testing the retrieval of all products """
        response = test_client.get("/products/")
        assert response.status_code == 200

        products = response.json()
        assert isinstance(products, list)

        for expected_product in expected:
            match = next(
                (p for p in products if 
                    p["name"] == expected_product["name"] and 
                    p["description"] == expected_product["description"] and
                    p["status"] == expected_product["status"]),
                None
            )
            assert match is not None, f"Product {expected_product} not found in response"
    
    # Parameterized create product test cases.
    @pytest.mark.parametrize(
        "payload, expected_status_code",
        [
            ({"name": "Product D", "description": "Product D Description", "status": "draft"}, 201),
            ({"name": "Product E", "description": "Product E Description", "status": "active"}, 201),
            ({"name": "Product F", "description": "Product F Description", "status": "archived"}, 201),
            ({"name": "Required Field Check", "description":"Status is Missing"},201),
            ({"name": "Required Field Check", "description":"Unsupported Field", "status":"draft","department":"marketing"},201)
        ],
    )
    def test_create_product_good(self,test_client:TestClient, payload, expected_status_code):
        response = test_client.post("/products/",json=payload)
        assert response.status_code == expected_status_code
        data = response.json()
        assert payload["name"] == data["name"]
        assert payload["description"] == data["description"]
        assert "status" in data, f"Missing 'status' key in response: {data}" 
        assert payload.get("status","draft") == data["status"]
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data
        

    @pytest.mark.parametrize(
        "payload, expected_status_code, err_msg, err_desc",
        [
            ({"description": "Missing Product Name", "status":"draft"},422, "Field required", "Missing Product Name"),
        ],
    )
    def test_create_product_bad_name(self, test_client:TestClient, payload, expected_status_code, err_msg,err_desc):
        response = test_client.post("/test_plans/",json=payload)
        assert response.status_code == expected_status_code
        data = response.json()
        assert response.status_code == expected_status_code
        assert data["detail"][0]["msg"] == err_msg
        assert data["detail"][0]["input"]["description"] == err_desc

    @pytest.mark.parametrize(
        "payload, expected_status_code, err_msg, err_desc",
        [
            ({"name": "Required Field Check", "description":"Invalid Status (Unsupported)", "status":"approved"}, 422, "Input should be 'draft', 'active' or 'archived'", "'draft', 'active' or 'archived'"),
            ({"name": "Required Field Check", "description":"Invalid Status (Upper)","status":"DRAFT"},422, "Input should be 'draft', 'active' or 'archived'", "'draft', 'active' or 'archived'"),
            ({"name": "Required Field Check", "description":"Invalid Status (Title)","status":"Draft"},422, "Input should be 'draft', 'active' or 'archived'", "'draft', 'active' or 'archived'"),
            ({"name": "Required Field Check", "description":"Status is Blank","status":""},422, "Input should be 'draft', 'active' or 'archived'", "'draft', 'active' or 'archived'"),
            ({"name": "Required Field Check", "description":"Status is Space","status":" "},422, "Input should be 'draft', 'active' or 'archived'", "'draft', 'active' or 'archived'"),
        ],
    )
    def test_create_product_invalid_status(self, test_client:TestClient, payload, expected_status_code, err_msg,err_desc):
        response = test_client.post("/test_plans/",json=payload)
        assert response.status_code == expected_status_code
        data = response.json()
        assert response.status_code == expected_status_code
        assert data["detail"][0]["msg"] == err_msg
        assert data["detail"][0]["ctx"]["expected"] == err_desc

    @pytest.mark.parametrize(
        "id, expected_status_code, expected_name, expected_desc, expected_status",
        [
            (1, 200, expected_products[0]["name"],expected_products[0]["description"], expected_products[0]["status"]), 
            (2, 200, expected_products[1]["name"],expected_products[1]["description"], expected_products[1]["status"]), 
            (3, 200, expected_products[2]["name"],expected_products[2]["description"], expected_products[2]["status"]), 
        ])
    def test_get_product_by_id(self,test_client:TestClient, id, expected_status_code, expected_name,expected_desc,expected_status):
        """ Test retrieving a product by ID """
        response = test_client.get(f"/products/{id}")
        assert response.status_code == expected_status_code
        data = response.json()
        assert data["id"] == id
        assert data["name"] == expected_name
        assert data["description"] == expected_desc
        assert data["status"] == expected_status
        assert "created_at" in data
        try:
            create_at = datetime.fromisoformat(data["created_at"].replace("Z","+00:00"))
        except ValueError:
            pytest.fail(f"create_at is not a valid ISO 8601 timestamp: {data['created_at']}")

        assert data["updated_at"] is None

    @pytest.mark.parametrize(
        "id, expected_status_code, err_msg, err_desc",
        [
            (9999, 404, "Not Found", ""), # Non-existent product id
        ])
    def test_invalid_product_fetch(self,test_client: TestClient, id, expected_status_code, err_msg, err_desc):
        """ Test getting a non-existent product """
        response = test_client.get("/product/{id}")
        data = response.json()
        assert response.status_code == expected_status_code
        if "detail" in data: assert data["detail"] == err_msg
        
    @classmethod
    def teardown_class(cls):
        # Clean something out or release resources
        pass


