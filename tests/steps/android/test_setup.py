# onboarding_flow.py

from pages.android.login_page import LoginPage
from pages.locators.android.onboarding.onboarding_locators import OnboardingLocators

def setup_flow(driver, common_actions, email, ver_code):
    print("Running onboarding flow...")

    # --- STEP 1: Start update (可選)
    start_updating_app = common_actions.find_element(*OnboardingLocators.START_UPDATE)
    start_updating_app.click()

    # --- STEP 2: Select language

    select_language_element = common_actions.find_element(*OnboardingLocators.SELECT_LANGUAGE)
    select_language_element.click()
    confirm_button_element = common_actions.find_element(*OnboardingLocators.CONFIRM_BUTTON)
    confirm_button_element.click()

    # --- STEP 3: Continue to login page
    login_page = LoginPage(driver)
    login_page.continue_to_login_page()

    # --- STEP 4: Login
    login_page.login(email, ver_code)

    # --- STEP 5: Verify login success
    assert login_page.is_logged_in(), "❌ Failed to log in successfully"
    print("🎉 Login successful")
