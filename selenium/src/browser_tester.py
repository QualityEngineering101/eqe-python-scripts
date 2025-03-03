"""
Automated Web UI Testing for OrangeHRM Demo Using Selenium and QEWebDriverHelper.

This script:
- Sets up Selenium WebDriver for Chrome, Edge, and Firefox using `QEWebDriverHelper`.
- Navigates to the OrangeHRM login page (`https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`).
- Automates the login process and verifies the presence of the "Dashboard" page.
- Executes the test in **headless mode** for all three browsers.

Dependencies:
- `selenium`
- `EQEUtils.QEWebDriverHelper`
- WebDriver binaries (managed via `webdriver-manager`)

Functions:
    execute_test(driver):
        Performs the login automation and verifies the expected page title.

Example Usage:
    Run the script directly to execute the test on Chrome, Edge, and Firefox.

Raises:
    ImportError: If `QEWebDriverHelper` is not found in the system path.
    selenium.common.exceptions.NoSuchElementException: If elements are not found during execution.

Notes:
- The **OrangeHRM demo site** is maintained by **SDET QA (YouTube)**.
- Debugging information is printed to validate the correct Python path.
"""
import sys, os, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
print (f"Python Path: {sys.path}") # Debugging to validate correct path
from EQEUtils.QEWebDriverHelper import QEWebDriverHelper
from selenium.webdriver.common.by import By

URL="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Sample test on website for demonstration purposes 
# OrangeHRM demo web site is brought to you by SDET QA (Youtube.com)
def execute_test(driver):
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    expected = 'Dashboard'
    actual = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    print(f'\nPass...Looking for {expected} and found {actual}') if expected == actual else print(f'\nFail...looking for {expected} and found {actual}')

# Create a new Chrome browser instance, get the driver, and run the test
browser_helper = QEWebDriverHelper(
    browser="Chrome", 
    url=URL, 
    mode="headless")
driver = browser_helper.get_driver()
execute_test(driver)
time.sleep(5)
driver.quit()

# Create a new Edge browser instance, get the driver, and run the test
browser_helper = QEWebDriverHelper(
    browser=QEWebDriverHelper.EDGE, 
    url=URL, 
    mode="headless")
driver = browser_helper.get_driver()
execute_test(driver)
time.sleep(5)
driver.quit()

# Create a new Firefox browser instance, get the driver, and run the test
browser_helper = QEWebDriverHelper(
    browser=QEWebDriverHelper.FIREFOX, 
    url=URL, 
    mode="headless")
driver = browser_helper.get_driver()
execute_test(driver)
time.sleep(5)
driver.quit()
