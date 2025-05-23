import pytest
import allure


from pytest_bdd import scenarios, given, when, then

from pages.android.onboarding import OnboardingPage
from pages.android.login_page import LoginPage

scenarios('../../../features/onboarding.feature')

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
def start_using_app(driver):
    login_page = LoginPage(driver)
    login_page.continue_to_login_page()