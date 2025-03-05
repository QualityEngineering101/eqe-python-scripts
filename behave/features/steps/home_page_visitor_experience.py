from assertpy import assert_that
from behave import given, then
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import time


@given("I am on the home page")
def step_impl(context):
    assert_that(context.driver.current_url).is_equal_to(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )


@then("I should see the login form containing fields for username and password")
def step_impl(context):
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
            By.XPATH, "//label[normalize-space()='Password']"
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


@then('I should see a "Login" button')
def step_impl(context):
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
def step_impl(context):
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
def step_impl(context):
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
def step_impl(context):
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


@then("I should see links to OrangeHRM's social media pages")
def step_impl(context):
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


@then("The links should include LinkedIn, Facebook, and Twitter")
def step_impl(context):
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
        domain = str(parsed_url.netloc.strip())  # e.g. www.linkedin.com
        expected_domains_list = [str(d).strip() for d in expected_domains]
        print(
            f"Checking with assert_that() after casting: {domain} in {expected_domains_list}"
        )
        assert_that(domain).described_as(
            f"Social media link {index + 1} should be from an expected domain"
        ).is_in(list(expected_domains))
