import time
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.service_persionnel_locators import ServicePersonnelPageLocators
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class ServicePersonnelPage(CommonUseSection):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.service_personnel = None

    def tap_service_personnel_in_branch_settings_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.SERVICE_PERSONNEL_IN_BRANCH_SETTING_PAGE).click()
        time.sleep(2)
        return self

    def tap_delete_service_personnel_in_service_personnel_page(self, service_personnel_name):
        locator = ServicePersonnelPageLocators.DELETE_SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE(self, service_personnel_name)
        self._scroll_to_element(locator)
        self.driver.find_element(*locator).click()
        time.sleep(2)
        return self


    def verify_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.TITLE_IN_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.DESCRIPTION_IN_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CLOSE_BUTTON_IN_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.ADD_SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE).is_displayed()
        return self

    def tap_add_service_personnel_in_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.ADD_SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE).click()
        time.sleep(2)
        return self

    def verify_add_service_personnel_alert_dialog(self):
        self.driver.find_element(*ServicePersonnelPageLocators.DESCRIPTION_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CANCEL_BUTTON_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.ADD_BUTTON_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        return self

    def tap_cancel_button_in_add_service_personnel_alert_dialog(self):
        self.driver.find_element(*ServicePersonnelPageLocators.CANCEL_BUTTON_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG).click()
        time.sleep(2)
        return self

    def verify_add_service_personnel_alert_dialog_dismissed(self):
        try:
            self.driver.find_element(*ServicePersonnelPageLocators.DESCRIPTION_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
            return False
        except NoSuchElementException:
            return True

    def tap_add_button_in_add_service_personnel_alert_dialog(self):
        self.driver.find_element(*ServicePersonnelPageLocators.ADD_BUTTON_IN_ADD_SERVICE_PERSONNEL_ALERT_DIALOG).click()
        time.sleep(2)
        return self

    def verify_add_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.TITLE_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CLOSE_BUTTON_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CONFIRM_BUTTON_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.UPLOAD_IMAGE_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.NAME_FIELD_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CUSTOM_PERSONNEL_COLOR_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.PERSONNEL_INTRODUCTION_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.EXPAND_ADVANCED_SETTINGS_BUTTON_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        return self

    def enter_name_in_add_service_personnel_page(self, service_personnel_name):
        self.driver.find_element(*ServicePersonnelPageLocators.NAME_FIELD_IN_ADD_SERVICE_PERSONNEL_PAGE).send_keys(service_personnel_name)
        time.sleep(2)
        return self

    def select_random_color_in_personnel_color(self):
        random_num = random.randint(1, 7)
        random_color = ServicePersonnelPageLocators.SELECT_PERSONNEL_COLOR_IN_ADD_SERVICE_PERSONNEL_PAGE(self, random_num)
        print(random_color)
        self.driver.find_element(*random_color).click()
        time.sleep(2)
        return self

    def tap_introduction_in_add_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.PERSONNEL_INTRODUCTION_IN_ADD_SERVICE_PERSONNEL_PAGE).click()
        time.sleep(2)
        return self

    def verify_personnel_introduction_dialog(self):
        self.driver.find_element(*ServicePersonnelPageLocators.TITLE_IN_PERSONNEL_INTRODUCTION_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CLOSE_BUTTON_IN_PERSONNEL_INTRODUCTION_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.INTRODUCTION_TEXT_IN_PERSONNEL_INTRODUCTION_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CLEAR_BUTTON_IN_PERSONNEL_INTRODUCTION_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CONFIRM_BUTTON_IN_PERSONNEL_INTRODUCTION_DIALOG).is_displayed()
        return self

    def enter_introduction_in_introduction_dialog(self, service_personnel_introduction):
        self.driver.find_element(*ServicePersonnelPageLocators.INTRODUCTION_TEXT_IN_PERSONNEL_INTRODUCTION_DIALOG).send_keys(service_personnel_introduction)
        time.sleep(2)
        return self

    def tap_confirm_button_in_introduction_dialog(self):
        self.driver.find_element(*ServicePersonnelPageLocators.CONFIRM_BUTTON_IN_PERSONNEL_INTRODUCTION_DIALOG).click()
        time.sleep(2)
        return self

    def tap_expand_advanced_settings_button_in_add_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.EXPAND_ADVANCED_SETTINGS_BUTTON_IN_ADD_SERVICE_PERSONNEL_PAGE).click()
        time.sleep(2)
        return self

    def verify_advanced_settings_section_expanded(self):
        self.driver.find_element(*ServicePersonnelPageLocators.SERVICE_COUNT_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.SERVICE_COUNT_FIELD_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.SERVICE_QUANTITY_RANGE_IN_ADD_SERVICE_PERSONNEL_PAGE).is_displayed()
        return self

    def enter_random_service_count_in_add_service_personnel_page(self):
        random_num = random.randint(1, 99)
        service_count = str(random_num)
        self.driver.find_element(*ServicePersonnelPageLocators.SERVICE_COUNT_FIELD_IN_ADD_SERVICE_PERSONNEL_PAGE).send_keys(service_count)
        time.sleep(2)
        return self

    def tap_confirm_button_in_add_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.CONFIRM_BUTTON_IN_ADD_SERVICE_PERSONNEL_PAGE).click()
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
            bool: True if an the element found, False otherwise
        """

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

    def verify_new_service_personnel_added(self, service_personnel_name):
        locator = ServicePersonnelPageLocators.SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE(self, service_personnel_name)
        print(locator)
        self._scroll_to_element(locator)
        return self

    def tap_service_personnel_in_service_personnel_page(self, service_personnel_name):
        locator = ServicePersonnelPageLocators.SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE(self, service_personnel_name)
        self._scroll_to_element(locator)
        self.driver.find_element(*locator).click()
        time.sleep(2)
        return self

    def verify_edit_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.TITLE_IN_EDIT_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CLOSE_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CONFIRM_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.UPLOAD_IMAGE_IN_EDIT_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.NAME_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CUSTOM_PERSONNEL_COLOR_IN_EDIT_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.PERSONNEL_INTRODUCTION_IN_EDIT_SERVICE_PERSONNEL_PAGE).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.EXPAND_ADVANCED_SETTINGS_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE).is_displayed()
        return self

    def enter_name_in_edit_service_personnel_page(self, service_personnel_name):
        self.driver.find_element(*ServicePersonnelPageLocators.NAME_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE).send_keys(service_personnel_name)
        time.sleep(2)
        return self

    def tap_introduction_in_edit_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.PERSONNEL_INTRODUCTION_IN_EDIT_SERVICE_PERSONNEL_PAGE).click()
        time.sleep(2)
        return self

    def tap_expand_advanced_settings_button_in_edit_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.EXPAND_ADVANCED_SETTINGS_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE).click()
        time.sleep(2)
        return self

    def enter_random_service_count_in_edit_service_personnel_page(self):
        random_num = random.randint(1, 99)
        service_count = str(random_num)
        self.driver.find_element(*ServicePersonnelPageLocators.SERVICE_COUNT_FIELD_IN_EDIT_SERVICE_PERSONNEL_PAGE).send_keys(service_count)
        time.sleep(2)
        return self

    def tap_confirm_button_in_edit_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.CONFIRM_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE).click()
        time.sleep(2)
        return self

    def verify_service_personnel_updated(self, service_personnel_name):
        locator = ServicePersonnelPageLocators.SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE(self, service_personnel_name)
        self._scroll_to_element(locator)
        return self

    def tap_delete_button_in_edit_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.DELETE_BUTTON_IN_EDIT_SERVICE_PERSONNEL_PAGE).click()
        time.sleep(2)
        return self

    def verify_delete_service_personnel_alert_dialog(self, service_personnel_name):
        self.driver.find_element(*ServicePersonnelPageLocators.TITLE_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        description = ServicePersonnelPageLocators.DESCRIPTION_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG(self, service_personnel_name)
        self.driver.find_element(*description).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.DELETE_ITEM_1_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.DELETE_ITEM_2_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.DELETE_INPUT_FIELD_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.CANCEL_BUTTON_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        self.driver.find_element(*ServicePersonnelPageLocators.DELETE_BUTTON_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).is_displayed()
        # 確認 DELETE 按鈕為 disable 狀態
        delete_buttons = self.driver.find_elements(*ServicePersonnelPageLocators.DELETE_BUTTON_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG)
        if delete_buttons:
            return not delete_buttons[0].is_enabled()
        return False

    def enter_delete_text_in_delete_service_personnel_alert_dialog(self):
        self.driver.find_element(*ServicePersonnelPageLocators.DELETE_INPUT_FIELD_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).send_keys("Delete")
        time.sleep(2)
        self.driver.find_element(*ServicePersonnelPageLocators.DELETE_BUTTON_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).is_enabled()
        return self

    def tap_delete_button_in_delete_service_personnel_alert_dialog(self):
        self.driver.find_element(*ServicePersonnelPageLocators.DELETE_BUTTON_IN_DELETE_SERVICE_PERSONNEL_ALERT_DIALOG).click()
        time.sleep(2)
        return self

    def verify_service_personnel_not_present(self ,service_personnel_name):
        try:
            locator = ServicePersonnelPageLocators.SERVICE_PERSONNEL_IN_SERVICE_PERSONNEL_PAGE(self, service_personnel_name)
            self._scroll_to_element(locator, max_swipes=1)
            self.driver.find_element(*locator).is_displayed()
            return False
        except NoSuchElementException:
            return True

    def tap_close_button_in_service_personnel_page(self):
        self.driver.find_element(*ServicePersonnelPageLocators.CLOSE_BUTTON_IN_SERVICE_PERSONNEL_PAGE).click()
        time.sleep(2)
        return self

