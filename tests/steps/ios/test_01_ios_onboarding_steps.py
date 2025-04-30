import pytest
import time
import allure


from pytest_bdd import scenarios, given, when, then

from pages.ios.login_page import LoginPage
from pages.locators.ios.onboarding.onboarding_locators import OnboardingLocators

scenarios('../../../features/onboarding.feature')



@allure.feature('Onboarding Functionality')
@pytest.mark.run(order=1)
@pytest.mark.login
@given('the app is launched for the first time')
def launch_app_first_time(driver):
    
    try:
        start_updating_app = driver.find_element(*OnboardingLocators.START_UPDATE)
        start_updating_app.click()
        time.sleep(5)
        assert driver is not None, "App failed to launch"
    except:
        pass
    

    #driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Allow'})

@when('I select my language and click sure button')
def verify_onboarding_page(driver):
    select_language_element = driver.find_element(*OnboardingLocators.SELECT_LANGUAGE)
    select_language_element.click()
    confirm_button_element = driver.find_element(*OnboardingLocators.CONFIRM_BUTTON)
    confirm_button_element.click()

@then('I can start using the app')
def start_using_app(driver):
    login_page = LoginPage(driver)
    login_page.continue_to_login_page()
