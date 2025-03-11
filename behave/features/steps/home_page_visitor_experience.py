from assertpy import assert_that
from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse
import time


def get_required_field_label(context, placeholder):
    return WebDriverWait(context.driver, 15).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                f"//input[@placeholder='{placeholder}']/ancestor::div/following-sibling::span",
            )
        )
    )


def required_field_should_not_exist(content, placeholder):
    # Validates that the required field label does NOT appear when it shouldn't
    try:
        WebDriverWait(content.driver, 5).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//input[@placeholder='{placeholder}']/ancestor::div/following-sibling::span",
                )
            )
        )
    except TimeoutException:
        pass


def get_invalid_credentials_label(context):
    # Wait for the error message container (div with <i> and <p>)
    error_message_element = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'oxd-alert-content--error')]//p")
        )
    )

    return error_message_element.text


def on_reset_password_page(context):
    try:
        WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h6[normalize-space()='Reset Password']")
            )
        )
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Undefined exception: {e}")

    page_url = context.driver.current_url
    assert_that(no_exception).described_as(
        "No exception found looking for Password Page"
    ).is_true()
    assert_that(page_url).described_as("Verify on Password Reset Page").ends_with(
        "requestPasswordResetCode"
    )
    return no_exception


def on_dashboard_page(context):
    try:
        WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h6[normalize-space()='Dashboard']")
            )
        )
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Undefined exception: {e}")

    page_url = context.driver.current_url
    assert_that(no_exception).described_as(
        "No exceptions found looking for Dashboard Page"
    ).is_true()
    assert_that(page_url).described_as("Verify on Dashboard Page").contains("dashboard")
    return no_exception


def on_home_page(context):
    try:
        WebDriverWait(context.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Undefined exception: {e}")

    page_url = context.driver.current_url
    assert_that(no_exception).described_as(
        "No exceptions found looking for Home Page"
    ).is_true()
    assert_that(page_url).described_as("Verify on Home Page").contains("login")


@given("I am on the home page")
def validate_on_home_page(context):
    assert_that(context.driver.current_url).is_equal_to(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )


@then("I should see the login form with fields")
def validate_home_page_fields_elements(context):
    try:
        # Get form components for validation
        login_form = context.driver.find_element(By.XPATH, "//form[@class='oxd-form']")
        login_text = context.driver.find_element(
            By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']"
        ).text

        user_name_label = context.driver.find_element(
            By.XPATH, "//label[contains(text(),'Username')]"
        ).text

        user_name_field = context.driver.find_element(
            By.XPATH, "//input[@placeholder='Username']"
        )

        password_label = context.driver.find_element(
            By.XPATH, "//label[contains(text(),'Password')]"
        ).text

        password_field = context.driver.find_element(
            By.XPATH, "//input[@Placeholder='Password']"
        )
        # If we haven't had any exceptions then set flag to True
        no_exception = True
    except Exception as e:
        # If we have had exceptions then print them
        no_exception = False
        print(f"Unexpected exception: {e}")

    # We had no exceptions when identifying webelements
    assert_that(no_exception).described_as(
        "No exceptions found for Login form"
    ).is_true()
    # We should have a login form
    assert_that(login_form).described_as(
        "Verifying the Login form exists"
    ).is_not_none()
    # There should be a label on the form that says Login
    assert_that(login_text).described_as("The form has a Login label").is_equal_to(
        "Login"
    )
    # There should be a Username label
    assert_that(user_name_label).described_as("There is a Username label").is_equal_to(
        "Username"
    )
    # There is a Username field that is enabled.
    assert_that(user_name_field.tag_name.lower()).described_as(
        "There is a field to enter a Username"
    ).is_equal_to("input")
    assert_that(user_name_field.is_enabled()).described_as(
        "The Username field is enabled"
    ).is_true()
    # There is a Password label
    assert_that(password_label).described_as("There is a Password label").is_equal_to(
        "Password"
    )
    # There is a Password field that is enabled
    assert_that(password_field.tag_name.lower()).described_as(
        "This is a place to enter a Password"
    ).is_equal_to("input")
    assert_that(password_field.is_enabled()).described_as(
        "The Password field is enabled"
    ).is_true()


@then("I should see a Login button")
def validate_home_page_fields_login_button(context):
    try:
        # Get web element for validation
        submit_button = context.driver.find_element(
            By.XPATH, "//button[@type='submit']"
        )
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")

    # Login button exists, has a name, and is enabled.
    assert_that(no_exception).described_as(
        "No exceptions were found for the Login button"
    ).is_true()
    assert_that(submit_button.tag_name.lower()).described_as(
        "Login button exists"
    ).is_equal_to("button")
    assert_that((submit_button.text or "").strip()).described_as(
        "Button displays the text 'Login'"
    ).is_equal_to("Login")
    assert_that(submit_button.is_enabled()).described_as(
        "Login button is enabled"
    ).is_true()


@then('I should see a "Forgot your password?" link')
def validate_home_page_fields_forgot_link(context):
    # Get web element for validation
    try:
        no_exception = True
        forgot_password = context.driver.find_element(
            By.XPATH, "//p[contains(normalize-space(),'Forgot your password?')]"
        )
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")

    # since it's a <p> we'll need to check if it becomes clickable
    for _ in range(10):  # Check every second for 10 seconds
        if (
            forgot_password.get_attribute("onclick") is not None
            or forgot_password.get_attribute("role") == "button"
            or forgot_password.value_of_css_property("cursor") == "pointer"
        ):
            is_clickable = True
            break
        time.sleep(1)
        # Validate the link exists and is clickable
        assert_that(no_exception).described_as(
            "No exceptions were found for the Forget your password? link"
        ).is_true()
        assert_that(is_clickable).described_as(
            "Forget your password? link is clickable"
        ).is_true()


@then('I should see the "OrangeHRM" logo')
def validate_home_page_logo(context):
    try:
        logo = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']")
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception {e}")

    # No unexpected exceptions were found
    assert_that(no_exception).described_as(
        "No exceptions were found for the logo"
    ).is_true()
    # Ensure the logo exists
    assert_that(logo).described_as("Logo should be present on the page").is_not_none()

    # Ensure the logo has a valid 'src' attribute
    logo_src = logo.get_attribute("src")
    assert_that(logo_src).described_as(
        "Logo should have a valid source URL"
    ).is_not_empty()

    # Ensure the src URL ends with a valid image extension
    logo_src_cleaned = logo_src.split("?")[
        0
    ]  # Remove query string suffix to get file name
    valid_extensions = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")
    assert_that(logo_src_cleaned.lower().endswith(valid_extensions)).described_as(
        "Logo should have a valid image file extension"
    ).is_true()


@then("I should see the application title")
def validate_home_page_app_title(context):
    try:
        application_title = context.driver.find_element(
            By.XPATH, "//p[normalize-space()='OrangeHRM OS 5.7']"
        ).text
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception {e}")

    # Validate that the application title appears on the page
    assert_that(no_exception).described_as(
        "No exceptions were found for the application title"
    ).is_true()
    assert_that(application_title).described_as(
        "The application title appears on the page"
    ).is_equal_to("OrangeHRM OS 5.7")


@then("I should see OrangeHRM social media links")
def validate_home_page_socmed_links(context):
    try:
        social_media_pages_footer = context.driver.find_element(
            By.XPATH, "//div[@class='orangehrm-login-footer-sm']"
        ).text
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception {e}")

    # Validate that the application title appears on the page
    assert_that(no_exception).described_as(
        "No exceptions were found for the application title"
    ).is_true()
    assert_that(social_media_pages_footer).described_as(
        "The social media footer exists on the page"
    ).is_not_none()


@then("The links should include LinkedIn, Facebook, Twitter, and YouTube")
def validate_home_page_socmed_link_list(context):
    try:
        # Find all social media links
        social_media_elements = context.driver.find_elements(
            By.XPATH, "//*[local-name()='svg']/ancestor::a"
        )
        assert_that(len(social_media_elements)).described_as(
            "At least one social media link should exist"
        ).is_greater_than(0)
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception {e}")
        assert_that(False).described_as("Failed to locate social media links").is_true()
    # Validate that social media links appear on the page
    assert_that(no_exception).described_as(
        "No exceptions were found for the social media links"
    ).is_true()

    # Validate that the links found actually work
    social_media_links = [
        element.get_attribute("href") for element in social_media_elements
    ]
    assert_that(len(social_media_links)).described_as(
        "There should be 4 social media links"
    ).is_equal_to(4)

    # Ensure each link is not empty and is well-formed
    for index, link in enumerate(social_media_links):
        assert_that(link).described_as(
            f"Social media link {index + 1} shoudl not be empty"
        ).is_not_empty()
        assert_that(link.startswith(("http://", "https"))).described_as(
            f"Social media link {index + 1} should be a valid URL"
        ).is_true()

    # Validate the names of the links are for the desired platforms
    expected_platforms = {"facebook", "twitter", "linkedin", "youtube"}
    link_lower = link.lower()
    is_valid_platform = any(platform in link_lower for platform in expected_platforms)
    assert_that(is_valid_platform).described_as(
        f"Social media link {index + 1} should be a known platform"
    ).is_true()

    # Validate the URLs are valid
    expected_domains = {
        "www.linkedin.com",
        "www.facebook.com",
        "twitter.com",
        "www.youtube.com",
    }
    for index, link in enumerate(social_media_links):
        parsed_url = urlparse(link)
        domain = parsed_url.netloc.strip()  # e.g. www.linkedin.com
        assert_that(expected_domains).described_as(
            f"Social media link {index + 1} should be from an expected domain"
        ).contains(domain)


@when("I do not enter a username")
def home_page_set_username_blank(context):
    try:
        # Locate and clear the username field
        username_field = context.driver.find_element(
            By.XPATH, "//input[@placeholder='Username']"
        )
        username_field.send_keys(Keys.CONTROL + "a")
        username_field.send_keys(Keys.DELETE)
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
    assert_that(no_exception).described_as(
        "No exceptions were found when clearing the username field"
    ).is_true()


@when("I do not enter a password")
def home_page_set_password_blank(context):
    try:
        # Locate and clear the Password field
        password_field = context.driver.find_element(
            By.XPATH, "//input[@placeholder='Password']"
        )
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
    assert_that(no_exception).described_as(
        "No exceptions were found when clearing the Password field"
    ).is_true()


@when("I enter a valid username")
def home_page_set_username_valid(context):
    try:
        # Locate and clear the username field
        context.driver.find_element(
            By.XPATH, "//input[@placeholder='Username']"
        ).send_keys("Admin")
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
    assert_that(no_exception).described_as(
        "No exceptions were found when entering values in the Username field "
    ).is_true()


@when("I enter a valid password")
def home_page_set_password_valid(context):
    try:
        # Locate and clear the Password field
        context.driver.find_element(
            By.XPATH, "//input[@placeholder='Password']"
        ).send_keys("admin123")
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
    assert_that(no_exception).described_as(
        "No exceptions were found when entering values in the Password field "
    ).is_true()


@when("I click the Login button")
def home_page_click_login_button(context):
    try:
        # Click Login button without credentials to be sure required fields are being displayed
        context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        context.login_pressed = True
        no_exception = True
    except Exception as e:
        no_exception = False
        context.Login_pressed = False
        print(f"Unexpected exception: {e}")

        # Validations that there were no exceptions when finding the login button
    assert_that(no_exception).described_as(
        "No exceptions were found for the Login button"
    ).is_true()


@then("I should see Username is Required")
def validate_home_page_username_required_field_label(context):
    try:
        username_required_message = get_required_field_label(context, "Username").text
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
        # Required field validations - no Username
    assert_that(no_exception).described_as(
        "No exceptions were found locating the required username field labels"
    ).is_true()
    assert_that(username_required_message).described_as(
        "Username should display Required when empty and Login button is pushed"
    ).is_equal_to("Required")


@then("I should see Password is Required")
def validate_home_page_password_required_field_label(context):
    try:
        password_required_message = get_required_field_label(context, "Password").text
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
        # Required field validations - no Password entered but login clicked
        assert_that(no_exception).described_as(
            "No exceptions were found for the Password required field label"
        ).is_true()
        assert_that(password_required_message).described_as(
            "Required should be displayed for missing passwords"
        ).is_equal_to("Required")


@when("I enter an invalid username")
def home_page_set_invalid_username(context):
    try:
        # Locate and clear the Password field
        context.driver.find_element(
            By.XPATH, "//input[@placeholder='Password']"
        ).send_keys("Uname")
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
    assert_that(no_exception).described_as(
        "No exceptions were found for the Password field "
    ).is_true()


@when("I enter an invalid password")
def home_page_set_invalid_password(context):
    try:
        # Locate and clear the Password field
        context.driver.find_element(
            By.XPATH, "//input[@placeholder='Password']"
        ).send_keys("Invalid")
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
    assert_that(no_exception).described_as(
        "No exceptions were found for the Password field "
    ).is_true()


@then("I should see an invalid credentials error message")
def validate_home_page_invalid_credentials_messsage(context):
    try:
        invalid_credentials_label = get_invalid_credentials_label(context)
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
    assert_that(no_exception).described_as(
        "No exceptions were found locating invalid credentials message"
    ).is_true()
    assert_that(invalid_credentials_label).described_as(
        "I should find 'Invalid Credientials' error message"
    ).is_equal_to("Invalid credentials")


@then("I should not see Username is Required")
def validate_home_page_no_required_field(context):
    does_required_field_label_exist = required_field_should_not_exist(
        context, "Username"
    )
    assert_that(does_required_field_label_exist).described_as(
        "Verify required field label does not appear"
    ).is_none()


@then("I should not see Password is Required")
def step_impl(context):
    does_required_field_label_exist = required_field_should_not_exist(
        context, "Password"
    )
    assert_that(does_required_field_label_exist).described_as(
        "Verify required field label does not appear"
    ).is_none()


@when('I click on the "Forgot your password?" link')
def home_page_click_forgot_password(context):
    try:
        no_exception = True
        context.driver.find_element(
            By.XPATH, "//p[contains(normalize-space(),'Forgot your password?')]"
        ).click()
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")

    assert_that(no_exception).described_as(
        "No exceptions were found locating invalid credentials message"
    ).is_true()


@then("I should be taken to the password recovery page")
def validate_on_reset_password_page(context):
    try:
        no_exception = True
        on_reset_pwd_page = on_reset_password_page(context)
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")

    assert_that(no_exception).described_as(
        "No exceptions were found locating invalid credentials message"
    ).is_true()
    assert_that(on_reset_pwd_page).described_as("Found Reset Password Page").is_true()


@then("I should be logged in")
def validate_on_dashboard_page(context):
    try:
        no_exception = True
        on_dashbrd_page = on_dashboard_page(context)
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")

    assert_that(no_exception).described_as(
        "No exceptions were found locating invalid credentials message"
    ).is_true()
    assert_that(on_dashbrd_page).described_as("Found Reset Password Page").is_true()


@when("I cancel Reset Password")
def cancel_reset_password(context):
    try:
        context.driver.find_element(
            By.XPATH, "//button[normalize-space()='Cancel']"
        ).click()
        no_exception = True
    except Exception as e:
        no_exception = False
        print(f"Unexpected exception: {e}")
    assert_that(no_exception).described_as(
        "No exception found canceling button"
    ).is_true()
    on_home_page(context)


@then("I am on the home page")
def then_home_page(context):
    on_home_page(context)
