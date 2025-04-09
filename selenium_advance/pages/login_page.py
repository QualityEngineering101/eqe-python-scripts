from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.wait_utils import WaitUtils

class LoginPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text") # Invalid Login
    DASHBOARD_MENU = (By.CSS_SELECTOR, "span.oxd-userdropdown-tab")
    
    def enter_username(self, username: str):
        WaitUtils.wait_for_element_visible(self.driver, self.USERNAME_INPUT).send_keys(username)
        
    def enter_password(self, password: str):
        WaitUtils.wait_for_element_visible(self.driver, self.PASSWORD_INPUT).send_keys(password)
    
    def click_login(self):
        WaitUtils.safe_click(self.driver, self.LOGIN_BUTTON)
        
    def login_successfully(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        WaitUtils.wait_for_element_visible(self.driver, self.DASHBOARD_MENU)
        
    def login_with_invalid_credentials(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        WaitUtils.wait_for_element_visible(self.driver,self.ERROR_MESSAGE)
        
    def get_error_message(self) -> str:
        return WaitUtils.wait_for_element_visible(self.driver, self.ERROR_MESSAGE).text
    
