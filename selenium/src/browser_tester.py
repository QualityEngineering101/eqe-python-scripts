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
