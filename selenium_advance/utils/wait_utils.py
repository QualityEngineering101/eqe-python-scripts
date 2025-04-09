from sqlite3 import Time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException

class WaitUtils:
    
    DEFAULT_TIMEOUT = 10
    
    @staticmethod
    def _fail(message):
        raise AssertionError(f"[WaitUtils] {message}")
    
    @staticmethod
    def wait_for_element_visible(driver: WebDriver, locator: tuple, timeout: int = DEFAULT_TIMEOUT):
        try:
            return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            WaitUtils._fail(f"Element {locator} was not visible after {timeout} seconds")
    
    @staticmethod
    def wait_for_element_present(driver: WebDriver, locator: tuple, timeout: int = DEFAULT_TIMEOUT):
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            WaitUtils._fail(f"Element {locator} was not present after {timeout} seconds")
    
    @staticmethod
    def wait_for_url_contains(driver: WebDriver, text: str, timeout: int = DEFAULT_TIMEOUT):
        try:
            return WebDriverWait(driver, timeout).until(EC.url_contains(text))
        except TimeoutException:
            WaitUtils._fail(f"URL did not contain '{text}' after {timeout} seconds")
    
    @staticmethod
    def wait_for_text_in_element(driver: WebDriver, locator: tuple, text: str, timeout: int = DEFAULT_TIMEOUT):
        try:
            return WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element(locator))
        except TimeoutException:
            WaitUtils._fail(f"Element {locator} did not contain text '{text}' after {timeout} seconds")
    
    @staticmethod
    def safe_click(driver: WebDriver, locator: tuple, timeout: int = DEFAULT_TIMEOUT):
        element = WaitUtils.wait_for_element_visible(driver, locator, timeout)
        element.click()