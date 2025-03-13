from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any

HRM_URL = "https://opensource-demo.orangehrmlive.com"
USERNAME = "Admin"
PASSWORD = "admin123"

# Initialize a webdriver (Chrome) and open site
# TODO add graceful waits, etc.
options = ChromeOptions()
options.add_argument("--headed")
options.add_argument("--log-level=3")  # Suppress DevTools & SSL errors
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-dev-shm-usage")
options.set_capability(
    "goog:loggingPrefs",
    {"performance": "OFF", "browser": "OFF", "driver": "OFF", "server": "OFF"},
)
# Initialize WebDriver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)
driver.maximize_window()
driver.get(HRM_URL)


def login():
    # Login to the Orange HRM site
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(
        USERNAME
    )
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(
        PASSWORD
    )
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


def navigate_to_users():
    # Navigate to user management section
    WebDriverWait(driver, 10).until(
        (
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )
    )
    admin_menu_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Admin']]"))
    )
    admin_menu_link.click()

    # Verify Page Name via Labels
    admin_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[normalize-space()='Admin']"))
    )
    user_management_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h6[normalize-space()='User Management']")
        )
    )
    if admin_label.text != "Admin":
        raise ValueError(f"Unexpected values found: Admin Label: '{admin_label.text}'")
    if user_management_label.text != "User Management":
        raise ValueError(f"User Management Label: '{user_management_label.text}'")
    # Select the User Management menu
    user_management = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'User Management')]")
        )
    )
    user_management.click()
    # Now select "Users" from the dropdown
    users_menu = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@class='oxd-topbar-body-nav-tab-link' and contains(text(), 'Users')]",
            )
        )
    )
    users_menu.click()


def extract_table_data() -> list[dict[str, Any]]:
    # Find the column headers and users
    column_headers = driver.find_elements(
        By.XPATH,
        "//div[@role = 'columnheader']",
    )
    data_cells = driver.find_elements(
        By.XPATH,
        "//div[@role='cell']//div[not(@class)]",
    )

    # Extract column headers (indexes 1 to 4)
    headers = [
        column_headers[i].text.strip().replace(" ","_") for i in range(1, min(5, len(column_headers)))
    ]

    # Extract data cells and organize into rows
    rows = []
    row_size = len(headers)  # Assuming each row has the same number of columns

    for j in range(
        0, len(data_cells), row_size
    ):  # Step through data in chunks of row_size
        row = [
            data_cells[k].text.strip()
            for k in range(j, min(j + row_size, len(data_cells)))
        ]
        rows.append(row)

    # Convert into a list of dictionaries
    return [dict(zip(headers, row)) for row in rows]
