from pages.shared_components.common_action import CommonActions
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.web_layout_management import WebLayoutManagementLocators

# noinspection DuplicatedCode
class WebLayoutManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = WebLayoutManagementLocators()
        self.common_actions = CommonActions(driver)
        self.common_use_section = CommonUseSection(driver)

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.locators.WEB_LAYOUT_MANAGEMENT_IN_BRANCH_SETTINGS_PAGE)
        return self

    def tap_web_layout_management(self):
        self.common_actions.wait_for_element_visible(*self.locators.WEB_LAYOUT_MANAGEMENT_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.locators.WEB_LAYOUT_MANAGEMENT_IN_BRANCH_SETTINGS_PAGE)
        return self

    def select_web_layout_color(self, color_num):
        self.common_actions.wait_for_element_visible(*self.locators.WEB_COLOR_SELECTION_IN_WEB_LAYOUT_MANAGEMENT_PAGE(color_num))
        self.common_actions.click_element(*self.locators.WEB_COLOR_SELECTION_IN_WEB_LAYOUT_MANAGEMENT_PAGE(color_num))
        return self

    def set_week_start_day(self, day):
        self.common_actions.wait_for_element_visible(*self.locators.WEEK_START_DAY)
        self.common_actions.click_element(*self.locators.WEEK_START_DAY)
        self.common_actions.wait_for_element_visible(*self.locators.WEEK_START_DAY_SELECTION(day))
        self.common_actions.click_element(*self.locators.WEEK_START_DAY_SELECTION(day))
        return self

    def set_google_tracking_code(self, tracking_code):
        self.common_actions.scroll_to_element(*self.locators.GOOGLE_TACKING_CODE)
        self.common_actions.click_element(*self.locators.GOOGLE_TACKING_CODE)
        self.common_actions.wait_for_element_visible(*self.locators.GOOGLE_TRACKING_CODE_FIELD_IN_GOOGLE_TRACKING_CODE_MODAL)
        self.common_actions.send_keys_to_element(*self.locators.GOOGLE_TRACKING_CODE_FIELD_IN_GOOGLE_TRACKING_CODE_MODAL, tracking_code)
        self.common_actions.wait_for_element_clickable(*self.locators.CONFIRM_BUTTON_IN_GOOGLE_TRACKING_CODE_MODAL)
        self.common_actions.click_element(*self.locators.CONFIRM_BUTTON_IN_GOOGLE_TRACKING_CODE_MODAL)
        return self

    def tap_confirm_button(self):
        self.common_actions.wait_for_element_clickable(*self.locators.CONFIRM_BUTTON_IN_WEB_LAYOUT_MANAGEMENT_PAGE)
        self.common_actions.click_element(*self.locators.CONFIRM_BUTTON_IN_WEB_LAYOUT_MANAGEMENT_PAGE)
        return self

    def tap_close_button(self):
        self.common_actions.wait_for_element_clickable(*self.locators.CLOSE_BUTTON_IN_WEB_LAYOUT_MANAGEMENT_PAGE)
        self.common_actions.click_element(*self.locators.CLOSE_BUTTON_IN_WEB_LAYOUT_MANAGEMENT_PAGE)
        return self