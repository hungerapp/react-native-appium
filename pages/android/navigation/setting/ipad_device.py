from pages.shared_components.common_action import CommonActions
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.ipad_device_locators import IpadDeviceLocators

# noinspection DuplicatedCode
class IpadDevicePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = IpadDeviceLocators()
        self.common_actions = CommonActions(driver)
        self.common_use_section = CommonUseSection(driver)

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.locators.IPAD_DEVICE_IN_BRANCH_SETTINGS_PAGE)
        return self

    def tap_ipad_device(self):
        self.common_actions.wait_for_element_visible(*self.locators.IPAD_DEVICE_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.IPAD_DEVICE_IN_BRANCH_SETTINGS_PAGE)
        return self

    def verify_ipad_device_page(self):
        self.common_actions.wait_for_element_visible(*self.locators.CLOSE_BUTTON_IN_IPAD_DEVICE_PAGE)
        self.common_actions.wait_for_element_visible(*self.locators.ADD_IPAD_DEVICE_BUTTON_IN_IPAD_DEVICE_PAGE)
        return self

    def add_new_ipad_device(self):
        self.common_actions.wait_for_element_visible(*self.locators.ADD_IPAD_DEVICE_BUTTON_IN_IPAD_DEVICE_PAGE)
        self.common_actions.click_element(*self.locators.ADD_IPAD_DEVICE_BUTTON_IN_IPAD_DEVICE_PAGE)
        self.common_actions.wait_for_element_visible(*self.locators.NEXT_BUTTON_IN_ADD_IPAD_DEVICE_DIALOG)
        self.common_actions.click_element(*self.locators.NEXT_BUTTON_IN_ADD_IPAD_DEVICE_DIALOG)
        self.common_actions.wait_for_element_visible(*self.locators.IPAD_PASS_CODE_IN_ADD_IPAD_DEVICE_DIALOG)
        self.common_actions.click_element(*self.locators.CLOSE_BUTTON_IN_ADD_IPAD_DEVICE_DIALOG)
        self.common_actions.wait_for_element_disappear(*self.locators.IPAD_PASS_CODE_IN_ADD_IPAD_DEVICE_DIALOG)
        return self

    def tap_close_button_ipad_device_page(self):
        self.common_actions.wait_for_element_visible(*self.locators.CLOSE_BUTTON_IN_IPAD_DEVICE_PAGE)
        self.common_actions.click_element(*self.locators.CLOSE_BUTTON_IN_IPAD_DEVICE_PAGE)
        return self