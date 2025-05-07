from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.brand_locators import BrandPageLocators
from pages.shared_components.common_action import CommonActions

# noinspection DuplicatedCode
class BrandPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)
        self.common_use = CommonUseSection(driver)
        self.brand_locators = BrandPageLocators()

    def tap_settings_icon(self):
        self.common_actions.is_element_visible(*self.brand_locators.SETTINGS_OPTION_IN_NAVIGATION)
        self.common_actions.click_element(*self.brand_locators.SETTINGS_OPTION_IN_NAVIGATION)
        self.common_actions.wait_for_element_visible(*self.brand_locators.BRANCH_SETTINGS_PAGE)
        return self

    def tap_branch_name(self):
        self.common_actions.click_element(*self.brand_locators.BRANCH_NAME_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.brand_locators.TITLE_IN_BRANCH_BRAND_INFO_PAGE)
        return self

    def verify_branch_brand_info_page(self):
        self.common_actions.wait_for_element_visible(*self.brand_locators.TITLE_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.is_element_visible(*self.brand_locators.CONFIRM_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.is_element_visible(*self.brand_locators.CLOSE_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        return self




    def enter_branch_name(self, branch_name):
        self.common_actions.send_keys_to_element(*self.brand_locators.BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE, branch_name)
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE,branch_name)
        return self

    def enter_branch_introduction(self, branch_introduction):
        self.common_actions.click_element(*self.brand_locators.BRANCH_INTRODUCTION_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.send_keys_to_element(*self.brand_locators.BRANCH_INTRODUCTION_FIELD_IN_BRANCH_BRAND_INFO_PAGE, branch_introduction)
        self.common_actions.click_element(*self.brand_locators.CONFIRM_BRANCH_INTRODUCTION_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_INTRODUCTION_IN_BRANCH_BRAND_INFO_PAGE, branch_introduction)
        return self

    def select_country_code(self, country_code):
        self.common_actions.is_element_visible(*self.brand_locators.BRANCH_PHONE_COUNTRY_CODE_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.click_element(*self.brand_locators.BRANCH_PHONE_COUNTRY_CODE_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.is_element_visible(*self.brand_locators.BRANCH_PHONE_COUNTRY_CODE_SEARCH_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.send_keys_to_element(*self.brand_locators.BRANCH_PHONE_COUNTRY_CODE_SEARCH_FIELD_IN_BRANCH_BRAND_INFO_PAGE, country_code)
        self.common_actions.scroll_to_element(*self.brand_locators.BRANCH_PHONE_COUNTRY_CODE_SELECTED(country_code))
        self.common_actions.click_element(*self.brand_locators.BRANCH_PHONE_COUNTRY_CODE_SELECTED(country_code))
        self.common_actions.click_element(*self.brand_locators.CONFIRM_BRANCH_PHONE_COUNTRY_CODE_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_PHONE_COUNTRY_CODE_IN_BRANCH_BRAND_INFO_PAGE, country_code)
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_PHONE_COUNTRY_CODE_IN_BRANCH_BRAND_INFO_PAGE, country_code)
        return self

    def enter_branch_phone_number(self, phone_number):
        self.common_actions.send_keys_to_element(*self.brand_locators.BRANCH_PHONE_NUMBER_FIELD_IN_BRANCH_BRAND_INFO_PAGE, phone_number)
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_PHONE_NUMBER_FIELD_IN_BRANCH_BRAND_INFO_PAGE, phone_number)
        return self

    def turn_off_branch_phone_display_switch(self):
        self.common_actions.scroll_to_element(*self.brand_locators.DISPLAY_BRANCH_PHONE_NUMBER_SWITCH_IN_BRANCH_BRAND_INFO_PAGE)
        if not self.common_actions.is_element_present(*self.brand_locators.BRANCH_PHONE_NUMBER_FIELD_IN_BRANCH_BRAND_INFO_PAGE):
            self.common_actions.click_element(*self.brand_locators.DISPLAY_BRANCH_PHONE_NUMBER_SWITCH_IN_BRANCH_BRAND_INFO_PAGE)
            self.common_actions.wait_for_element_visible(*self.brand_locators.BRANCH_PHONE_NUMBER_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.click_element(*self.brand_locators.DISPLAY_BRANCH_PHONE_NUMBER_SWITCH_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.wait_for_element_disappear(*self.brand_locators.BRANCH_PHONE_NUMBER_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        return self

    def turn_on_branch_phone_display_switch(self):
        self.common_actions.scroll_to_element(*self.brand_locators.DISPLAY_BRANCH_PHONE_NUMBER_SWITCH_IN_BRANCH_BRAND_INFO_PAGE)
        if not self.common_actions.is_element_present(*self.brand_locators.BRANCH_PHONE_NUMBER_FIELD_IN_BRANCH_BRAND_INFO_PAGE):
            self.common_actions.click_element(*self.brand_locators.DISPLAY_BRANCH_PHONE_NUMBER_SWITCH_IN_BRANCH_BRAND_INFO_PAGE)
            self.common_actions.wait_for_element_visible(*self.brand_locators.BRANCH_PHONE_NUMBER_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        return self

    def turn_off_branch_address_display_switch(self):
        if not self.common_actions.is_element_present(*self.brand_locators.BRANCH_ADDRESS_COUNTRY_IN_BRANCH_BRAND_INFO_PAGE):
            self.common_actions.click_element(*self.brand_locators.DISPLAY_BRANCH_ADDRESS_SWITCH_IN_BRANCH_BRAND_INFO_PAGE)
            self.common_actions.wait_for_element_visible(*self.brand_locators.BRANCH_ADDRESS_COUNTRY_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.click_element(*self.brand_locators.DISPLAY_BRANCH_ADDRESS_SWITCH_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.wait_for_element_disappear(*self.brand_locators.BRANCH_ADDRESS_COUNTRY_IN_BRANCH_BRAND_INFO_PAGE)
        return self

    def turn_on_branch_address_display_switch(self):
        if not self.common_actions.is_element_present(*self.brand_locators.BRANCH_ADDRESS_COUNTRY_IN_BRANCH_BRAND_INFO_PAGE):
            self.common_actions.click_element(*self.brand_locators.DISPLAY_BRANCH_ADDRESS_SWITCH_IN_BRANCH_BRAND_INFO_PAGE)
            self.common_actions.wait_for_element_visible(*self.brand_locators.BRANCH_ADDRESS_COUNTRY_IN_BRANCH_BRAND_INFO_PAGE)
        return self

    def select_branch_city(self, branch_city):
        self.common_actions.scroll_to_element(*self.brand_locators.BRANCH_ADDRESS_CITY_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_ADDRESS_COUNTRY_IN_BRANCH_BRAND_INFO_PAGE,"台灣")
        self.common_actions.click_element(*self.brand_locators.BRANCH_ADDRESS_CITY_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.scroll_to_element(*self.brand_locators.BRANCH_ADDRESS_CITY_SELECTED(branch_city))
        self.common_actions.click_element(*self.brand_locators.BRANCH_ADDRESS_CITY_SELECTED(branch_city))
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_ADDRESS_CITY_IN_BRANCH_BRAND_INFO_PAGE, branch_city)
        return self

    def select_branch_district(self, branch_district):
        self.common_actions.scroll_to_element(*self.brand_locators.BRANCH_ADDRESS_DISTRICT_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.click_element(*self.brand_locators.BRANCH_ADDRESS_DISTRICT_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.scroll_to_element(*self.brand_locators.BRANCH_ADDRESS_DISTRICT_SELECTED(branch_district))
        self.common_actions.click_element(*self.brand_locators.BRANCH_ADDRESS_DISTRICT_SELECTED(branch_district))
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_ADDRESS_DISTRICT_IN_BRANCH_BRAND_INFO_PAGE, branch_district)
        return self

    def enter_branch_address(self, branch_address):
        self.common_actions.scroll_to_element(*self.brand_locators.BRANCH_ADDRESS_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.send_keys_to_element(*self.brand_locators.BRANCH_ADDRESS_FIELD_IN_BRANCH_BRAND_INFO_PAGE, branch_address)
        self.common_actions.verify_element_text(*self.brand_locators.BRANCH_ADDRESS_FIELD_IN_BRANCH_BRAND_INFO_PAGE, branch_address)
        return self

    def tap_expand_brand_settings(self):
        self.common_actions.scroll_to_element(*self.brand_locators.EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.click_element(*self.brand_locators.EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.wait_for_element_visible(*self.brand_locators.CLOSE_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.scroll_to_element(*self.brand_locators.BRAND_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.is_element_visible(*self.brand_locators.BRAND_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.scroll_to_element(*self.brand_locators.BRAND_INTRODUCTION_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.is_element_visible(*self.brand_locators.BRAND_INTRODUCTION_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        return self

    def tap_confirm_button(self):
        self.common_actions.click_element(*self.brand_locators.CONFIRM_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.common_actions.wait_for_element_visible(*self.brand_locators.BRANCH_SETTINGS_PAGE)
        return self

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.brand_locators.BRANCH_SETTINGS_PAGE)
        return self
