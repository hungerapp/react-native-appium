from pages.shared_components.common_use import CommonUseSection
from pages.shared_components.common_action import CommonActions
from pages.locators.android.navigation.setting.service_personnel_locators import ServicePersonnelPageLocators

# noinspection DuplicatedCode
class ServicePersonnelPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)
        self.common_use = CommonUseSection(driver)
        self.service_personnel_page_locators = ServicePersonnelPageLocators()

    def verify_service_personnel_page(self):
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.TITLE_IN_SERVICE_PERSONNEL_PAGE)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.CLOSE_BUTTON_IN_SERVICE_PERSONNEL_PAGE)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.SERVICE_PERSONNEL_DESCRIPTION_IN_SERVICE_PERSONNEL_PAGE)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.ADD_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE)
        return self

    def tap_add_service_personnel_button(self):
        self.common_actions.click_element(*self.service_personnel_page_locators.ADD_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE)
        self.common_actions.wait_for_element_clickable(*self.service_personnel_page_locators.ADD_BUTTON_IN_ADD_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.TITLE_IN_ADD_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.DESCRIPTION_IN_ADD_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.CANCEL_BUTTON_IN_ADD_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.click_element(*self.service_personnel_page_locators.ADD_BUTTON_IN_ADD_SERVICE_PERSONNEL_DIALOG)
        return self

    def verify_service_personnel_modal(self):
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.TITLE_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.CLOSE_BUTTON_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.CONFIRM_BUTTON_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.SERVICE_PERSONNEL_NAME_FIELD_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.SERVICE_PERSONNEL_COLOR_SELECTION_IN_SERVICE_PERSONNEL_MODAL(1))
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.SERVICE_PERSONNEL_INTRODUCTION_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.EXPAND_ADVANCED_SETTINGS_IN_SERVICE_PERSONNEL_MODAL)
        return self

    def enter_service_personnel_name(self, service_personnel_name):
        self.common_actions.send_keys_to_element(*self.service_personnel_page_locators.SERVICE_PERSONNEL_NAME_FIELD_IN_SERVICE_PERSONNEL_MODAL, service_personnel_name)
        return self

    def select_color(self, color_num):
        self.common_actions.click_element(*self.service_personnel_page_locators.SERVICE_PERSONNEL_COLOR_SELECTION_IN_SERVICE_PERSONNEL_MODAL(color_num))
        return self

    def enter_service_personnel_introduction(self, service_personnel_introduction):
        self.common_actions.click_element(*self.service_personnel_page_locators.SERVICE_PERSONNEL_INTRODUCTION_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.SERVICE_PERSONNEL_INTRODUCTION_FIELD)
        self.common_actions.send_keys_to_element(*self.service_personnel_page_locators.SERVICE_PERSONNEL_INTRODUCTION_FIELD, service_personnel_introduction)
        self.common_actions.wait_for_element_clickable(*self.service_personnel_page_locators.CONFIRM_CLEAR_SERVICE_PERSONNEL_INTRODUCTION_BUTTON)
        self.common_actions.click_element(*self.service_personnel_page_locators.CONFIRM_CLEAR_SERVICE_PERSONNEL_INTRODUCTION_BUTTON)
        return self

    def enter_simultaneous_service_count(self, simultaneous_service_count):
        self.common_actions.scroll_to_element(*self.service_personnel_page_locators.EXPAND_ADVANCED_SETTINGS_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.click_element(*self.service_personnel_page_locators.EXPAND_ADVANCED_SETTINGS_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.CLOSE_ADVANCED_SETTINGS_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.SIMULTANEOUS_SERVICE_COUNT_FIELD_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.send_keys_to_element(*self.service_personnel_page_locators.SIMULTANEOUS_SERVICE_COUNT_FIELD_IN_SERVICE_PERSONNEL_MODAL, simultaneous_service_count)
        return self

    def tap_confirm_button(self):
        self.common_actions.click_element(*self.service_personnel_page_locators.CONFIRM_BUTTON_IN_SERVICE_PERSONNEL_MODAL)
        self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.TITLE_IN_SERVICE_PERSONNEL_PAGE)
        return self

    def verify_service_personnel_name(self, service_personnel_name):
        self.common_actions.scroll_to_element(*self.service_personnel_page_locators.DELETE_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE(service_personnel_name))
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.DELETE_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE(service_personnel_name))
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.EDIT_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE(service_personnel_name))
        return self

    def delete_service_personnel(self, service_personnel_name):
        self.common_actions.click_element(*self.service_personnel_page_locators.DELETE_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE(service_personnel_name))
        self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.TITLE_IN_DELETE_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.DESCRIPTION_IN_DELETE_SERVICE_PERSONNEL_DIALOG(service_personnel_name))
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.DELETE_FIELD_IN_DELETE_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.is_element_visible(*self.service_personnel_page_locators.CANCEL_BUTTON_IN_DELETE_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.send_keys_to_element(*self.service_personnel_page_locators.DELETE_FIELD_IN_DELETE_SERVICE_PERSONNEL_DIALOG, "Delete")
        self.common_actions.wait_for_element_clickable(*self.service_personnel_page_locators.DELETE_BUTTON_IN_DELETE_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.click_element(*self.service_personnel_page_locators.DELETE_BUTTON_IN_DELETE_SERVICE_PERSONNEL_DIALOG)
        self.common_actions.wait_for_element_disappear(*self.service_personnel_page_locators.DELETE_FIELD_IN_DELETE_SERVICE_PERSONNEL_DIALOG)
        return self


