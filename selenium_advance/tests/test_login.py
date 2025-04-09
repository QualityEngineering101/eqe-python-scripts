from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login_successfully("Admin","admin123")
    assert "dashboard" in driver.current_url.lower()
    
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login_with_invalid_credentials("invaliduser","invalidpass")
    assert "Invalid credentials" in login_page.get_error_message()
    