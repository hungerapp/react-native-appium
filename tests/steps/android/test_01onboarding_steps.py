import pytest
import time
import allure

from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import scenarios, given, when, then

from pages.android.login_page import LoginPage
"""order=1"""

scenarios('../../../features/onboarding.feature')



@allure.feature('Onboarding Functionality')
@pytest.mark.run(order=1)
@pytest.mark.onboarding
@given('the app is launched for the first time')
def launch_app_first_time(driver):
    assert driver is not None, "App failed to launch"

    onboarding_language = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='選擇你的語言')
  
    assert onboarding_language.is_displayed(), "Onboarding language not found"

    #driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Allow'})

@when('I select my language and click sure button')
def verify_onboarding_page(driver):
    """Verify navigation to the onboarding page."""
    #time.sleep(2)
    select_language_element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='繁體中文, 繁體中文(台灣)')
    select_language_element.click()
    confirm_button_element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='確定')
    confirm_button_element.click()

@then('I can start using the app')
def start_using_app(driver):
    """Verify that user can start using the app."""
    login_page = LoginPage(driver)
    login_page.continue_to_login_page()
