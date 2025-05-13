from pages.shared_components.common_use import CommonUseSection
from pages.shared_components.common_action import CommonActions
from pages.locators.android.navigation.setting.service_appointment_locators import ServiceAppointmentPageLocators
from pages.locators.android.navigation.setting.service_personnel_locators import ServicePersonnelPageLocators

# noinspection DuplicatedCode
class ServiceAppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)
        self.common_use = CommonUseSection(driver)
        self.service_appointment_page_locators = ServiceAppointmentPageLocators()
        self.service_personnel_page_locators = ServicePersonnelPageLocators()

    def verify_branch_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_APPOINTMENT_IN_BRANCH_SETTINGS_PAGE)
        return self

    def tap_service_appointment(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_APPOINTMENT_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def verify_service_appointment_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.BACK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def share_appointment_link(self):
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.COPY_MEMBER_BOOKING_LINK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_COPY_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_COPY_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_COPY_BUTTON)
        return self

    def click_apply_line_official_account(self):
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.COPY_MEMBER_BOOKING_LINK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_LINE_OA_LINK_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_LINE_OA_LINK_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_LINE_OA_LINK_BUTTON)
        self.driver.back()
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def tap_service_items(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_PRICE_LIST_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_PRICE_LIST_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_SERVICE_ITEM_LIST_PAGE)
        return self

    def add_service_category(self, category_name):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_SERVICE_ITEM_LIST_PAGE)
        if self.common_actions.is_element_present(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE):
            self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
            self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_ADD_BUTTON)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD)
            self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD, category_name)
            self.common_actions.click_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_NAME(category_name))
            self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
        else:
            self.common_actions.click_element(*self.service_appointment_page_locators.ADD_FIRST_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD)
            self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD, category_name)
            self.common_actions.click_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
        return self

    def edit_service_category(self, old_category, new_category):
        self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_EDIT_BUTTON(old_category))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD, new_category)
        self.common_actions.click_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
        return self

    def select_service_category(self, category_name):
        self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE(category_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE(category_name))
        return self

    def click_add_service_item_button(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.ADD_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        return self

    def enter_service_item_name(self, item_name):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_NAME_FIELD, item_name)
        return self

    def enter_service_code_name(self, code_name):
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CODENAME_FIELD, code_name)
        return self

    def enter_service_introduction(self, introduction):
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_INTRODUCTION):
            self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_INTRODUCTION_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_INTRODUCTION)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_INTRODUCTION)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.INTRODUCTION_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.INTRODUCTION_FIELD, introduction)
        self.common_actions.click_element(*self.service_appointment_page_locators.INTRODUCTION_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.INTRODUCTION_CONFIRM_BUTTON)
        return self

    def select_service_category_in_add_service_item(self, category_name):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CATEGORY_SELECTION)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CATEGORY_SELECTION)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_SELECTION_DIALOG_CLOSE_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_SELECTION_DIALOG_NAME_SELECTION(category_name))
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CATEGORY_SELECTION_DIALOG_CLOSE_BUTTON)
        return self

    def enter_service_duration(self, duration):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DURATION_FIELD)
        self.common_actions.clear_text(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DURATION_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DURATION_FIELD, duration)
        return self

    def enter_service_price(self, price):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_PRICE_FIELD)
        self.common_actions.clear_text(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_PRICE_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_PRICE_FIELD, price)
        return self

    def select_display_price_method(self, display_price_method):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DISPLAY_PRICE_METHOD_SELECTION(display_price_method))
        self.common_actions.click_element(*self.service_appointment_page_locators.DISPLAY_PRICE_METHOD_SELECTION(display_price_method))
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DISPLAY_PRICE_METHOD_SELECTION(display_price_method))
        return self

    def select_sub_service_type(self, sub_service_type):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SUB_SERVICE_TYPE_SELECTION(sub_service_type))
        self.common_actions.click_element(*self.service_appointment_page_locators.SUB_SERVICE_TYPE_SELECTION(sub_service_type))
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SUB_SERVICE_TYPE_SELECTION(sub_service_type))
        return self

    def add_sub_service_items(self, sub_item_name, duration, price):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_ADD_SUB_SERVICE_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_ADD_SUB_SERVICE_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_NAME_FIELD, sub_item_name)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_DURATION_FIELD, duration)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_PRICE_FIELD, price)
        self.common_actions.click_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_CONFIRM_BUTTON)
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_ITEM(sub_item_name))
        return self

    def edit_sub_service_items(self, old_sub_item_name, new_sub_item_name, duration, price):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_ITEM(old_sub_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_ITEM_EDIT_BUTTON(old_sub_item_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_NAME_FIELD)
        self.common_actions.clear_text(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_NAME_FIELD, new_sub_item_name)
        self.common_actions.clear_text(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_DURATION_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_DURATION_FIELD, duration)
        self.common_actions.clear_text(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_PRICE_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_PRICE_FIELD, price)
        self.common_actions.click_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_EDIT_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_EDIT_CONFIRM_BUTTON)
        return self

    def delete_sub_service_items(self, sub_item_name):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_ITEM(sub_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_ITEM_DELETE_BUTTON(sub_item_name))
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_ITEM(sub_item_name))
        return self

    def click_save_add_service_item_button(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CONFIRM_BUTTON)
        return self

    def copy_service_item_name(self, item_name):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE(item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE(item_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.COPY_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.COPY_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.COPY_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        assert self.common_actions.get_element_count(*self.service_appointment_page_locators.SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE(item_name)) >= 2, "Service item name not copied successfully"
        return self

    def delete_service_item(self, item_name):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE(item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE(item_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DELETE_SERVICE_ITEM_DIALOG_DELETE_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_SERVICE_ITEM_DIALOG_DELETE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DELETE_SERVICE_ITEM_DIALOG_DELETE_BUTTON)
        return self

    def edit_service_item(self, item_name):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE(item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE(item_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EDIT_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        return self

    def delete_service_category(self, category_name= None, delete_all=False):
        self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
        if delete_all:
            while self.common_actions.is_element_present(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_DELETE_BUTTON_ALL):
                self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_DELETE_BUTTON_ALL)
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DELETE_BUTTON)
                self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DELETE_BUTTON)
                self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DELETE_BUTTON)
        else:
            self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_DELETE_BUTTON(category_name))
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_TITLE)
            self.common_actions.is_element_visible(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DESCRIPTION(category_name))
            self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DELETE_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DELETE_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
        return self

    def tap_close_service_item_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        return self

    def verify_service_personnel(self, service_personnel_name):
        self.common_actions.click_element(*self.service_appointment_page_locators.BACK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.SERVICE_PERSONNEL_BUTTON_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.service_personnel_page_locators.SERVICE_PERSONNEL_BUTTON_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.TITLE_IN_SERVICE_PERSONNEL_PAGE)
        if not self.common_actions.scroll_to_element(*self.service_personnel_page_locators.EDIT_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE(service_personnel_name)):
            self.common_actions.click_element(*self.service_personnel_page_locators.ADD_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE)
            self.common_actions.wait_for_element_clickable(*self.service_personnel_page_locators.ADD_BUTTON_IN_ADD_SERVICE_PERSONNEL_DIALOG)
            self.common_actions.is_element_visible(*self.service_personnel_page_locators.TITLE_IN_ADD_SERVICE_PERSONNEL_DIALOG)
            self.common_actions.is_element_visible(*self.service_personnel_page_locators.DESCRIPTION_IN_ADD_SERVICE_PERSONNEL_DIALOG)
            self.common_actions.is_element_visible(*self.service_personnel_page_locators.CANCEL_BUTTON_IN_ADD_SERVICE_PERSONNEL_DIALOG)
            self.common_actions.click_element(*self.service_personnel_page_locators.ADD_BUTTON_IN_ADD_SERVICE_PERSONNEL_DIALOG)
            self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.SERVICE_PERSONNEL_NAME_FIELD_IN_SERVICE_PERSONNEL_MODAL)
            self.common_actions.send_keys_to_element(*self.service_personnel_page_locators.SERVICE_PERSONNEL_NAME_FIELD_IN_SERVICE_PERSONNEL_MODAL, service_personnel_name)
            self.common_actions.click_element(*self.service_personnel_page_locators.CONFIRM_BUTTON_IN_SERVICE_PERSONNEL_MODAL)
            self.common_actions.wait_for_element_visible(*self.service_personnel_page_locators.TITLE_IN_SERVICE_PERSONNEL_PAGE)
            self.common_actions.scroll_to_element(*self.service_personnel_page_locators.EDIT_SERVICE_PERSONNEL_BUTTON_IN_SERVICE_PERSONNEL_PAGE(service_personnel_name))
        self.common_actions.click_element(*self.service_personnel_page_locators.CLOSE_BUTTON_IN_SERVICE_PERSONNEL_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_APPOINTMENT_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_APPOINTMENT_IN_BRANCH_SETTINGS_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def verify_service_item(self, category_name, item_name):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_PRICE_LIST_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_PRICE_LIST_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_SERVICE_ITEM_LIST_PAGE)
        if not self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE(category_name)):
            if self.common_actions.is_element_present(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE):
                self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
                self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_ADD_BUTTON)
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD)
                self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD, category_name)
                self.common_actions.click_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
                self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_NAME(category_name))
                self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
                self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
            else:
                self.common_actions.click_element(*self.service_appointment_page_locators.ADD_FIRST_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD)
                self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD, category_name)
                self.common_actions.click_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
                self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
        self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE(category_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE(category_name))
        if not self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE(item_name)):
            self.common_actions.click_element(*self.service_appointment_page_locators.ADD_SERVICE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_NAME_FIELD)
            self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_NAME_FIELD, item_name)
            self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DURATION_FIELD)
            self.common_actions.clear_text(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DURATION_FIELD)
            self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DURATION_FIELD, "60")
            self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_PRICE_FIELD)
            self.common_actions.clear_text(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_PRICE_FIELD)
            self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_PRICE_FIELD, "100")
            self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD)
            self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DISPLAY_PRICE_METHOD_SELECTION("固定價"))
            self.common_actions.click_element(*self.service_appointment_page_locators.DISPLAY_PRICE_METHOD_SELECTION("固定價"))
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DISPLAY_PRICE_METHOD_SELECTION("固定價"))
            self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE)
            self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SUB_SERVICE_TYPE_SELECTION("複選"))
            self.common_actions.click_element(*self.service_appointment_page_locators.SUB_SERVICE_TYPE_SELECTION("複選"))
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SUB_SERVICE_TYPE_SELECTION("複選"))
            self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_ADD_SUB_SERVICE_BUTTON)
            self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_ADD_SUB_SERVICE_BUTTON)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_NAME_FIELD)
            self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_NAME_FIELD, "子服務")
            self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_DURATION_FIELD, "30")
            self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_PRICE_FIELD, "50")
            self.common_actions.click_element(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_CONFIRM_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SUB_SERVICE_DIALOG_CONFIRM_BUTTON)
            self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_ITEM("子服務"))
            self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CONFIRM_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        return self

    def tap_online_booking(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.ONLINE_BOOKING_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def verify_online_booking_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.DESCRIPTION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        return self

    def enter_appointment_combination_name(self, combination_name):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_NAME_FIELD, combination_name)
        return self

    def enter_appointment_combination_introduction(self, combination_introduction):
        self.common_actions.click_element(*self.service_appointment_page_locators.ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION_FIELD, combination_introduction)
        self.common_actions.click_element(*self.service_appointment_page_locators.UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_INTRODUCTION_CONFIRM_BUTTON)
        return self

    def select_appointment_combination_service_personnel(self, service_personnel):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_SERVICE_PERSONNEL_SELECTION(service_personnel))
        self.common_actions.click_element(*self.service_appointment_page_locators.ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_SERVICE_PERSONNEL_SELECTION(service_personnel))
        return self

    def tap_confirm_add_appointment_combination(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_CONFIRM_BUTTON)
        return self

    def verify_appointment_combination_name(self, combination_name):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(combination_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(combination_name))
        return self

    def tap_edit_appointment_combination(self, combination_name):
        self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(combination_name))
        return self

    def tap_open_item_tab(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.OPEN_ITEM_TAB_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_ITEM_TAB_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE)
        return self

    def select_main_service_item(self, service_item_category, service_item_name, clear_all=False):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MAIN_SERVICE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.MAIN_SERVICE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE)
        if clear_all:
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CLEAR_BUTTON)
            self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CLEAR_BUTTON)
        self.common_actions.wait_for_element_present(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CONFIRM_BUTTON)
        self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_CATEGORY_SELECTION(service_item_category))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_CATEGORY_SELECTION(service_item_category))
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CONFIRM_BUTTON)
        return self

    def select_online_booking_type(self, booking_type):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.ONLINE_BOOKING_TYPE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.ONLINE_BOOKING_TYPE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ONLINE_BOOKING_TYPE_SELECTION(booking_type))
        self.common_actions.click_element(*self.service_appointment_page_locators.ONLINE_BOOKING_TYPE_SELECTION(booking_type))
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.ONLINE_BOOKING_TYPE_SELECTION(booking_type))
        return self

    def select_additional_service_item(self, service_item_category, service_item_name, clear_all=False):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.ADDITIONAL_SERVICE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.ADDITIONAL_SERVICE_IN_EDIT_UNSPECIFIED_SERVICE_PAGE)
        if clear_all:
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CLEAR_BUTTON)
            self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CLEAR_BUTTON)
        self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_CATEGORY_SELECTION(service_item_category))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_CATEGORY_SELECTION(service_item_category))
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SERVICE_ITEM_SELECTION_DIALOG_CONFIRM_BUTTON)
        return self

    def tap_close_edit_appointment_combination(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE)
        return self

    def delete_appointment_combination(self, combination_name= None, delete_all=False):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        if delete_all:
            while self.common_actions.is_element_present(*self.service_appointment_page_locators.EDIT_ALL_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE):
                self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_ALL_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BASIC_INFO_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE)
                self.common_actions.scroll_to_element(*self.service_appointment_page_locators.DELETE_BUTTON_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE)
                self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_BUTTON_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE)
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DELETE_COMBINATION_DIALOG_DELETE_BUTTON)
                self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_COMBINATION_DIALOG_DELETE_BUTTON)
                self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DELETE_COMBINATION_DIALOG_DELETE_BUTTON)
        else:
            self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(combination_name))
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DELETE_BUTTON_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE)
            self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_BUTTON_IN_EDIT_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DELETE_COMBINATION_DIALOG_DELETE_BUTTON)
            self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_COMBINATION_DIALOG_DELETE_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DELETE_COMBINATION_DIALOG_DELETE_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(combination_name))
        return self

    def verify_appointment_combination_name_not_visible(self, combination_name):
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(combination_name))
        return self

    def tap_edit_service_personnel(self, service_personnel):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.EDIT_SERVICE_PERSONNEL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(service_personnel))
        self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_SERVICE_PERSONNEL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(service_personnel))
        return self

    def set_available_date(self, specific_date, open_month):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.OPEN_SITTING_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_SITTING_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.AVAILABLE_DAYS_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.AVAILABLE_DAYS_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.AVAILABLE_DAYS_MODAL_SPECIFIC_DATE)
        self.common_actions.click_element(*self.service_appointment_page_locators.AVAILABLE_DAYS_MODAL_SPECIFIC_DATE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.AVAILABLE_DAYS_MODAL_SPECIFIC_DATE_SELECTION(specific_date))
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.AVAILABLE_DAYS_MODAL_SPECIFIC_DATE_SELECTION(specific_date))
        self.common_actions.click_element(*self.service_appointment_page_locators.AVAILABLE_DAYS_MODAL_SPECIFIC_DATE_SELECTION(specific_date))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.AVAILABLE_DAYS_MODAL_MONTH_SELECTION(open_month))
        self.common_actions.click_element(*self.service_appointment_page_locators.AVAILABLE_DAYS_MODAL_MONTH_SELECTION(open_month))
        self.common_actions.click_element(*self.service_appointment_page_locators.AVAILABLE_DAYS_MODAL_CONFIRM_BUTTON)
        return self

    def set_latest_booking_time(self, latest_booking_time):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.OPEN_SITTING_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_SITTING_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.LATEST_BOOKING_TIME_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.LATEST_BOOKING_TIME_MODAL_TIME_SELECTION(latest_booking_time))
        self.common_actions.click_element(*self.service_appointment_page_locators.LATEST_BOOKING_TIME_MODAL_TIME_SELECTION(latest_booking_time))
        return self

    def set_online_booking_quantity_range(self, min_quantity, max_quantity):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EXPAND_ADVANCED_SETTINGS_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.EXPAND_ADVANCED_SETTINGS_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.MIN_BOOKING_QUANTITY_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.MIN_BOOKING_QUANTITY_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE, min_quantity)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.MAX_BOOKING_QUANTITY_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE, max_quantity)
        return self

    def set_open_time(self, times):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.OPEN_TIME_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_TIME_TAB_IN_EDIT_SERVICE_PERSONNEL_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.OPEN_TIME_DATE_SELECTION)
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_TIME_DATE_SELECTION)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_CLOSE_TIME_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_CLOSE_TIME_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CLOSE_TIME_DIALOG_ALL_TIME_CLOSE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CLOSE_TIME_DIALOG_ALL_TIME_CLOSE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CLOSE_ALL_TIME_DIALOG_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.CLOSE_ALL_TIME_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CLOSE_ALL_TIME_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_TODAY_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_TODAY_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_SHOW_EARLY_MORNING_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_TIME_SELECTION("0:00"))
        time_list = [t.strip() for t in times.split(',')]
        for time in time_list:
            try:
                self.common_actions.scroll_to_element(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_TIME_SELECTION(time))
                self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_TIME_SELECTION(time))
            except Exception as e:
                    print(f"Error setting time {time}: {str(e)}")
        self.common_actions.click_element(*self.service_appointment_page_locators.OPEN_TIME_SELECTION_MODAL_CLOSE_BUTTON)
        return self

    def tap_close_online_booking_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        return self

    def tap_add_appointment_combination(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.ADD_ADD_UNSPECIFIED_APPOINTMENT_COMBINATION_MODAL_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        return self

    def tap_booking_note(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BOOKING_NOTE_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.BOOKING_NOTE_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_BOOKING_NOTE_PAGE)
        return self

    def turn_off_booking_note_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BOOKING_NOTE_SWITCH_IN_BOOKING_NOTE_PAGE)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.BOOKING_NOTE_FIELD_IN_BOOKING_NOTE_PAGE):
            self.common_actions.click_element(*self.service_appointment_page_locators.BOOKING_NOTE_SWITCH_IN_BOOKING_NOTE_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BOOKING_NOTE_FIELD_IN_BOOKING_NOTE_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.BOOKING_NOTE_SWITCH_IN_BOOKING_NOTE_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.BOOKING_NOTE_FIELD_IN_BOOKING_NOTE_PAGE)
        return self

    def turn_on_booking_note_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BOOKING_NOTE_SWITCH_IN_BOOKING_NOTE_PAGE)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.BOOKING_NOTE_FIELD_IN_BOOKING_NOTE_PAGE):
            self.common_actions.click_element(*self.service_appointment_page_locators.BOOKING_NOTE_SWITCH_IN_BOOKING_NOTE_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BOOKING_NOTE_FIELD_IN_BOOKING_NOTE_PAGE)
        return self

    def enter_booking_note(self, note):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BOOKING_NOTE_FIELD_IN_BOOKING_NOTE_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.BOOKING_NOTE_FIELD_IN_BOOKING_NOTE_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BOOKING_NOTE_DIALOG_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.BOOKING_NOTE_DIALOG_FIELD, note)
        self.common_actions.click_element(*self.service_appointment_page_locators.BOOKING_NOTE_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.BOOKING_NOTE_DIALOG_CONFIRM_BUTTON)
        return self

    def tap_confirm_booking_note(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.CONFIRM_BUTTON_IN_BOOKING_NOTE_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CONFIRM_BUTTON_IN_BOOKING_NOTE_PAGE)
        return self

    def tap_deposit_management(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEPOSIT_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.DEPOSIT_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_DEPOSIT_MANAGEMENT_PAGE)
        return self

    def tap_general_deposit_settings(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.GENERAL_DATE_IN_DEPOSIT_MANAGEMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.GENERAL_DATE_IN_DEPOSIT_MANAGEMENT_PAGE)
        return self

    def turn_off_general_date_deposit_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.GENERAL_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE):
            self.common_actions.click_element(*self.service_appointment_page_locators.GENERAL_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.GENERAL_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        return self

    def turn_on_general_date_deposit_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.GENERAL_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE):
            self.common_actions.click_element(*self.service_appointment_page_locators.GENERAL_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        return self

    def set_default_member_status_no_receive_deposit(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS)
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS_SELECTION_NO_RECEIVE)
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS_SELECTION_NO_RECEIVE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS_SELECTION_NO_RECEIVE)
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_CONFIRM_BUTTON)
        return self

    def set_default_member_status_receive_deposit(self, receive_type):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS)
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS_SELECTION_RECEIVE)
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS_SELECTION_RECEIVE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_MEMBER_STATUS_SELECTION_RECEIVE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_RECEIVE_TYPE_SELECTION(receive_type))
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_RECEIVE_TYPE_SELECTION(receive_type))
        self.common_actions.click_element(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        return self

    def set_payable_service_item(self, service_scope, service_item_category = None, service_item_name = None, clear_all=False):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SPECIFIC_SERVICE_ITEM)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SPECIFIC_SERVICE_ITEM)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_SCOPE_SELECTION(service_scope))
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_SCOPE_SELECTION(service_scope))
        if service_scope == "指定服務":
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM)
            self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM)
            if clear_all:
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM_SELECTION_ALL_CLEAR)
                self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM_SELECTION_ALL_CLEAR)
            self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM_CATEGORY(service_item_category))
            self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM_CATEGORY(service_item_category))
            self.common_actions.scroll_to_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM_SELECTION(service_item_name))
            self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM_SELECTION(service_item_name))
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM_SELECTION_CONFIRM)
            self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_SERVICE_ITEM_SELECTION_CONFIRM)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYABLE_SERVICE_ITEM_MODAL_CONFIRM_BUTTON)
        return self

    def go_to_integration_payment_method(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_METHOD_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_METHOD_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_GO_TO_INTEGRATION_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_GO_TO_INTEGRATION_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_GO_TO_INTEGRATION_BUTTON)
        self.driver.back()
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_GO_TO_INTEGRATION_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_CLOSE_BUTTON)
        return self

    def set_payment_method(self, payment_method):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_METHOD_IN_DEPOSIT_SETTING_PAGE)
        text = self.common_actions.get_element_text(*self.service_appointment_page_locators.PAYMENT_METHOD_TEXT_IN_DEPOSIT_SETTING_PAGE)
        if payment_method not in text:
            self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_METHOD_IN_DEPOSIT_SETTING_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_SWITCH(payment_method))
            self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_SWITCH(payment_method))
            if payment_method == "銀行匯款":
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_BANK_NAME)
                self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_BANK_NAME)
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_BANK_NAME_SELECTION("004 臺灣銀行"))
                self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_BANK_NAME_SELECTION("004 臺灣銀行"))
                self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_BANK_ACCOUNT_NUMBER)
                self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_BANK_ACCOUNT_NUMBER, "123456789012345678")
            self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_METHOD_MODAL_CONFIRM_BUTTON)
        return self

    def set_payment_amount_pricing_method(self, pricing_method, amount, percentage = None):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_AMOUNT_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_AMOUNT_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_PRICING_METHOD)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_PRICING_METHOD)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_PRICING_METHOD_SELECTION(pricing_method))
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_PRICING_METHOD_SELECTION(pricing_method))
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_PRICING_METHOD_SELECTION(pricing_method))
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_AMOUNT_FIELD, amount)
        if pricing_method == "比例":
            self.common_actions.scroll_to_element(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_PERCENTAGE_VALUE_SELECTION(percentage))
            self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_PERCENTAGE_VALUE_SELECTION(percentage))
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_AMOUNT_MODAL_CONFIRM_BUTTON)
        return self

    def set_auto_cancel_if_unpaid(self, auto_cancel_time):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.AUTO_CANCEL_IF_NOT_PAID_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.AUTO_CANCEL_IF_NOT_PAID_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.AUTO_CANCEL_IF_UNPAID_MODAL_AUTO_CANCEL_IF_UNPAID_TIME_SELECTION(auto_cancel_time))
        self.common_actions.click_element(*self.service_appointment_page_locators.AUTO_CANCEL_IF_UNPAID_MODAL_AUTO_CANCEL_IF_UNPAID_TIME_SELECTION(auto_cancel_time))
        self.common_actions.click_element(*self.service_appointment_page_locators.AUTO_CANCEL_IF_UNPAID_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.AUTO_CANCEL_IF_UNPAID_MODAL_AUTO_CANCEL_IF_UNPAID_TIME_SELECTION(auto_cancel_time))
        return self

    def set_payment_instructions(self, instructions):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.PAYMENT_INSTRUCTIONS_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_INSTRUCTIONS_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_INSTRUCTIONS_MODAL_INSTRUCTIONS_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.PAYMENT_INSTRUCTIONS_MODAL_INSTRUCTIONS_FIELD, instructions)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_INSTRUCTIONS_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.PAYMENT_INSTRUCTIONS_MODAL_CONFIRM_BUTTON)
        return self

    def tap_confirm_deposit_settings(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CONFIRM_BUTTON_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CONFIRM_BUTTON_IN_DEPOSIT_SETTING_PAGE)
        return self

    def tap_close_deposit_management_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_DEPOSIT_MANAGEMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_DEPOSIT_MANAGEMENT_PAGE)
        return self

    def tap_specific_date_deposit_settings(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SPECIFIC_DATE_RANGE_IN_DEPOSIT_MANAGEMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SPECIFIC_DATE_RANGE_IN_DEPOSIT_MANAGEMENT_PAGE)
        return self

    def turn_off_specific_date_deposit_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SPECIFIC_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE):
            self.common_actions.click_element(*self.service_appointment_page_locators.SPECIFIC_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SPECIFIC_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        return self

    def turn_on_specific_date_deposit_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SPECIFIC_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE):
            self.common_actions.click_element(*self.service_appointment_page_locators.SPECIFIC_DATE_DEPOSIT_SWITCH_IN_DEPOSIT_SETTING_PAGE)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DEFAULT_MEMBER_STATUS_IN_DEPOSIT_SETTING_PAGE)
        return self

    def set_specific_date(self, name, start_date, end_date):
        today = self.common_use.get_current_timestamp()
        if end_date == "tomorrow":
            end_date = self.common_use.add_days_to_date(today, 1)
        today_year = int(today[:4])
        today_month = int(today[4:6])
        start_year, start_month, start_day = map(int, start_date.split('/'))
        end_year, end_month, end_day = map(int, end_date.split('/'))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.PAYMENT_PERIOD_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_PERIOD_IN_DEPOSIT_SETTING_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADDITIONAL_PAYMENT_PERIOD_MODAL_ADDITIONAL_PAYMENT_PERIOD)
        self.common_actions.click_element(*self.service_appointment_page_locators.ADDITIONAL_PAYMENT_PERIOD_MODAL_ADDITIONAL_PAYMENT_PERIOD)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADDITIONAL_PAYMENT_PERIOD_MODAL_PERIOD_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADDITIONAL_PAYMENT_PERIOD_MODAL_PERIOD_NAME_FIELD, name)
        self.common_actions.click_element(*self.service_appointment_page_locators.ADDITIONAL_PAYMENT_PERIOD_MODAL_START_DATE)
        if start_year >= today_year:
            if start_month >= today_month:
                click_num = (start_year-today_year) * 12 + (start_month - today_month)
                for i in range(click_num):
                    self.common_actions.click_element(*self.service_appointment_page_locators.ARROW_RIGHT)
                    self.common_actions.is_element_visible(*self.service_appointment_page_locators.MONTH_AND_YEAR(start_year, start_month))
                self.common_actions.click_element(*self.service_appointment_page_locators.DAY(start_day))
                self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_PERIOD_MODAL_CONFIRM_BUTTON)
                self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.MONTH_AND_YEAR(start_year, start_month))
        self.common_actions.click_element(*self.service_appointment_page_locators.ADDITIONAL_PAYMENT_PERIOD_MODAL_END_DATE)
        if end_year >= today_year:
            if end_month >= today_month:
                click_num = (end_year-today_year) * 12 + (end_month - today_month)
                for i in range(click_num):
                    self.common_actions.click_element(*self.service_appointment_page_locators.ARROW_RIGHT)
                    self.common_actions.is_element_visible(*self.service_appointment_page_locators.MONTH_AND_YEAR(end_year, end_month))
                self.common_actions.click_element(*self.service_appointment_page_locators.DAY(end_day))
                self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_PERIOD_MODAL_CONFIRM_BUTTON)
                self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.MONTH_AND_YEAR(end_year, end_month))
        self.common_actions.click_element(*self.service_appointment_page_locators.ADDITIONAL_PAYMENT_PERIOD_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.ADDITIONAL_PAYMENT_PERIOD_MODAL_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.PAYMENT_PERIOD_MODAL_CONFIRM_BUTTON)
        return self

    def tap_advanced_feature_settings(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADVANCED_FEATURES_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.ADVANCED_FEATURES_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def tap_reservation_restriction(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.RESERVATION_RESTRICTION_IN_ADVANCED_FEATURES_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.RESERVATION_RESTRICTION_IN_ADVANCED_FEATURES_PAGE)
        return self

    def set_cancellation_time(self, cancellation_time):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.RESERVATION_CANCELLATION_SETTINGS)
        self.common_actions.click_element(*self.service_appointment_page_locators.RESERVATION_CANCELLATION_SETTINGS)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.RESERVATION_CANCELLATION_SETTINGS_SELECTION(cancellation_time))
        self.common_actions.click_element(*self.service_appointment_page_locators.RESERVATION_CANCELLATION_SETTINGS_SELECTION(cancellation_time))
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.RESERVATION_CANCELLATION_SETTINGS_SELECTION(cancellation_time))
        return self

    def turn_off_upcoming_reservation_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.UPCOMING_RESERVATION_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.UPCOMING_RESERVATION_COUNT_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.UPCOMING_RESERVATION_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.UPCOMING_RESERVATION_COUNT_FIELD)
        self.common_actions.click_element(*self.service_appointment_page_locators.UPCOMING_RESERVATION_SWITCH)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.UPCOMING_RESERVATION_COUNT_FIELD)
        return self

    def turn_on_upcoming_reservation_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.UPCOMING_RESERVATION_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.UPCOMING_RESERVATION_COUNT_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.UPCOMING_RESERVATION_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.UPCOMING_RESERVATION_COUNT_FIELD)
        return self

    def set_upcoming_reservation_count(self, count):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.UPCOMING_RESERVATION_COUNT_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.UPCOMING_RESERVATION_COUNT_FIELD, count)
        return self

    def turn_off_no_show_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.NO_SHOW_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.NO_SHOW_COUNT_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.NO_SHOW_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.NO_SHOW_COUNT_FIELD)
        self.common_actions.click_element(*self.service_appointment_page_locators.NO_SHOW_SWITCH)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.NO_SHOW_COUNT_FIELD)
        return self

    def turn_on_no_show_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.NO_SHOW_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.NO_SHOW_COUNT_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.NO_SHOW_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.NO_SHOW_COUNT_FIELD)
        return self

    def set_no_show_count(self, count):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.NO_SHOW_COUNT_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.NO_SHOW_COUNT_FIELD, count)
        return self

    def turn_off_monthly_reservation_cancellation_limit_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_COUNT_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_COUNT_FIELD)
        self.common_actions.click_element(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_SWITCH)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_COUNT_FIELD)
        return self

    def turn_on_monthly_reservation_cancellation_limit_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_COUNT_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_COUNT_FIELD)
        return self

    def set_monthly_reservation_cancellation_limit(self, count):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_COUNT_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.MONTHLY_RESERVATION_CANCELLATION_LIMIT_COUNT_FIELD, count)
        return self

    def turn_off_customer_score_limit_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_FIELD)
        self.common_actions.click_element(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_SWITCH)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_FIELD)
        return self

    def turn_on_customer_score_limit_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_FIELD)
        return self

    def set_customer_score_limit(self, count):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.CUSTOMER_SCORE_LIMIT_FIELD, count)
        return self

    def tap_confirm_reservation_restriction(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CONFIRM_BUTTON_IN_RESERVATION_RESTRICTION_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CONFIRM_BUTTON_IN_RESERVATION_RESTRICTION_PAGE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CONFIRM_BUTTON_IN_RESERVATION_RESTRICTION_PAGE)
        return self

    def tap_post_reservation_buffer(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_IN_ADVANCED_FEATURES_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_IN_ADVANCED_FEATURES_PAGE)
        return self

    def turn_off_post_reservation_buffer_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_FIELD)
        self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_SWITCH)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_FIELD)
        return self

    def turn_on_post_reservation_buffer_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_FIELD)
        return self

    def set_post_reservation_buffer_time(self, time):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_FIELD, time)
        return self

    def set_need_post_reservation_buffer_service_item(self, category, service_item_name, clear_all=False):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM)
        self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_ALL_CLEAR)
        if clear_all:
            self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_ALL_CLEAR)
        self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_CATEGORY(category))
        self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_CATEGORY(category))
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_CONFIRM)
        self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_CONFIRM)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_SERVICE_ITEM_CONFIRM)
        return self

    def tap_confirm_post_reservation_buffer(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_CONFIRM_BUTTON)
        return self

    def tap_business_hours(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_IN_ADVANCED_FEATURES_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_IN_ADVANCED_FEATURES_PAGE)
        return self

    def turn_off_business_hours_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY("週一")):
            self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY("週一"))
        self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_SWITCH)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY("週一"))
        return self

    def turn_on_business_hours_switch(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY("週一")):
            self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY("週一"))
        return self

    def set_business_hours(self, weekdays):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY(weekdays))
        self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY(weekdays))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_CLOSED_ALL_DAY_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_ADD_BUSINESS_HOURS_BUTTON):
            self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_CLOSED_ALL_DAY_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_ADD_BUSINESS_HOURS_BUTTON)
        while self.common_actions.is_element_present(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_DELETE_BUTTON):
            self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_DELETE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_DELETE_BUTTON, timeout=1)
        self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_ADD_BUSINESS_HOURS_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_TIME)
        self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_BY_DAY_CONFIRM_BUTTON)
        return self

    def tap_close_business_hours_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.BUSINESS_HOURS_CLOSE_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.BUSINESS_HOURS_CLOSE_BUTTON)
        return self

    def tap_equipment_management(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_IN_ADVANCED_FEATURES_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_IN_ADVANCED_FEATURES_PAGE)
        return self

    def delete_equipment(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_ADD_EQUIPMENT_BUTTON)
        while self.common_actions.is_element_present(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_DELETE_BUTTON):
            self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_DELETE_BUTTON)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DELETE_DIALOG_DELETE_BUTTON)
            self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_DIALOG_DELETE_BUTTON)
            self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DELETE_DIALOG_DELETE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_DELETE_BUTTON, timeout=1)
        return self

    def add_equipment(self, equipment_name, equipment_num, service_item_category, service_item_name, clear_all=False):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_ADD_EQUIPMENT_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_ADD_EQUIPMENT_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_ENABLE_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.EQUIPMENT_NAME_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_ENABLE_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.EQUIPMENT_NAME_FIELD, equipment_name)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.EQUIPMENT_NUMBER_FIELD, equipment_num)
        self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_LINKED_SERVICE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_ALL_CLEAR)
        if clear_all:
            self.common_actions.click_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_ALL_CLEAR)
        self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CATEGORY(service_item_category))
        self.common_actions.click_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CATEGORY(service_item_category))
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CONFIRM)
        self.common_actions.click_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CONFIRM)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CONFIRM)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_EDIT_BUTTON(equipment_name))
        return self

    def edit_equipment(self, old_equipment_name, new_equipment_name, new_equipment_num, service_item_category, service_item_name, clear_all=False):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_EDIT_BUTTON(old_equipment_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_EDIT_BUTTON(old_equipment_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_ENABLE_SWITCH)
        if not self.common_actions.is_element_present(*self.service_appointment_page_locators.EQUIPMENT_NAME_FIELD):
            self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_ENABLE_SWITCH)
            self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_NAME_FIELD)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.EQUIPMENT_NAME_FIELD, new_equipment_name)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.EQUIPMENT_NUMBER_FIELD, new_equipment_num)
        self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_LINKED_SERVICE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_ALL_CLEAR)
        if clear_all:
            self.common_actions.click_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_ALL_CLEAR)
        self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CATEGORY(service_item_category))
        self.common_actions.click_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CATEGORY(service_item_category))
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_SELECTION(service_item_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CONFIRM)
        self.common_actions.click_element(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CONFIRM)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.LINKED_SERVICE_ITEM_CONFIRM)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_CONFIRM_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_EDIT_BUTTON(new_equipment_name))
        return self

    def tap_close_equipment_management_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_CLOSE_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.EQUIPMENT_MANAGEMENT_CLOSE_BUTTON)
        return self

    def tap_close_advanced_feature_settings_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.POST_RESERVATION_BUFFER_TIME_IN_ADVANCED_FEATURES_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_ADVANCED_FEATURES_PAGE)
        return self

    def tap_close_service_appointment_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.BACK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        return self