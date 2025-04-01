from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = None

@given('the browser is open')
def step_the_browser_is_open(context):
    global driver
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
@given('the user navigates to the {site}')
def step_the_user_navigates_to_the__site_(context, site):
    driver.get(site)
@when('the user enters {username} into the username field')
def step_the_user_enters__username__into_the_username_field(context, username):
    driver.find_element(By.NAME, "username").send_keys(username)
@when('the user enters {password} into the password field')
def step_the_user_enters__password__into_the_password_field(context, password):
    driver.find_element(By.NAME, "password").send_keys(password)
@when('the user clicks the login button')
def step_the_user_clicks_the_login_button(context):
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
@then('the user should see the Dashboard page')
def step_the_user_should_see_the_dashboard_page(context):
    time.sleep(2)
    assert "dashboard" in driver.current_url.lower()
@when('the user logs out')
def step_the_user_logs_out(context):
    driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Logout']").click()
@then('the user should see the login form')
def step_the_user_should_see_the_login_form(context):
    time.sleep(2)
    assert driver.find_element(By.NAME, "username").is_displayed()
    assert driver.find_element(By.NAME, "password").is_displayed()
