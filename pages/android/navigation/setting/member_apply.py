from pages.shared_components.common_action import CommonActions
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.member_apply_locators import MemberApplyLocators

# noinspection DuplicatedCode
class SettingMemberApplyPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)
        self.common_use_section = CommonUseSection(driver)
        self.locators_settings = MemberApplyLocators()

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.locators_settings.MEMBER_APPLY_IN_BRANCH_SETTINGS_PAGE)
        return self

    def tap_member_apply(self):
        self.common_actions.scroll_to_element(*self.locators_settings.MEMBER_APPLY_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators_settings.MEMBER_APPLY_IN_BRANCH_SETTINGS_PAGE)
        return self

    def verify_member_apply_page(self):
        self.common_actions.wait_for_element_visible(*self.locators_settings.MEMBER_APPLY)
        return self