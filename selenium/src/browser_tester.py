import sys, os, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
print (f"Python Path: {sys.path}") # Debugging to validate correct path
from EQEUtils.QEWebDriverHelper import QEWebDriverHelper

URL="https://wwww.amazon.com"

# Create a new browser instance and get the driver
browser_helper = QEWebDriverHelper(
    browser="Chrome", 
    url=URL, 
    mode="headed")
driver = browser_helper.get_driver()
time.sleep(5)
driver.quit()

browser_helper = QEWebDriverHelper(
    browser=QEWebDriverHelper.EDGE, 
    url=URL, 
    mode="headed")
driver = browser_helper.get_driver()
time.sleep(5)

browser_helper = QEWebDriverHelper(
    browser=QEWebDriverHelper.FIREFOX, 
    url=URL, 
    mode="headed")
driver = browser_helper.get_driver()
time.sleep(5)
driver.quit()

# Perform any additional actions with the driver
time.sleep(10)

# Close the browser
driver.quit()
