import pytest
from utils.driver_factory import create_driver

@pytest.fixture
def driver():
    driver = create_driver(headless=False)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()