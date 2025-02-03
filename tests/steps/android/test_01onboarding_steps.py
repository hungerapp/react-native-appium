import pytest
import time
import allure

from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import scenarios, given, when, then

"""order=1"""

scenarios('../../../features/onboarding.feature')



@allure.feature('Onboarding Functionality')
@pytest.mark.run(order=1)
@pytest.mark.onboarding
@given('the app is launched for the first time')
def launch_app_first_time(driver):
    assert driver is not None, "App failed to launch"

    onboarding_animation = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.ImageView")')
  
    assert onboarding_animation is not None, "Onboarding animation not found"

    #driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Allow'})

@when('I select my language and click sure button')
def verify_onboarding_page(driver):
    """Verify navigation to the onboarding page."""
    #time.sleep(2)
    select_language_element = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.view.ViewGroup").instance(19)')
    select_language_element.click()
    confirm_button_element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='確定')
    confirm_button_element.click()

@then('I can start using the app')
def start_using_app(driver):
    """Verify that user can start using the app."""
    language_setting_btn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='語言設定')
    contact_cs_btn = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("聯繫客服")')

    assert language_setting_btn.is_displayed(), "Language setting button not found"
    assert contact_cs_btn.is_displayed(), "Contact customer service button not found"
    assert driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='開始使用') is not None, "Start using the app button not found"
    # click button move to login step
    #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='開始使用').click()
