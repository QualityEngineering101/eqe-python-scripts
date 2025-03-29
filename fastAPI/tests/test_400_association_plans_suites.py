import pytest
from fastapi.testclient import TestClient

class TestPlanSuiteAssociation:
    def setup_class(cls):
        # Load Test Data
        pass
    def test_associate_valid_test_suite(self,test_client: TestClient):
        # Test Plans and Test Suites must have status = "draft" or "active" (not "archived") 
        tp_id = 4
        ts_id = 4
        payload = {"test_plan_id":tp_id,"test_suite_id":ts_id}
        response = test_client.post(f"/test_plans/{tp_id}/associate_test_suite",json=payload)
        assert response.status_code == 200
        assert response.json() == {"message":"Test Suite successfully associated with a Test Plan"}

    def test_cannot_associate_archived_test_suite(self,test_client: TestClient):
        tp_id = 4
        ts_id = 6
        payload = {"test_plan_id":tp_id, "test_suite_id":ts_id} # TP 4 Active / TS 6 Archived
        response = test_client.post(f"/test_plans/{tp_id}/associate_test_suite", json=payload)
        assert response.status_code == 400
        assert response.json()["detail"] == "Archived test suites cannot be associated with test plans"
    def teardown_class(cls):
        # Clean something out or release resources
        pass