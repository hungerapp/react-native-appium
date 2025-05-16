from pages.shared_components.common_action import CommonActions
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.third_party_tools_locators import ThirdPartToolsPageLocators

# noinspection DuplicatedCode
class ThirdPartToolsPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = ThirdPartToolsPageLocators()
        self.common_actions = CommonActions(driver)
        self.common_use_section = CommonUseSection(driver)

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.locators.THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE)
        return self

    def verify_subscription_plan(self, subscription_name):
        self.common_actions.wait_for_element_visible(*self.locators.SUBSCRIPTION_PLAN_IN_BRANCH_SETTINGS_PAGE(subscription_name))
        return self

    def tap_third_party_tools(self):
        self.common_actions.wait_for_element_visible(*self.locators.THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE)
        return self

    def verify_feature_unsupported_dialog(self):
        self.common_actions.wait_for_element_visible(*self.locators.SUBSCRIPTION_PLAN_NOW_BUTTON)
        self.common_actions.click_element(*self.locators.SUBSCRIPTION_PLAN_NOW_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.locators.SUBSCRIPTION_PLAN_NOW_BUTTON)
        self.driver.back()
        self.common_actions.wait_for_element_visible(*self.locators.THIRD_PART_TOOLS_IN_BRANCH_SETTINGS_PAGE)
        return self