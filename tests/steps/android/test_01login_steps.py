import pytest
import allure
import random

from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.onboarding import OnboardingPage
from pages.android.login_page import LoginPage


scenarios('../../../features/login.feature')

TEST_EMAIL = 'julian@hotcake.app'

# Scenario: Display onboarding animation and start using the app
@allure.feature('Onboarding Functionality')
@pytest.mark.run(order=1)
@pytest.mark.login
@given('the app is launched for the first time')
def launch_app_first_time(driver, common_actions):
    onboarding_page = OnboardingPage(driver)
    onboarding_page.start_update()

@when('I select my language and click sure button')
def verify_onboarding_page(driver):
    onboarding_page = OnboardingPage(driver)
    onboarding_page.select_language()
    onboarding_page.confirm_language_selection()

@then('I can start using the app')


# Scenario: Select language and click contact cs
@allure.feature('Select Language and click contact cs')
@allure.story('Select Language and click contact cs')
@pytest.mark.run(order=2)
@pytest.mark.login
@given('the app is launched')
def login_page_loaded(driver):
    #driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Allow'})
    assert driver is not None, "App failed to launch"
    
@then('I can see the login page displayed')
def continue_to_login_page(driver):
    login_page = LoginPage(driver)
    login_page.continue_to_login_page()

@then('I can select my language and click sure button')
def select_language(driver):
    login_page = LoginPage(driver)
    login_page.select_language()
    
    
@then('I can click contact cs button and go back to the login page')
def click_contact_cs_button(driver):
    login_page = LoginPage(driver)
    login_page.click_contact_cs_button()
    
    
    
    
    
    

# Scenario: Click terms and conditions
@allure.feature('Click Terms and Conditions')
@allure.story('Click Terms and Conditions')
@pytest.mark.run(order=3)
@pytest.mark.login
@when('I click terms and conditions button')
def click_terms_and_conditions_button(driver):
    login_page = LoginPage(driver)
    login_page.click_terms_and_conditions_button()

@then('I can see the terms page and click the back button to go back to the start page')
def verify_terms_and_conditions_page(driver):
    login_page = LoginPage(driver)
    login_page.click_tc_back_button()
    login_page.continue_to_login_page()
    
@when('I click privacy button')
def click_privacy_button(driver):
    login_page = LoginPage(driver)
    login_page.click_privacy_button()

@then('I can see the privacy page and click the back button to go back to the start page')
def verify_privacy_page(driver):
    login_page = LoginPage(driver)
    login_page.click_privacy_back_button()
    login_page.continue_to_login_page()




# Scenario: Unsuccessful login with invalid email
@allure.feature('Login Functionality')
@allure.story('Unsuccessful login with invalid email')
@pytest.mark.run(order=4)
@pytest.mark.login
@when(parsers.parse('the user enters an invalid email "{email}"'))
def login_with_invalid_email(driver, email):
    login_page = LoginPage(driver)
    login_page.login_with_invalid_email(email)

@then(parsers.parse('the user should see an invalid email error message "{error_message}"'))
def verify_invalid_email_error(driver, error_message):
    login_page = LoginPage(driver)
    assert login_page.get_email_error_message() == error_message, "Invalid email error message not shown"
    login_page.click_login_cancel_button()


# Scenario: Login Unregistered Email
@allure.feature('Login Unregistered Email')
@allure.story('Login Unregistered Email')
@pytest.mark.run(order=5)
@pytest.mark.login
@when(parsers.parse('the user enters an unregistered email "{email}"'))
def login_with_unregistered_email(driver, email):
    login_page = LoginPage(driver)
    login_page.login_with_unregistered_email(email)
    
@then(parsers.parse('the user should see an popup window with email not registered "{error_message}"'))
def verify_unregistered_email_error(driver, error_message):
    login_page = LoginPage(driver)
    assert login_page.error_unregistered_message() == error_message, "Unregistered email error message not shown"
    login_page.click_login_cancel_button()


# Scenario: Unsuccessful login with invalid verification code
@allure.feature('Unsuccessful login with invalid verification code')
@allure.story('Unsuccessful login with invalid verification code')
@pytest.mark.run(order=6)
@pytest.mark.login
@when(parsers.parse('the user enters an invalid verification code "{email}" "{ver_code}"'))
def login_with_invalid_ver_code(driver, email, ver_code):
    login_page = LoginPage(driver)
    login_page.login_with_valid_email(email)
    login_page.login_with_invalid_ver_code(ver_code)
    
@then(parsers.parse('the user should see an invalid verification code error message "{error_message}"'))
def verify_invalid_ver_code_error(driver, error_message):
    login_page = LoginPage(driver)
    assert login_page.error_ver_window() == error_message, "Invalid verification window not shown"
    login_page.click_login_cancel_button()
    

# Scenario: Modify email from verification code page
@allure.feature('Modify email from verification code page')
@allure.story('Modify email from verification code page')
@pytest.mark.run(order=7)
@pytest.mark.login
@when(parsers.parse('the user clicks modify email button "{email}"'))
def click_modify_email_button(driver, email):
    login_page = LoginPage(driver)
    login_page.login_with_valid_email(email)
    login_page.click_modify_email_button()
    
@then(parsers.parse('the user can enter valid email again "{email}"'))
def enter_another_valid_email(driver, email):
    login_page = LoginPage(driver)
    login_page.login_with_another_valid_email(email)

@then('the user should be on verification code page again')
def verify_verification_code_page(driver):
    login_page = LoginPage(driver)
    assert login_page.is_verification_code_page(), "User is not on verification code page"
    login_page.click_login_cancel_button()


# Scenario: Successful login
@allure.feature('Successful login')
@allure.story('Successful login')
@pytest.mark.run(order=8)
@pytest.mark.login
@when(parsers.parse('the user enters valid credentials "{email}" "{ver_code}"'))
def login_with_valid_credentials(driver, email, ver_code):
    login_page = LoginPage(driver)
    login_page.login(email, ver_code)

@then('the user should be logged in successfully')
def verify_login_success(driver):
    login_page = LoginPage(driver)
    login_page.is_logged_in(), "Failed to log in successfully"
    
    