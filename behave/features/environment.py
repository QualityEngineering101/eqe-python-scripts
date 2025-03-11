from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


import requests
import time
import sys


def is_page_in_english(driver) -> bool:
    # Detects the language on the page
    try:
        # Wait for the Login button to be visible before checking its text value
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        login_button_name = login_button.text.strip()
        return login_button_name == "Login"  # Returns True if English, else False

    except Exception as e:
        print(f"Unexpected exception {e}")
        return False


def is_site_available(url) -> bool:
    # Checks to see if the site is up before trying executing the logic
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200  # Return True if site is up
    except requests.RequestException as e:
        print(f"Site check failed: {e}")
        return False  # Return False if site is down


def before_all(context):
    site_url = "https://opensource-demo.orangehrmlive.com"
    if not is_site_available(site_url):
        print(f"ERROR: {site_url} is unavailable. Aborting tests.")
        sys.exit(1)  # Cleanly exit without launching selenium

    browser = context.config.userdata.get("browser", "chrome").lower()
    headless = context.config.userdata.get("headless", "false").lower() == "true"

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
        options.add_argument("--log-level=3")  # Suppress DevTools & SSL errors
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-dev-shm-usage")
        context.driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        options.add_argument("--log-level=3")  # Suppress DevTools & SSL errors
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-dev-shm-usage")
        context.driver = webdriver.Edge(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height-1080")
        options.add_argument("--log-level=3")  # Suppress DevTools & SSL errors
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-dev-shm-usage")
        context.driver = webdriver.Firefox(options=options)
    else:
        print(f"Unsupported browser: {browser}")
        sys.exit(1)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.get(site_url)
    WebDriverWait(context.driver, 10).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

    # Need to check the language of an element to be sure it's in English,
    # otherwise refresh the page a few times until it is English (demo-site Feature)
    for _ in range(10):
        # If the page is not in English
        if not is_page_in_english(context.driver):
            print("Environments.py -> before_all: Page is not in English")
            context.driver.refresh()
            WebDriverWait(context.driver, 10).until(
                lambda driver: driver.execute_script("return document.readyState")
                == "complete"
            )
            time.sleep(2)
        else:
            break


def after_all(context):
    if context.driver:
        context.driver.delete_all_cookies()
        context.driver.quit()
        context.driver = None
