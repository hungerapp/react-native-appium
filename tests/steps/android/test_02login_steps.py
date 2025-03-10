import pytest
import allure
import random

#from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import scenarios, given, when, then

from pages.android.login_page import LoginPage


scenarios('../../../features/login.feature')

TEST_EMAIL = 'ann@hunger.ai'
TEST_UNREGISTERED_EMAIL = 'ann@hotcake.com'
TEST_EMAIL_2 = 'ann@hotcake.app'
TEST_INVALID_EMAILS = [
    'ann@hotcake',  # invalid domain
    'ann@',         # missing domain
    'ann',          # missing @ and domain
    '@hunger.ai',   # missing username
    'ann@@hunger.ai' # multiple @ symbols
]
TEST_VER = '5556666'
TEST_INVALID_VER = '123456'


# Scenario: Select language
@allure.feature('Select Language and click contact cs')
@pytest.mark.run(order=2)
@pytest.mark.login
@given('the app is launched')
def login_page_loaded(driver):
    #driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Allow'})
    assert driver is not None, "App failed to launch"

@when('I select my language and click sure button')
def select_language(driver):
    login_page = LoginPage(driver)
    login_page.select_language()
    
@then('I can save the language setting and continue to the login page')
def continue_to_login_page(driver):
    login_page = LoginPage(driver)
    login_page.continue_to_login_page()
    
@when('I click contact cs button')
def click_contact_cs_button(driver):
    login_page = LoginPage(driver)
    login_page.click_contact_cs_button()
    
@then('I can see the contact cs page')
def verify_contact_cs_page(driver):
    pass
    
    
    
    
    

# Scenario: Click terms and conditions
@allure.feature('Click Terms and Conditions')
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
@when('the user enters an invalid email')
def login_with_invalid_email(driver):
    login_page = LoginPage(driver)
    login_page.login_with_invalid_email(random.choice(TEST_INVALID_EMAILS))

@then('the user should see an invalid email error message')
def verify_invalid_email_error(driver):
    login_page = LoginPage(driver)
    assert login_page.get_email_error_message() == "請填寫正確的電子郵件。", "Invalid email error message not shown"
    login_page.click_login_cancel_button()



@allure.feature('Login Unregistered Email')
@pytest.mark.run(order=5)
@pytest.mark.login
@when('the user enters an unregistered email')
def login_with_unregistered_email(driver):
    login_page = LoginPage(driver)
    login_page.login_with_unregistered_email(TEST_UNREGISTERED_EMAIL)
    
@then('the user should see an popup window with email not registered')
def verify_unregistered_email_error(driver):
    login_page = LoginPage(driver)
    assert login_page.error_unregistered_message() == "請檢查信箱是否輸入正確", "Unregistered email error message not shown"
    login_page.click_login_cancel_button()


# Scenario: Unsuccessful login with invalid verification code
@allure.story('Unsuccessful login with invalid verification code')
@pytest.mark.run(order=6)
@pytest.mark.login
@when('the user enters an invalid verification code')
def login_with_invalid_ver_code(driver):
    login_page = LoginPage(driver)
    login_page.login_with_valid_email(TEST_EMAIL)
    login_page.login_with_invalid_ver_code(TEST_INVALID_VER)
    
@then('the user should see an invalid verification code error message')
def verify_invalid_ver_code_error(driver):
    login_page = LoginPage(driver)
    assert login_page.error_ver_window() == "請檢查驗證通行碼是否輸入正確", "Invalid verification window not shown"
    login_page.click_login_cancel_button()
    

# Scenario: Modify email from verification code page
@allure.story('Modify email from verification code page')
@pytest.mark.run(order=7)
@pytest.mark.login
@when('the user clicks modify email button')
def click_modify_email_button(driver):
    login_page = LoginPage(driver)
    login_page.login_with_valid_email(TEST_EMAIL)
    login_page.click_modify_email_button()
    
@then('the user can enter valid email again')
def enter_another_valid_email(driver):
    login_page = LoginPage(driver)
    login_page.login_with_another_valid_email(TEST_EMAIL)

@then('the user should be on verification code page again')
def verify_verification_code_page(driver):
    login_page = LoginPage(driver)
    assert login_page.is_verification_code_page(), "User is not on verification code page"
    login_page.click_login_cancel_button()


# Scenario: Successful login
@allure.story('Successful login')
@pytest.mark.run(order=8)
@pytest.mark.login
@when('the user enters valid credentials')
def login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login(TEST_EMAIL, TEST_VER)

@then('the user should be logged in successfully')
def verify_login_success(driver):
    login_page = LoginPage(driver)
    login_page.is_logged_in(), "Failed to log in successfully"

    #click logout button-> move to personal page
    #login_page.click_logout_button()
  
    
    