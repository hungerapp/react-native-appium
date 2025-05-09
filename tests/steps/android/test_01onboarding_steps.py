import pytest
import time
import allure


from pytest_bdd import scenarios, given, when, then

from pages.android.login_page import LoginPage
from pages.locators.android.onboarding.onboarding_locators import OnboardingLocators


scenarios('../../../features/onboarding.feature')


@allure.feature('Onboarding Functionality')
@pytest.mark.run(order=1)
@pytest.mark.login
@given('the app is launched for the first time')
def launch_app_first_time(driver,common_actions):
    
    try:
        start_updating_app = common_actions.find_element(*OnboardingLocators.START_UPDATE)
        start_updating_app.click()
        assert driver is not None, "App failed to launch"
    except:
        pass
    

    #driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Allow'})

@when('I select my language and click sure button')
def verify_onboarding_page(common_actions):
    select_language_element = common_actions.find_element(*OnboardingLocators.SELECT_LANGUAGE)
    select_language_element.click()
    confirm_button_element = common_actions.find_element(*OnboardingLocators.CONFIRM_BUTTON)
    confirm_button_element.click()

@then('I can start using the app')
def start_using_app(common_actions):
    login_page = LoginPage(common_actions)
    login_page.continue_to_login_page()
