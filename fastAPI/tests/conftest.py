import pytest
from fastapi.testclient import TestClient
from main import app
import os, sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import seed_db

@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    print("\n[INFO] Seeding test database...")
    seed_db.main()
    print("[INFO] Test database setup complete...")

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client