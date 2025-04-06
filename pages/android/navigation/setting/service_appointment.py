import time
import random

from datetime import datetime, timedelta
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.service_appointment_locators import ServiceAppointmentPageLocators

class ServiceAppointmentPage(CommonUseSection):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.appointment_code = None


    def tap_service_appointment_in_branch_settings_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_APPOINTMENT_IN_BRANCH_SETTING_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_appointment_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.BACK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.MEMBER_EXCLUSIVE_LINK_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.BOOKING_ISSUE_AND_NOTES_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.BOOKING_PRECAUTIONS_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DEPOSIT_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.ADVANCED_SETTINGS_IN_SERVICE_APPOINTMENT_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.BACK_TO_CALENDER_BUTTON_IN_SERVICE_APPOINTMENT_PAGE)
        return self

    def tap_member_exclusive_booking_link_copy_button(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.COPY_BUTTON_IN_MEMBER_EXCLUSIVE_LINK_IN_SERVICE_APPOINTMENT_PAGE).click()
        time.sleep(2)
        return self

    def verify_copy_link_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_COPY_LINK_DIALOG)
        self.driver.find_element(*ServiceAppointmentPageLocators.COPY_LINK_IN_COPY_LINK_DIALOG)
        self.driver.find_element(*ServiceAppointmentPageLocators.APPLY_LINE_LINK_IN_COPY_LINK_DIALOG)
        return self

    def tap_copy_link_in_copy_link_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.COPY_LINK_IN_COPY_LINK_DIALOG).click()
        time.sleep(2)
        return self

    def verify_copy_link_dialog_dismissed(self):
        try:
            self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_COPY_LINK_DIALOG)
            return False
        except NoSuchElementException:
            return True

    def tap_service_item_in_service_appointment_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SERVICE_APPOINTMENT_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_EDIT_BUTTON_IN_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_SERVICE_ITEM_IN_SERVICE_ITEM_PAGE)
        return self

    def tap_category_edit_button_in_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_EDIT_BUTTON_IN_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_category_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_CATEGORY_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_CATEGORY_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_CATEGORY_IN_CATEGORY_PAGE)
        return self

    def tap_add_category_in_category_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_CATEGORY_IN_CATEGORY_PAGE).click()
        time.sleep(2)
        return self

    def verify_add_category_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_ADD_CATEGORY_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_ADD_CATEGORY_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ADD_CATEGORY_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_NAME_IN_ADD_CATEGORY_PAGE)
        return self

    def enter_new_category_in_add_category_page(self, category_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_NAME_IN_ADD_CATEGORY_PAGE).send_keys(category_name)
        time.sleep(2)
        return self

    def tap_confirm_button_in_add_category_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ADD_CATEGORY_PAGE).click()
        time.sleep(2)
        return self

    def verify_category_added(self, category_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_ITEM_IN_CATEGORY_PAGE(self, category_name))
        return self

    def tap_close_button_in_category_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_CATEGORY_PAGE).click()
        time.sleep(2)
        return self

    def verify_category_displayed_in_service_item_page(self, category_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_ITEM_IN_SERVICE_ITEM_PAGE(self, category_name))
        return self

    def tap_category_item_in_service_item_page(self, category_name):
        category_item_locator = self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_ITEM_IN_SERVICE_ITEM_PAGE(self, category_name))
        category_item_locator.click()
        time.sleep(1)
        return not category_item_locator.is_enabled()

    def tap_add_service_item_in_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_SERVICE_ITEM_IN_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def _scroll_to_element(self, element_locator, max_swipes=3, timeout=2):
        """
        Scrolls the screen until the specified element is visible.

        Args:
            element_locator: Element locator tuple (strategy, value)
            max_swipes: Maximum number of swipe attempts
            timeout: Timeout in seconds for element searches

        Returns:
            bool: True if element found, False otherwise
        """
        from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

        try:
            # Try finding the element first without scrolling
            element = self.driver.find_element(*element_locator)

            # Check if element is already displayed, if so no need to scroll
            if element.is_displayed():
                return True

        except (NoSuchElementException, StaleElementReferenceException):
            pass

        # Element not visible or not found, scroll to find it
        for i in range(max_swipes):
            # Scroll down (swipe up)
            screen_size = self.driver.get_window_size()
            start_x = screen_size['width'] // 2
            start_y = screen_size['height'] * 0.8
            end_y = screen_size['height'] * 0.2

            self.driver.swipe(start_x, start_y, start_x, end_y, 500)
            time.sleep(0.5)

            try:
                # Try to find the element after scrolling
                element = self.driver.find_element(*element_locator)
                if element.is_displayed():
                    return True
            except (NoSuchElementException, StaleElementReferenceException):
                continue

        return False

    def verify_add_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.UPLOAD_IMAGE_BUTTON_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_NAME_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_CODE_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_INTRODUCTION_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_DURATION_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DURATION_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_PRICE_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_PRICE_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_DISPLAY_PRICE_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DISPLAY_PRICE_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DISPLAY_METHOD_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SUB_SERVICE_TYPE_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_SUB_SERVICE_IN_ADD_SERVICE_ITEM_PAGE)
        return self

    def enter_service_item_name_in_add_service_item_page(self, service_item_name):
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_ITEM_NAME_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_NAME_FIELD_IN_ADD_SERVICE_ITEM_PAGE).send_keys(service_item_name)
        time.sleep(2)
        return self

    def enter_service_code_in_add_service_item_page(self, service_item_code):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_CODE_FIELD_IN_ADD_SERVICE_ITEM_PAGE).send_keys(service_item_code)
        time.sleep(2)
        return self

    def is_introduction_toggle_on_in_add_service_item_page(self):
        try:
            element = self.driver.find_element(
                *ServiceAppointmentPageLocators.SERVICE_INTRODUCTION_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
            if element.is_displayed():
                return True
        except NoSuchElementException:
            pass
        # 若找不到該元素，點擊 toggle
        self.driver.find_element(
            *ServiceAppointmentPageLocators.SERVICE_INTRODUCTION_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)

    def tap_introduction_in_add_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_INTRODUCTION_FIELD_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_item_introduction_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CLEAR_BUTTON_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.INTRODUCTION_FIELD_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        return self

    def enter_introduction_in_introduction_dialog(self, service_item_introduction):
        self.driver.find_element(*ServiceAppointmentPageLocators.INTRODUCTION_FIELD_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).send_keys(service_item_introduction)
        time.sleep(2)
        return self

    def tap_confirm_button_in_introduction_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_INTRODUCTION_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_service_category_in_add_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_CATEGORY_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_category_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_SERVICE_CATEGORY_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_SERVICE_CATEGORY_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        return self

    def select_service_category(self, category_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_CATEGORY_ITEM_IN_SERVICE_CATEGORY_DIALOG_IN_ADD_SERVICE_ITEM_PAGE(self, category_name)).click()
        time.sleep(2)
        return self

    def service_category_dialog_dismissed(self):
        try:
            self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_SERVICE_CATEGORY_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
            return False
        except NoSuchElementException:
            return True

    def enter_service_duration_in_add_service_item_page(self, service_duration):
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_DURATION_FIELD_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DURATION_FIELD_IN_ADD_SERVICE_ITEM_PAGE).send_keys(service_duration)
        time.sleep(2)
        return self

    def enter_service_price_in_add_service_item_page(self, service_price):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_PRICE_FIELD_IN_ADD_SERVICE_ITEM_PAGE).send_keys(service_price)
        time.sleep(2)
        return self

    def tap_service_display_price_toggle(self):
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_DISPLAY_PRICE_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DISPLAY_PRICE_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_service_display_method_in_add_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DISPLAY_METHOD_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_display_method_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_SERVICE_DISPLAY_METHOD_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.STARTING_PRICE_IN_SERVICE_DISPLAY_METHOD_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.FIXED_PRICE_IN_SERVICE_DISPLAY_METHOD_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        return self

    def select_fixed_price_in_service_display_method_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.FIXED_PRICE_IN_SERVICE_DISPLAY_METHOD_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def select_starting_price_in_service_display_method_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.STARTING_PRICE_IN_SERVICE_DISPLAY_METHOD_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_sub_service_type_in_add_service_item_page(self):
        self._scroll_to_element(ServiceAppointmentPageLocators.SUB_SERVICE_TYPE_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SUB_SERVICE_TYPE_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_sub_service_type_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_SUB_SERVICE_TYPE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SINGLE_CHOICE_IN_SUB_SERVICE_TYPE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.MULTIPLE_CHOICE_IN_SUB_SERVICE_TYPE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        return self

    def select_multiple_choice_in_sub_service_type_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.MULTIPLE_CHOICE_IN_SUB_SERVICE_TYPE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def select_single_choice_in_sub_service_type_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SINGLE_CHOICE_IN_SUB_SERVICE_TYPE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_add_sub_service_in_add_service_item_page(self):
        self._scroll_to_element(ServiceAppointmentPageLocators.ADD_SUB_SERVICE_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_SUB_SERVICE_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_add_sub_service_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SUB_SERVICE_NAME_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DURATION_INCREASE_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.PRICE_INCREASE_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        return self

    def enter_sub_service_name_in_add_sub_service_dialog(self, sub_service_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SUB_SERVICE_NAME_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).send_keys(sub_service_name)
        time.sleep(2)
        return self

    def enter_duration_in_add_sub_service_dialog(self, duration):
        self.driver.find_element(*ServiceAppointmentPageLocators.DURATION_INCREASE_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).send_keys(duration)
        time.sleep(2)
        return self

    def enter_price_in_add_sub_service_dialog(self, price):
        self.driver.find_element(*ServiceAppointmentPageLocators.PRICE_INCREASE_FIELD_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).send_keys(price)
        time.sleep(2)
        return self

    def tap_confirm_button_in_add_sub_service_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ADD_SUB_SERVICE_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_confirm_button_in_add_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_close_button_in_add_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_edit_sub_service_in_add_service_item_page(self, sub_service_name):
        self._scroll_to_element(ServiceAppointmentPageLocators.EDIT_SUB_SERVICE_ITEM_IN_ADD_SERVICE_ITEM_PAGE(self, sub_service_name))
        self.driver.find_element(*ServiceAppointmentPageLocators.EDIT_SUB_SERVICE_ITEM_IN_ADD_SERVICE_ITEM_PAGE(self, sub_service_name)).click()
        time.sleep(2)
        return self

    def verify_edit_sub_service_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SUB_SERVICE_NAME_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DURATION_INCREASE_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.PRICE_INCREASE_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE)
        return self

    def enter_sub_service_name_in_edit_sub_service_dialog(self, sub_service_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SUB_SERVICE_NAME_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).send_keys(sub_service_name)
        time.sleep(2)
        return self

    def enter_duration_in_edit_sub_service_dialog(self, duration):
        self.driver.find_element(*ServiceAppointmentPageLocators.DURATION_INCREASE_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).clear()
        self.driver.find_element(*ServiceAppointmentPageLocators.DURATION_INCREASE_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).send_keys(duration)
        time.sleep(2)
        return self

    def enter_price_in_edit_sub_service_dialog(self, price):
        self.driver.find_element(*ServiceAppointmentPageLocators.PRICE_INCREASE_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).clear()
        self.driver.find_element(*ServiceAppointmentPageLocators.PRICE_INCREASE_FIELD_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).send_keys(price)
        time.sleep(2)
        return self

    def tap_confirm_button_in_edit_sub_service_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_EDIT_SUB_SERVICE_ITEM_DIALOG_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_delete_sub_service_in_add_service_item_page(self, sub_service_name):
        self._scroll_to_element(ServiceAppointmentPageLocators.DELETE_SUB_SERVICE_ITEM_IN_ADD_SERVICE_ITEM_PAGE(self, sub_service_name))
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_SUB_SERVICE_ITEM_IN_ADD_SERVICE_ITEM_PAGE(self, sub_service_name)).click()
        time.sleep(2)
        return self

    def verify_service_item_added(self, service_item_name):
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SERVICE_ITEM_PAGE(self, service_item_name))
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SERVICE_ITEM_PAGE(self, service_item_name))
        return self


    def tap_service_item_in_service_item_page(self, service_item_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SERVICE_ITEM_PAGE(self, service_item_name)).click()
        time.sleep(2)
        return self

    def verify_edit_service_item_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.EDIT_SERVICE_ITEM_IN_SERVICE_ITEM_DIALOG)
        self.driver.find_element(*ServiceAppointmentPageLocators.COPY_SERVICE_ITEM_IN_SERVICE_ITEM_DIALOG)
        return self

    def tap_edit_service_item_in_edit_service_item_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.EDIT_SERVICE_ITEM_IN_SERVICE_ITEM_DIALOG).click()
        time.sleep(2)
        return self

    def verify_edit_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.UPLOAD_IMAGE_BUTTON_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_NAME_FIELD_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_CODE_FIELD_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_INTRODUCTION_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_DURATION_FIELD_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DURATION_FIELD_IN_EDIT_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_PRICE_FIELD_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_PRICE_FIELD_IN_EDIT_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_DISPLAY_PRICE_TOGGLE_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DISPLAY_PRICE_TOGGLE_IN_EDIT_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_DISPLAY_METHOD_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DISPLAY_METHOD_IN_EDIT_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.ADD_SUB_SERVICE_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_SUB_SERVICE_IN_EDIT_SERVICE_ITEM_PAGE)
        self._scroll_to_element(ServiceAppointmentPageLocators.SUB_SERVICE_TYPE_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SUB_SERVICE_TYPE_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_SERVICE_ITEM_IN_EDIT_SERVICE_ITEM_PAGE)
        return self

    def tap_close_button_in_edit_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_EDIT_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def edit_service_item_name_in_edit_service_item_page(self, service_item_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_NAME_FIELD_IN_EDIT_SERVICE_ITEM_PAGE).send_keys(service_item_name)
        time.sleep(2)
        return self

    def edit_service_code_in_edit_service_item_page(self, service_item_code):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_CODE_FIELD_IN_EDIT_SERVICE_ITEM_PAGE).send_keys(service_item_code)
        time.sleep(2)
        return self

    def is_introduction_toggle_on_in_edit_service_item_page(self):
        try:
            element = self.driver.find_element(
                *ServiceAppointmentPageLocators.SERVICE_INTRODUCTION_FIELD_IN_EDIT_SERVICE_ITEM_PAGE)
            if element.is_displayed():
                return True
        except NoSuchElementException:
            pass
        # 若找不到該元素，點擊 toggle
        self.driver.find_element(
            *ServiceAppointmentPageLocators.SERVICE_INTRODUCTION_TOGGLE_IN_ADD_SERVICE_ITEM_PAGE).click()
        time.sleep(2)

    def tap_introduction_in_edit_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_INTRODUCTION_FIELD_IN_EDIT_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_service_category_in_edit_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_CATEGORY_IN_EDIT_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def enter_service_duration_in_edit_service_item_page(self, service_duration):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DURATION_FIELD_IN_EDIT_SERVICE_ITEM_PAGE).send_keys(service_duration)
        time.sleep(2)
        return self

    def enter_service_price_in_edit_service_item_page(self, service_price):
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_PRICE_FIELD_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_PRICE_FIELD_IN_EDIT_SERVICE_ITEM_PAGE).send_keys(service_price)
        time.sleep(2)
        return self

    def tap_service_display_method_in_edit_service_item_page(self):
        self._scroll_to_element(ServiceAppointmentPageLocators.SERVICE_DISPLAY_METHOD_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_DISPLAY_METHOD_IN_EDIT_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_sub_service_type_in_edit_service_item_page(self):
        self._scroll_to_element(ServiceAppointmentPageLocators.SUB_SERVICE_TYPE_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.SUB_SERVICE_TYPE_IN_EDIT_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_confirm_button_in_edit_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_EDIT_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_item_edited(self, service_item_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SERVICE_ITEM_PAGE(self, service_item_name))
        return self

    def tap_copy_service_item_in_edit_service_item_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.COPY_SERVICE_ITEM_IN_SERVICE_ITEM_DIALOG).click()
        time.sleep(3)
        return self

    def verify_service_item_copied(self, service_item_name):
        elements = self.driver.find_elements(
            *ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SERVICE_ITEM_PAGE(self, service_item_name))
        assert len(elements) >= 2, f"Expected more than 2 service item elements, but found {len(elements)}"
        return self

    def tap_delete_service_item_in_edit_service_item_page(self):
        self._scroll_to_element(ServiceAppointmentPageLocators.DELETE_SERVICE_ITEM_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_SERVICE_ITEM_IN_EDIT_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_delete_service_item_alert_dialog(self, service_item_nam):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CANCEL_BUTTON_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_BUTTON_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE(self, service_item_nam))
        return self

    def tap_delete_button_in_delete_service_item_alert_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_BUTTON_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_EDIT_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_item_deleted_in_service_item_page(self, service_item_name):
        try:
            self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SERVICE_ITEM_PAGE(self, service_item_name))
            return False
        except NoSuchElementException:
            return True

    def tap_delete_all_service_item_in_service_item_page(self, service_item_name):
        while True:
            elements = self.driver.find_elements(*ServiceAppointmentPageLocators.DELETE_SERVICE_ITEM_IN_SERVICE_ITEM_PAGE(self, service_item_name))
            if len(elements) == 0:
                break
            elements[0].click()
            time.sleep(1)
            self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_BUTTON_IN_DELETE_SERVICE_ITEM_ALERT_DIALOG_IN_SERVICE_ITEM_PAGE).click()
            time.sleep(1)
        return self

    def tap_delete_category_item_in_category_page(self, category_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_CATEGORY_ITEM_IN_CATEGORY_PAGE(self, category_name)).click()
        time.sleep(2)
        return self

    def tap_delete_button_in_delete_category_item_alert_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_BUTTON_IN_DELETE_CATEGORY_ITEM_ALERT_DIALOG_IN_CATEGORY_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_category_deleted_in_category_page(self, category_name):
        try:
            self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_ITEM_IN_CATEGORY_PAGE(self, category_name))
            return False
        except NoSuchElementException:
            return True

    def verify_service_category_deleted_in_service_item_page(self, category_name):
        try:
            self.driver.find_element(*ServiceAppointmentPageLocators.CATEGORY_ITEM_IN_SERVICE_ITEM_PAGE(self, category_name))
            return False
        except NoSuchElementException:
            return True

    def tap_close_button_in_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_online_booking_management_button_in_service_appointment_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_MANAGEMENT_IN_SERVICE_APPOINTMENT_PAGE).click()
        time.sleep(2)
        return self

    def verify_online_booking_management_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_ONLINE_BOOKING_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE).is_displayed()
        return self

    def tap_personal_online_booking_management_in_online_booking_management_page(self, personal_online_booking_management_name):
        self._scroll_to_element(ServiceAppointmentPageLocators.PERSONAL_ONLINE_BOOKING_MANAGEMENT_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(self, personal_online_booking_management_name))
        self.driver.find_element(*ServiceAppointmentPageLocators.PERSONAL_ONLINE_BOOKING_MANAGEMENT_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(self, personal_online_booking_management_name)).click()
        time.sleep(2)
        return self

    def verify_personal_online_booking_page(self, personal_online_booking_management_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_PERSONAL_ONLINE_BOOKING_PAGE(self, personal_online_booking_management_name)).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_TIME_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_PERSONAL_ONLINE_BOOKING_TOGGLE_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_DAY_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.LATEST_APPOINTMENT_TIME_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.ADVANCE_SETTING_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_TIME_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_OPEN_TIME_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        self.driver.find_element(*ServiceAppointmentPageLocators.MAIN_SERVICE_ITEM_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_SELECTION_TYPE_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_SELECTION_TYPE_DESCRIPTION_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.ADDITIONAL_SERVICE_ITEM_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.ADDITIONAL_SERVICE_ITEM_DESCRIPTION_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).is_displayed()
        return self

    def tap_open_setting_tab_in_personal_online_booking_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_open_days_in_open_setting_tab(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_DAY_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_random_specific_day_in_open_days(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SPECIFIC_OPEN_DAYS_IN_OPEN_DAYS_PAGE).click()
        time.sleep(2)
        random_num = random.randint(6, 28)
        print(f"Random number: {random_num}")
        locator = ServiceAppointmentPageLocators.DAYS_IN_SPECIFIC_DAYS_PAGE(self, random_num)
        self._scroll_to_element(locator)
        self.driver.find_element(*locator).click()
        time.sleep(1)
        return self

    def tap_specific_time_in_open_days(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SPECIFIC_OPEN_TIMES_IN_OPEN_DAYS_PAGE).click()
        time.sleep(2)
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_FEATURE_NOT_AVAILABLE_DIALOG).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_FEATURE_NOT_AVAILABLE_DIALOG).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.GOT_IT_BUTTON_IN_FEATURE_NOT_AVAILABLE_DIALOG).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.GOT_IT_BUTTON_IN_FEATURE_NOT_AVAILABLE_DIALOG).click()
        time.sleep(2)
        return self

    def tap_random_open_months_available_in_open_days(self):
        random_month = random.randint(1, 7)
        print(f"Random month: {random_month}")
        if random_month == 7:
            self.driver.find_element(*ServiceAppointmentPageLocators.ALL_OPEN_AVAILABLE_IN_OPEN_DAYS_PAGE).click()
            time.sleep(1)
        else:
            self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_MONTHS_AVAILABLE_IN_OPEN_DAYS_PAGE(self, str(random_month))).click()
            time.sleep(1)
        return self

    def tap_confirm_button_in_open_days(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_OPEN_DAYS_PAGE).click()
        time.sleep(2)
        return self

    def tap_latest_appointment_time_in_personal_online_booking_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.LATEST_APPOINTMENT_TIME_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_random_latest_appointment_time_in_latest_appointment_time(self):
        random_num = random.randint(0, 13)
        print(f"Random number: {random_num}")
        locator = ServiceAppointmentPageLocators.LAST_APPOINTMENT_TIME_IN_LATEST_APPOINTMENT_TIME_PAGE(self, random_num)
        self.driver.find_element(*locator).click()
        time.sleep(2)
        return self

    def tap_advance_setting_in_personal_online_booking_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.ADVANCE_SETTING_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_random_advance_setting_in_advance_setting(self):
        random_num_1 = random.randint(0, 3)
        random_num_2 = random.randint(3, 99)
        print(f"Random number: {random_num_1}")
        print(f"Random number: {random_num_2}")
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_LIMIT_MINIMUM_IN_ADVANCE_SETTING_DIALOG_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).clear()
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_LIMIT_MINIMUM_IN_ADVANCE_SETTING_DIALOG_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).send_keys(random_num_1)
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_LIMIT_MAXIMUM_IN_ADVANCE_SETTING_DIALOG_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).clear()
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_LIMIT_MAXIMUM_IN_ADVANCE_SETTING_DIALOG_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).send_keys(random_num_2)
        return self

    def tap_open_time_tab_in_personal_online_booking_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_TIME_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_open_time_today_in_open_time_tab(self):
        today = datetime.now()
        formatted_date = today.strftime("%d")
        formatted_date = str(int(formatted_date))
        print(f"Formatted date: {formatted_date}")
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_TIME_ADD_TIME_BUTTON_IN_OPEN_TIME_TAB(self, formatted_date)).click()
        time.sleep(1)
        return self

    def tap_display_early_morning_in_edit_open_time_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.DISPLAY_EARLY_MORNING_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        return self

    def tap_random_time_in_edit_open_time_page(self):
        random_hour = random.randint(0, 23)
        random_minute = random.choice([0, 10, 20, 30, 40, 50])
        formatted_time = f"{random_hour}:{random_minute:02d}"
        print(f"Random Time: {formatted_time}")
        locator = ServiceAppointmentPageLocators.TIME_IN_EDIT_OPEN_TIME_PAGE(self, formatted_time)
        self._scroll_to_element(locator)
        self.driver.find_element(*locator).click()
        time.sleep(1)
        return self

    def tap_close_button_in_edit_open_time_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(2)
        return self

    def tap_edit_open_time_today_in_open_time_tab(self):
        today = datetime.now()
        formatted_date = today.strftime("%d")
        formatted_date = str(int(formatted_date))
        print(f"Formatted date: {formatted_date}")
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_TIME_EDIT_TIME_BUTTON_IN_OPEN_TIME_TAB(self, formatted_date)).click()
        time.sleep(1)
        return self

    def copy_open_time_in_edit_open_time_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.COPY_TODAY_SCHEDULE_BUTTON_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        return self

    def tap_specific_time_in_copy_dialog_in_edit_open_time_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.COPY_TO_SPECIFIC_DATE_BUTTON_IN_COPY_DIALOG_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        return self

    def select_next_day_open_time_in_copy_specific_time_page(self):
        today = datetime.now()
        next_day = today + timedelta(days=1)
        formatted_date = next_day.strftime("%d")
        formatted_date = str(int(formatted_date))
        print(f"Formatted date: {formatted_date}")
        self.driver.find_element(*ServiceAppointmentPageLocators.DATE_IN_COPY_SPECIFIC_DATE_PAGE(self, formatted_date)).click()
        time.sleep(1)
        formatted_date = next_day.strftime("%Y/%m/%d")
        print(f"Formatted date: {formatted_date}")
        self.driver.find_element(*ServiceAppointmentPageLocators.DATE_VALUE_IN_COPY_SPECIFIC_DATE_PAGE(self, formatted_date)).is_displayed()
        return self

    def tap_confirm_button_in_copy_specific_time_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_COPY_SPECIFIC_DATE_PAGE).click()
        time.sleep(2)
        return self

    def tap_date_range_in_copy_dialog_in_edit_open_time_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.COPY_TO_DATE_RANGE_BUTTON_IN_COPY_DIALOG_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        return self

    def select_repeat_open_time_range_in_copy_range_page(self):
        today = datetime.now()
        start_date = today.strftime("%d")
        start_date = str(int(start_date))
        end_date = today + timedelta(days=7)
        end_date = end_date.strftime("%d")
        end_date = str(int(end_date))
        print(f"Start date: {start_date}")
        print(f"End date: {end_date}")
        random_num = random.randint(1, 7)
        print(f"Random number: {random_num}")
        self.driver.find_element(*ServiceAppointmentPageLocators.START_DATE_IN_COPY_DATE_RANGE_PAGE).click()
        self.driver.find_element(*ServiceAppointmentPageLocators.START_DATE_IN_RANGE_DATE_DIALOG(self, start_date)).click()
        time.sleep(1)
        start_date = today.strftime("%Y/%m/%d")
        self.driver.find_element(*ServiceAppointmentPageLocators.START_DATE_VALUE_IN_RANGE_DATE_DIALOG(self, start_date)).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_COPY_DATE_RANGE_PAGE).click()
        time.sleep(1)
        self.driver.find_element(*ServiceAppointmentPageLocators.END_DATE_IN_COPY_DATE_RANGE_PAGE).click()
        self.driver.find_element(*ServiceAppointmentPageLocators.END_DATE_IN_RANGE_DATE_DIALOG(self, end_date)).click()
        time.sleep(1)
        end_date = today + timedelta(days=7)
        end_date = end_date.strftime("%Y/%m/%d")
        self.driver.find_element(*ServiceAppointmentPageLocators.END_DATE_VALUE_IN_RANGE_DATE_DIALOG(self, end_date)).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_COPY_DATE_RANGE_PAGE).click()
        time.sleep(1)
        self.driver.find_element(*ServiceAppointmentPageLocators.REPEAT_WEEKDAY_IN_COPY_DATE_RANGE_PAGE(self, random_num)).click()
        time.sleep(1)
        return self

    def tap_confirm_button_in_copy_range_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_COPY_DATE_RANGE_PAGE).click()
        time.sleep(2)
        return self

    def tap_quick_close_button_in_edit_open_time_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.QUICK_CLOSE_BUTTON_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(2)
        return self

    def tap_today_close_in_quick_close_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TODAY_CLOSE_IN_QUICK_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        return self

    def verify_today_close_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_TODAY_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_TODAY_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_TODAY_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CANCEL_BUTTON_IN_TODAY_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE)
        return self

    def tap_confirm_button_in_today_close_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(2)
        return self

    def tap_range_close_in_quick_close_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.RANGE_CLOSE_IN_QUICK_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        return self

    def select_range_close_in_range_close_page(self):
        today = datetime.now()
        start_date = today.strftime("%d")
        start_date = str(int(start_date))
        end_date = today + timedelta(days=7)
        end_date = end_date.strftime("%d")
        end_date = str(int(end_date))
        print(f"Start date: {start_date}")
        print(f"End date: {end_date}")
        self.driver.find_element(*ServiceAppointmentPageLocators.START_DATE_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE).click()
        self.driver.find_element(*ServiceAppointmentPageLocators.START_DATE_IN_RANGE_DATE_DIALOG(self, start_date)).click()
        time.sleep(1)
        start_date = today.strftime("%Y/%m/%d")
        self.driver.find_element(*ServiceAppointmentPageLocators.START_DATE_VALUE_IN_RANGE_DATE_DIALOG(self, start_date)).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        self.driver.find_element(*ServiceAppointmentPageLocators.END_DATE_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE).click()
        self.driver.find_element(*ServiceAppointmentPageLocators.END_DATE_IN_RANGE_DATE_DIALOG(self, end_date)).click()
        time.sleep(1)
        end_date = today + timedelta(days=7)
        end_date = end_date.strftime("%Y/%m/%d")
        self.driver.find_element(*ServiceAppointmentPageLocators.END_DATE_VALUE_IN_RANGE_DATE_DIALOG(self, end_date)).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        return self

    def tap_confirm_button_in_range_close_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_RANGE_CLOSE_PAGE_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(2)
        return self

    def tap_all_close_in_quick_close_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.ALL_CLOSE_IN_QUICK_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(1)
        return self

    def verify_all_close_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE)
        self.driver.find_element(*ServiceAppointmentPageLocators.CANCEL_BUTTON_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE)
        return self

    def tap_confirm_button_in_all_close_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ALL_CLOSE_DIALOG_IN_EDIT_OPEN_TIME_PAGE).click()
        time.sleep(2)
        return self

    def tap_open_items_tab_in_personal_online_booking_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_main_service_item_in_open_items_tab(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.MAIN_SERVICE_ITEM_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_service_item_in_select_main_service_item_page(self, service_item_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_ITEM_IN_SELECT_MAIN_SERVICE_ITEM_PAGE(self, service_item_name)).click()
        time.sleep(2)
        return self

    def tap_confirm_button_in_select_main_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_SELECT_MAIN_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_online_booking_item_in_open_items_tab(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.ONLINE_BOOKING_SELECTION_TYPE_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_single_choice_in_select_online_booking_item_dialog(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.SINGLE_CHOICE_IN_ONLINE_BOOKING_SELECTION_TYPE_DIALOG).click()
        time.sleep(2)
        return self

    def tap_additional_service_item_in_open_items_tab(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.ADDITIONAL_SERVICE_ITEM_IN_OPEN_ITEM_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_confirm_button_in_select_additional_service_item_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_SELECT_ADDITIONAL_SERVICE_ITEM_PAGE).click()
        time.sleep(2)
        return self

    def tap_close_button_in_personal_online_booking_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def open_personal_online_booking_toggle(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_PERSONAL_ONLINE_BOOKING_TOGGLE_IN_OPEN_SETTING_TAB_IN_PERSONAL_ONLINE_BOOKING_PAGE).click()
        time.sleep(2)
        return self

    def tap_personal_online_booking_closed_section_expand_in_online_booking_management_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.PERSONAL_ONLINE_BOOKING_CLOSE_EXPAND_IN_ONLINE_BOOKING_MANAGEMENT_PAGE).click()
        time.sleep(2)
        return self

    def verify_personal_online_booking_closed_section_in_online_booking_management_page(self, service_item_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.PERSONAL_ONLINE_BOOKING_MANAGEMENT_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(self, service_item_name)).is_displayed()
        return self

    def tap_add_unspecified_appointment_combination_in_service_appointment_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE).click()
        time.sleep(2)
        return self

    def verify_add_unspecified_appointment_combination_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.TITLE_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.UPLOAD_IMAGE_BUTTON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.COMBINATION_NAME_FIELD_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.COMBINATION_INTRODUCTION_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.ALL_SELECTED_SERVICE_PERSON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).is_displayed()
        return self

    def enter_unspecified_appointment_combination_name_in_add_unspecified_appointment_combination_page(self, service_combination_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.COMBINATION_NAME_FIELD_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).send_keys(service_combination_name)
        time.sleep(2)
        return self

    def enter_unspecified_appointment_combination_introduction_in_add_unspecified_appointment_combination_page(self, service_combination_introduction):
        self.driver.find_element(*ServiceAppointmentPageLocators.COMBINATION_INTRODUCTION_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).click()
        time.sleep(1)
        self.driver.find_element(*ServiceAppointmentPageLocators.COMBINATION_INTRODUCTION_FIELD_IN_COMBINATION_INTRODUCTION_DIALOG_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).send_keys(service_combination_introduction)
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_COMBINATION_INTRODUCTION_DIALOG_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).click()
        time.sleep(1)
        return self

    def tap_service_personnel_in_add_unspecified_appointment_combination_page(self, service_personnel_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SELECT_SERVICE_PERSON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE(self, service_personnel_name)).click()
        time.sleep(2)
        return self

    def tap_confirm_button_in_add_unspecified_appointment_combination_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CONFIRM_BUTTON_IN_ADD_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_unspecified_appointment_combination_added_in_service_appointment_page(self, service_combination_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(self, service_combination_name))
        return self

    def tap_service_unspecified_appointment_combination_in_service_appointment_page(self, service_combination_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(self, service_combination_name)).click()
        time.sleep(2)
        return self

    def tap_service_personnel_in_edit_unspecified_appointment_combination_page(self, service_personnel_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_PERSONNEL_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE(self, service_personnel_name)).click()
        time.sleep(2)
        return self

    def tap_open_item_setting_tab_in_edit_unspecified_appointment_combination_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.OPEN_ITEM_SETTING_TAB_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).click()
        time.sleep(2)
        return self

    def tap_main_service_item_in_open_item_setting_tab_in_edit_unspecified_appointment_combination_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.MAIN_SERVICE_ITEM_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).click()
        time.sleep(2)
        return self

    def tap_close_button_in_edit_unspecified_appointment_combination_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).click()
        time.sleep(2)
        return self

    def tap_delete_button_in_edit_unspecified_appointment_combination_page(self, service_combination_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_BUTTON_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).click()
        time.sleep(1)
        self.driver.find_element(*ServiceAppointmentPageLocators.DESCRIPTION_IN_DELETE_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_ALERT_DIALOG_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE(self, service_combination_name)).is_displayed()
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_BUTTON_IN_DELETE_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_ALERT_DIALOG_IN_EDIT_SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_unspecified_appointment_combination_deleted_in_service_appointment_page(self, service_combination_name):
        try:
            self.driver.find_element(*ServiceAppointmentPageLocators.SERVICE_UNSPECIFIED_APPOINTMENT_COMBINATION_IN_ONLINE_BOOKING_MANAGEMENT_PAGE(self, service_combination_name)).is_displayed()
            return False
        except NoSuchElementException:
            return True

    def tap_close_button_in_online_booking_management_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.CLOSE_BUTTON_IN_ONLINE_BOOKING_MANAGEMENT_PAGE).click()
        time.sleep(2)
        return self

    def tap_delete_service_item_in_service_item_page(self, service_item_name):
        self.driver.find_element(*ServiceAppointmentPageLocators.DELETE_SERVICE_ITEM_IN_SERVICE_ITEM_PAGE(self, service_item_name)).click()
        time.sleep(2)
        return self

    def tap_back_button_in_service_appointment_page(self):
        self.driver.find_element(*ServiceAppointmentPageLocators.BACK_BUTTON_IN_SERVICE_APPOINTMENT_PAGE).click()
        time.sleep(2)
        return self


















