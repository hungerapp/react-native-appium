from pages.locators.android.onboarding.onboarding_locators import OnboardingLocators
from pages.shared_components.common_action import CommonActions

class OnboardingPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)
        self.onboarding_locators = OnboardingLocators()

    def start_update(self):
        self.common_actions.wait_for_element_visible(*self.onboarding_locators.START_UPDATE)
        self.common_actions.click_element(*self.onboarding_locators.START_UPDATE)
        return self

    def select_language(self):
        self.common_actions.wait_for_element_visible(*self.onboarding_locators.SELECT_LANGUAGE)
        self.common_actions.click_element(*self.onboarding_locators.SELECT_LANGUAGE)
        return self

    def confirm_language_selection(self):
        self.common_actions.wait_for_element_visible(*self.onboarding_locators.CONFIRM_BUTTON)
        self.common_actions.click_element(*self.onboarding_locators.CONFIRM_BUTTON)
        return self

