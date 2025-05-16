from pages.shared_components.common_action import CommonActions
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.checkout_locators import CheckoutPageLocators

# noinspection DuplicatedCode
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = CheckoutPageLocators()
        self.common_actions = CommonActions(driver)
        self.common_use_section = CommonUseSection(driver)

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.locators.CHECKOUT_IN_BRANCH_SETTINGS_PAGE)
        return self

    def tap_checkout(self):
        self.common_actions.wait_for_element_visible(*self.locators.CHECKOUT_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.CHECKOUT_IN_BRANCH_SETTINGS_PAGE)
        return self

    def verify_checkout_page(self):
        self.common_actions.wait_for_element_visible(*self.locators.BACK_BUTTON_IN_CHECKOUT_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.locators.CHECKOUT_SIGNATURE_IN_CHECKOUT_SETTINGS_PAGE)
        return self

    def turn_on_checkout_signature(self):
        self.common_actions.wait_for_element_visible(*self.locators.CHECKOUT_SIGNATURE_IN_CHECKOUT_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.CHECKOUT_SIGNATURE_IN_CHECKOUT_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.locators.CHECKOUT_SIGNATURE_SWITCH_IN_CHECKOUT_SIGNATURE_PAGE)
        self.common_actions.click_element(*self.locators.CHECKOUT_SIGNATURE_SWITCH_IN_CHECKOUT_SIGNATURE_PAGE)
        self.common_actions.wait_for_element_clickable(*self.locators.CLOSE_BUTTON_IN_CHECKOUT_SIGNATURE_PAGE)
        self.common_actions.click_element(*self.locators.CLOSE_BUTTON_IN_CHECKOUT_SIGNATURE_PAGE)
        return self

    def tap_back_button(self):
        self.common_actions.wait_for_element_visible(*self.locators.BACK_BUTTON_IN_CHECKOUT_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.BACK_BUTTON_IN_CHECKOUT_SETTINGS_PAGE)
        return self





