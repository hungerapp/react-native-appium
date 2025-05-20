# onboarding_flow.py

from pages.android.onboarding import OnboardingPage
from pages.android.login_page import LoginPage
from pages.android.personal_page import PersonalPage


def setup_flow(driver, email, ver_code):
    print("Running onboarding flow...")

    # --- STEP 1: Start update (可選)
    onboarding_page = OnboardingPage(driver)
    onboarding_page.start_update()

    # --- STEP 2: Select language
    onboarding_page.select_language()
    onboarding_page.confirm_language_selection()

    # --- STEP 3: Continue to login page
    login_page = LoginPage(driver)
    login_page.continue_to_login_page()

    # --- STEP 4: Login
    login_page.login(email, ver_code)

    # --- STEP 5: Verify login success
    login_page.is_logged_in(),

    # --- STEP 6: visit branch
    personal_page = PersonalPage(driver)
    personal_page.visit_branch()

