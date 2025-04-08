import pytest
from fastapi.testclient import TestClient

class TestPlans:
    @classmethod
    def setup_class(cls):
        # Load Test Data
        pass
    
    expected_test_plans = [
        {"name":"Test Plan A", "description":"Test Plan A Description", "status":"draft"},
        {"name":"Test Plan B", "description":"Test Plan B Description", "status":"draft"},
        {"name":"Test Plan C", "description":"Test Plan C Description", "status":"draft"},    
    ]
    
    @pytest.mark.parametrize("expected",[expected_test_plans])
    def test_get_all_test_plans(self,test_client: TestClient, expected):
        """Test retrieving all test plans"""
        response = test_client.get("/test_plans/")
        assert response.status_code == 200

        test_plans = response.json()
        assert isinstance(test_plans, list)

        for expected_test_plan in expected:
            match = next(
                (t for t in test_plans if
                    t["name"] == expected_test_plan["name"] and
                    t["description"] == expected_test_plan["description"] and
                    t["status"] == expected_test_plan["status"]),
                None
            )

        assert match is not None, f"Test Plans {expected_test_plan} not found in the response"

    @pytest.mark.parametrize("payload, expected_status_code, err_msg, err_desc",[
            ({"name": "Test Plan D", "description": "Test Plan D Description", "status": "draft"}, 201, "", ""),
            ({"name": "Test Plan E", "description": "Test Plan E Description", "status": "active"}, 201, "", ""),
            ({"name": "Test Plan F", "description": "Test Plan F Description", "status": "archived"}, 201, "",""),
            ({"description": "Missing Test Plan Name", "status":"draft"},422, "Field required", "Missing Test Plan Name"),
            ({"name": "Required Field Check", "description":"Invalid Status (Unsupported)", "status":"approved"}, 422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Invalid Status (Upper)","status":"DRAFT"},422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Invalid Status (Title)","status":"Draft"},422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Status is Blank","status":""},422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Status is Space","status":" "},422, "Input should be 'draft', 'active' or 'archived'", ""),
            ({"name": "Required Field Check", "description":"Status is Missing"},201, "", ""),
            ({"name": "Required Field Check", "description":"Unsupported Field", "status":"draft","department":"marketing"},201, "", "")
        ],                    
    )
    def test_create_test_plan(self,test_client: TestClient, payload, expected_status_code, err_msg,err_desc):
        """Test creating a new test plan"""
        response = test_client.post("/test_plans/", json=payload)
        assert response.status_code == expected_status_code
        data = response.json()
        # TODO: Split this into two - good and bad
        
        
        
    def test_update_test_plan(self,test_client: TestClient):
        """Test updating a test plan"""
        test_plan_id = 1  # Assuming test plan ID 1 exists
        update_data = {"name": "Updated Test Plan"}
        response = test_client.put(f"/test_plans/{test_plan_id}", json=update_data)
        if response.status_code == 200:
            assert response.json()["name"] == "Updated Test Plan"
        else:
            assert response.status_code == 404

    def test_delete_test_plan(self,test_client: TestClient):
        """Test deleting a test plan"""
        test_plan_id = 1  # Assuming test plan ID 1 exists
        response = test_client.delete(f"/test_plans/{test_plan_id}")
        assert response.status_code in [200, 404]  # Either deleted or not found

    def teardown_class(cls):
        # Clean something out or release resources
        pass