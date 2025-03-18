import pytest
import seed_db
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    print("\n[INFO] Seeding test database...")
    seed_db.main()
    print("[INFO] Test database setup complete...")

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client