import pytest
from fastapi.testclient import TestClient

class TestProducts:
    # Example of a using a Test Class rather than just test methods.
    # If this were going to be mainttained with purpose, I would expand the class to inherit
    # from a base test class, log all assertions, etc. 

    def test_get_all_products(self,test_client:TestClient):
        """ Testing the retrieval of all products """
        response = test_client.get("/products/")
        assert response.status_code == 200
        assert isinstance(response.json(),list)

    # Parameterized create product test cases.
    @pytest.mark.parametrize(
        "payload, expected_status_code, err_msg, err_desc",
        [
            ({"name": "Product D", "description": "Product D Description", "status": "draft"}, 201, "", ""),
            ({"name": "Product E", "description": "Product E Description", "status": "active"}, 201, "", ""),
            ({"name": "Product F", "description": "Product F Description", "status": "archived"}, 201, "",""),
            ({"description": "Missing Product Name", "status":"draft"},422, "Field required", "Missing Product Name"),
            ({"name": "Required Field Check", "description":"Invalid Status (Unsupported)", "status":"approved"}, 422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Invalid Status (Upper)","status":"DRAFT"},422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Invalid Status (Title)","status":"Draft"},422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Status is Blank","status":""},422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Status is Space","status":" "},422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Status is Missing"},201, "", ""),
            ({"name": "Required Field Check", "description":"Unsupported Field", "status":"draft","department":"marketing"},201, "", "")
        ],
    )
    def test_create_product(self, test_client:TestClient, payload, expected_status_code, err_msg, err_desc):
        response = test_client.post("/products/",json=payload)
        assert response.status_code == expected_status_code
        data = response.json()
        if response.status_code == 201:
            assert payload["name"] == data["name"]
            assert payload["description"] == data["description"]
            assert "status" in data, f"Missing 'status' key in response: {data}" 
            assert payload.get("status","draft") == data["status"]
            assert "id" in data
            assert "created_at" in data
        elif response.status_code == 422:
            element = data["detail"][0]
            assert element["msg"] == err_msg
            if "ctx" not in element:
                assert element["input"]["description"] == err_desc
        else:
            assert "detail" in data
            print(f"Validational error: {data}")

    @pytest.mark.parametrize(
        "id, expected_status_code, err_msg, err_desc",
        [
            (4, 200, "", ""), 
            (5, 200, "", ""),
            (6, 200, "", ""),
        ])
    def test_get_product_by_id(self,test_client:TestClient, id, expected_status_code, err_msg, err_desc):
        """ Test retrieving a product by ID """
        response = test_client.get(f"/products/{id}")
        assert response.status_code == expected_status_code
        data = response.json()
        assert data["id"] == id
        print(f"\n\nData: {data}")

            
    @pytest.mark.parametrize(
        "id, expected_status_code, err_msg, err_desc",
        [
            (9999, 404, "Not Found", ""), # Non-existent product id
            (1, 404, "Not Found","") # Deleted transaction is no longer available
        ])
    def test_invalid_product_fetch(self,test_client: TestClient, id, expected_status_code, err_msg, err_desc):
        """ Test getting a non-existent product """
        response = test_client.get("/product/{id}")
        data = response.json()
        assert response.status_code == expected_status_code
        if "detail" in data: assert data["detail"] == err_msg
 


