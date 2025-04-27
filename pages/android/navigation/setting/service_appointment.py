from pages.shared_components.common_use import CommonUseSection
from pages.shared_components.common_action import CommonActions
from pages.locators.android.navigation.setting.service_appointment_locators import ServiceAppointmentPageLocators

# noinspection DuplicatedCode
class ServiceAppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_actions = CommonActions(driver)
        self.common_use = CommonUseSection(driver)
        self.service_appointment_page_locators = ServiceAppointmentPageLocators()

    def verify_service_appointment_page(self):
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.TITLE_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.BACK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def share_appointment_link(self):
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.COPY_MEMBER_BOOKING_LINK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_LINE_OA_LINK_BUTTON)
        self.common_actions.click_element(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_COPY_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.MEMBER_BOOKING_LINK_DIALOG_COPY_BUTTON)
        return self

    def tap_service_items(self):
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.SERVICE_PRICE_LIST_IN_SERVICE_APPOINTMENT_PAGE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_PRICE_LIST_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def verify_service_items_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        return self

    def add_service_category(self, category_name):
        self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_ADD_BUTTON)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD, category_name)
        self.common_actions.click_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
        return self

    def verify_service_category(self, category_name):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_NAME(category_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
        self.common_actions.scroll_to_element_left(*self.service_appointment_page_locators.CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE(category_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE(category_name))
        return self

    def edit_service_category(self, old_category, new_category):
        self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_EDIT_BUTTON(old_category))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD)
        self.common_actions.send_keys_to_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_NAME_FIELD, new_category)
        self.common_actions.click_element(*self.service_appointment_page_locators.ADD_CATEGORY_DIALOG_CONFIRM_BUTTON)
        return self

    def delete_service_category(self, category_name):
        self.common_actions.click_element(*self.service_appointment_page_locators.EDIT_CATEGORY_BUTTON_IN_SERVICE_ITEM_LIST_PAGE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_DELETE_BUTTON(category_name))
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_TITLE)
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DESCRIPTION(category_name))
        self.common_actions.click_element(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DELETE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.DELETE_CATEGORY_DIALOG_DELETE_BUTTON)
        return self

    def verify_service_category_not_visible(self, category_name):
        self.common_actions.click_element(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_CLOSE_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CATEGORY_MANAGEMENT_MODAL_TITLE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.CATEGORY_NAME_IN_SERVICE_ITEM_LIST_PAGE(category_name))
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

    def select_fixed_price(self):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.FIXED_PRICE_METHOD)
        self.common_actions.click_element(*self.service_appointment_page_locators.FIXED_PRICE_METHOD)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.FIXED_PRICE_METHOD)
        return self

    def select_starting_price(self):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_DISPLAY_PRICE_METHOD)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.STARTING_PRICE_METHOD)
        self.common_actions.click_element(*self.service_appointment_page_locators.STARTING_PRICE_METHOD)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.STARTING_PRICE_METHOD)
        return self

    def select_single_choice(self):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.SINGLE_CHOICE_SUB_SERVICE_TYPE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SINGLE_CHOICE_SUB_SERVICE_TYPE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SINGLE_CHOICE_SUB_SERVICE_TYPE)
        return self

    def select_multiple_choice(self):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE)
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_SUB_SERVICE_TYPE)
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.MULTIPLE_CHOICE_SUB_SERVICE_TYPE)
        self.common_actions.click_element(*self.service_appointment_page_locators.MULTIPLE_CHOICE_SUB_SERVICE_TYPE)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.MULTIPLE_CHOICE_SUB_SERVICE_TYPE)
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

    def click_save_add_service_item_button(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CONFIRM_BUTTON)
        self.common_actions.wait_for_element_disappear(*self.service_appointment_page_locators.SERVICE_ITEM_MODAL_CONFIRM_BUTTON)
        return self

    def verify_service_item_name(self, item_name):
        self.common_actions.scroll_to_element(*self.service_appointment_page_locators.SERVICE_NAME_IN_SERVICE_ITEM_LIST_PAGE(item_name))
        return self

    def tap_online_booking(self):
        self.common_actions.click_element(*self.service_appointment_page_locators.ONLINE_BOOKING_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def verify_online_booking_page(self):
        self.common_actions.wait_for_element_visible(*self.service_appointment_page_locators.TITLE_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.DESCRIPTION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        self.common_actions.is_element_visible(*self.service_appointment_page_locators.CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE)
        return self