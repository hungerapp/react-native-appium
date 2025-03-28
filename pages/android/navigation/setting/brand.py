import time
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.navigation.setting.brand_locators import BrandPageLocators


class BrandPage:
    def __init__(self, driver):
        self.driver = driver
        self.common_use = CommonUseSection(driver)
        self.brand_locators = BrandPageLocators()

    def tap_settings_option(self):
        self.driver.find_element(*self.brand_locators.SETTINGS_OPTION_IN_NAVIGATION).click()
        time.sleep(0.5)
        return self

    def verify_branch_settings_page(self):
        time.sleep(1)
        try:
            # Check for the Branch Settings page element
            branch_settings_element = self.driver.find_element(*self.brand_locators.BRANCH_SETTINGS_PAGE)
            return branch_settings_element.is_displayed()
        except NoSuchElementException:
            print("Branch Settings page not found")
            return False
        except Exception as e:
            print(f"Error verifying Branch Settings page: {e}")
            return False

    def tap_branch_name_in_branch_setting_page(self):
        self.driver.find_element(*self.brand_locators.BRANCH_NAME_IN_BRANCH_SETTINGS_PAGE).click()
        time.sleep(0.5)
        return self

    def verify_branch_branch_info_page(self):
        time.sleep(1)
        try:
            # Check for the Branch Name element which should be visible on the Branch Settings page
            branch_name_element = self.driver.find_element(*self.brand_locators.BRANCH_BRAND_INFO_PAGE)
            return branch_name_element.is_displayed()
        except NoSuchElementException:
            print("Branch Name element not found")
            return False
        except Exception as e:
            print(f"Error verifying Branch Name in Branch Settings page: {e}")
            return False

    def tap_confirm_edit_button_in_branch_brand_info_page(self):
        self.driver.find_element(*self.brand_locators.CONFIRM_BUTTON_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        return self

    def verify_return_to_branch_settings_page(self):
        time.sleep(1)
        try:
            # Check for the Branch Name element which should be visible on the Branch Settings page
            branch_name_element = self.driver.find_element(*self.brand_locators.BRANCH_NAME_IN_BRANCH_SETTINGS_PAGE)
            return branch_name_element.is_displayed()
        except Exception as e:
            print(f"Failed to verify return to Branch Settings page: {e}")
            return False

    def enter_new_branch_name_in_branch_brand_info_page(self, new_branch_name):
        self.driver.find_element(*self.brand_locators.BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE).clear()
        time.sleep(0.5)
        # Enter new branch name
        self.driver.find_element(*self.brand_locators.BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE).send_keys(new_branch_name)
        time.sleep(0.5)
        return self

    def verify_branch_name_updated_in_branch_brand_info_page(self, branch_name):
        time.sleep(1)
        branch_name_locator = self.brand_locators.BRANCH_NAME_VALUE_IN_BRANCH_SETTINGS_PAGE(branch_name)
        print(branch_name_locator)
        self.driver.find_element(*branch_name_locator).is_displayed()
        return self

    def tap_branch_description_in_branch_information_page(self):
        self.driver.find_element(*self.brand_locators.BRANCH_DESCRIPTION_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        return self

    def enter_new_branch_description_in_description_dialog(self, new_branch_description):
        self.driver.find_element(*self.brand_locators.TEXT_IN_BRANCH_DESCRIPTION_DIALOG).clear()
        time.sleep(0.5)
        # Enter new branch name
        self.driver.find_element(*self.brand_locators.TEXT_IN_BRANCH_DESCRIPTION_DIALOG).send_keys(new_branch_description)
        time.sleep(0.5)

    def tap_confirm_button_in_description_dialog(self):
        self.driver.find_element(*self.brand_locators.CONFIRM_BUTTON_IN_BRANCH_DESCRIPTION_DIALOG).click()
        time.sleep(0.5)
        return self

    def verify_branch_description_updated(self, branch_description):
        description_locator = self.brand_locators.BRANCH_DESCRIPTION_VALUE_IN_BRANCH_BRAND_INFO_PAGE(branch_description)
        self.driver.find_element(*description_locator).is_displayed()
        return self

    def tap_branch_phone_toggle(self):
        try:
            self.driver.find_element(*self.brand_locators.BRANCH_PHONE_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE).click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Failed to tap Branch Phone Toggle: {e}")
            return False

    def is_branch_phone_toggle_off(self):
        try:
            # Check if the phone section exists and is displayed
            phone_section = self.driver.find_element(*self.brand_locators.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            if not phone_section.is_displayed():
                print("Branch Phone Info Section is not displayed, no action taken")
                return True
            # Since section exists, check for the toggle
            toggle = self.driver.find_element(*self.brand_locators.BRANCH_PHONE_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE)
            toggle.click()
            time.sleep(0.5)
            return True
        except NoSuchElementException:
            print("Branch Phone Info Section not found, no action taken")
            return True
        except Exception as e:
            print(f"Failed to tap Branch Phone Toggle: {e}")
            return False

    def verify_branch_phone_turn_on(self):
        try:
            section_element = self.driver.find_element(*self.brand_locators.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            return section_element.is_displayed()
        except NoSuchElementException:
            return False

    def is_branch_phone_toggle_on(self):
        """Check if branch phone toggle is on; turn it on if section is not visible."""
        try:
            try:
                section_element = self.driver.find_element(*self.brand_locators.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
                section_exists = section_element.is_displayed()
            except NoSuchElementException:
                section_exists = False
            toggle = self.driver.find_element(*self.brand_locators.BRANCH_PHONE_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE)
            if not section_exists:
                toggle.click()
                time.sleep(0.5)
                return True
            return True
        except NoSuchElementException:
            print("Branch Phone Toggle not found")
            return False
        except Exception as e:
            print(f"Error checking branch phone toggle: {e}")
            return False

    def verify_branch_phone_turn_off(self):
        try:
            section_element = self.driver.find_element(*self.brand_locators.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            return not section_element.is_displayed()
        except NoSuchElementException:
            return True

    def select_branch_phone_county_code(self):
        try:
            self.common_use.select_random_country_code()
            self.common_use.search_country_code()
            self.common_use.is_country_code_changed()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Failed to tap Branch Phone County Code: {e}")
            return False

    def select_branch_phone_county_code_tw(self):
        """
        Click country code selector, search for '台' and select Taiwan (+886)
        """
        # Click on country code dropdown
        self.driver.find_element(*self.brand_locators.BRANCH_PHONE_COUNTY_CODE_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        # Find search field and enter '台'
        search_field = self.driver.find_element(*self.brand_locators.SEARCH_COUNTRY_CODE_IN_BRANCH_PHONE_COUNTY_CODE_DIALOG)
        search_field.clear()
        search_field.send_keys("台灣")
        time.sleep(0.5)
        # Select Taiwan from search results
        taiwan_option = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'台灣') and contains(@text,'+886')]")
        self.driver.find_element(*taiwan_option).click()
        tap_confirm_button = self.driver.find_element(*self.brand_locators.CONFIRM_BUTTON_IN_BRANCH_PHONE_COUNTY_CODE_DIALOG)
        tap_confirm_button.click()
        time.sleep(0.5)
        return self

    def enter_new_branch_phone_number(self, branch_phone_number):
        self.driver.find_element(*self.brand_locators.BRANCH_PHONE_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE).clear()
        time.sleep(0.5)
        # Enter new branch phone number
        self.driver.find_element(*self.brand_locators.BRANCH_PHONE_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE).send_keys(branch_phone_number)
        time.sleep(0.5)
        return self

    def tap_branch_address_toggle(self):
        try:
            self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE).click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Failed to tap Branch Address Toggle: {e}")
            return False

    def is_branch_address_toggle_off(self):
        try:
            # Check if the address section exists and is displayed
            address_section = self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            if not address_section.is_displayed():
                print("Branch Address Info Section is not displayed, no action taken")
                return True
            # Since section exists, check for the toggle
            toggle = self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE)
            toggle.click()
            time.sleep(0.5)
            return True
        except NoSuchElementException:
            print("Branch Address Info Section not found, no action taken")
            return True
        except Exception as e:
            print(f"Failed to tap Branch Address Toggle: {e}")
            return False

    def verify_branch_address_turn_on(self):
        try:
            section_element = self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            return section_element.is_displayed()
        except NoSuchElementException:
            return False

    def is_branch_address_toggle_on(self):
        """Check if branch address toggle is on; turn it on if section is not visible."""
        try:
            try:
                section_element = self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
                section_exists = section_element.is_displayed()
            except NoSuchElementException:
                section_exists = False
            toggle = self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE)
            if not section_exists:
                toggle.click()
                time.sleep(0.5)
                return True
            return True
        except NoSuchElementException:
            print("Branch Address Toggle not found")
            return False
        except Exception as e:
            print(f"Error checking branch address toggle: {e}")
            return False

    def verify_branch_address_turn_off(self):
        try:
            section_element = self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            return not section_element.is_displayed()
        except NoSuchElementException:
            return True

    def tap_branch_address_city_in_branch_brand_info_page(self):
        self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_CITY_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        return self

    def scroll_city_dialog(self):
        scrollable_element = self.brand_locators.BRANCH_ADDRESS_CITY_IN_DIALOG
        self._scroll_element_down(scrollable_element)
        self._scroll_element_up(scrollable_element)
        time.sleep(1)

    def select_random_city(self):
        # Generate random number between 1-22 (avoid 0 index)
        random_num = random.randint(0, 22)

        if random_num >= 15:
            self._scroll_element_down(self.brand_locators.BRANCH_ADDRESS_CITY_IN_DIALOG)
            random_num -= 7
        # Call the method on your locators instance
        locator = self.brand_locators.BRANCH_ADDRESS_CITY_OPTION_IN_DIALOG(random_num)

        # Then use it
        self.driver.find_element(*locator).click()
        time.sleep(1)
        # Additional code...
        return self

    def _scroll_element_down(self, element_locator, scroll_count=1):
        """
        Performs downward scroll(s) within the specified element (finger swipes from bottom to top)

        Args:
            element_locator: Element locator, in the format of tuple(location strategy, location value)
            scroll_count: Number of downward scrolls to perform (default: 1)

        Returns:
            self: Supports method chaining
        """
        try:
            # Locate the element
            element = self.driver.find_element(*element_locator)

            # Get element dimensions
            rect = element.rect
            center_x = rect['x'] + rect['width'] / 2

            # Define scroll positions
            top_y = rect['y'] + (rect['height'] * 0.2)
            bottom_y = rect['y'] + (rect['height'] * 0.8)

            # Perform the specified number of downward scrolls
            for i in range(scroll_count):
                print(f"Scrolling element downward ({i + 1}/{scroll_count})")
                # Scroll down (finger swipes from bottom to top)
                self.driver.swipe(center_x, bottom_y, center_x, top_y, 200)
                time.sleep(0.3)

            return self

        except Exception as e:
            print(f"Element downward scrolling failed: {e}")
            return self

    def _scroll_element_up(self, element_locator, scroll_count=1):
        """
        Performs upward scroll(s) within the specified element (finger swipes from top to bottom)

        Args:
            element_locator: Element locator, in the format of tuple(location strategy, location value)
            scroll_count: Number of upward scrolls to perform (default: 1)

        Returns:
            self: Supports method chaining
        """
        try:
            # Locate the element
            element = self.driver.find_element(*element_locator)

            # Get element dimensions
            rect = element.rect
            center_x = rect['x'] + rect['width'] / 2

            # Define scroll positions
            top_y = rect['y'] + (rect['height'] * 0.2)
            bottom_y = rect['y'] + (rect['height'] * 0.8)

            # Perform the specified number of upward scrolls
            for i in range(scroll_count):
                print(f"Scrolling element upward ({i + 1}/{scroll_count})")
                # Scroll up (finger swipes from top to bottom)
                self.driver.swipe(center_x, top_y, center_x, bottom_y, 200)
                time.sleep(0.3)

            return self

        except Exception as e:
            print(f"Element upward scrolling failed: {e}")
            return self

    def tap_branch_address_district_in_branch_brand_info_page(self):
        self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_DISTRICT_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_DISTRICT_IN_DIALOG).is_displayed()
        return self

    def scroll_district_dialog(self):
        scrollable_element = self.brand_locators.BRANCH_ADDRESS_DISTRICT_IN_DIALOG
        self._scroll_element_down(scrollable_element)
        self._scroll_element_up(scrollable_element)
        time.sleep(1)

    def select_random_district(self):
        # Generate random number between 0-2
        random_num = random.randint(0, 1)
        print(f"Random number for district selection: {random_num}")
        # Use the class-level property with the random index
        district_option = self.brand_locators.BRANCH_ADDRESS_DISTRICT_OPTION_IN_DIALOG(random_num)
        # Click on the selected district option
        self.driver.find_element(*district_option).click()
        time.sleep(1)
        return self

    def enter_new_branch_address(self, branch_address):
        self._scroll_to_element(self.brand_locators.BRANCH_ADDRESS_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE).clear()
        time.sleep(0.5)
        # Enter new branch address
        self.driver.find_element(*self.brand_locators.BRANCH_ADDRESS_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE).send_keys(branch_address)
        time.sleep(0.5)
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

    def tap_expand_brand_settings_button(self):
        self._scroll_to_element(self.brand_locators.EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.driver.find_element(*self.brand_locators.EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        close_button = self.driver.find_element(*self.brand_locators.CLOSE_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        close_button.is_displayed()
        return self

    def verify_brand_settings_section_expanded(self):
        self._scroll_to_element(self.brand_locators.BRAND_IMAGE_IN_BRANCH_BRAND_INFO_PAGE)
        self.driver.find_element(*self.brand_locators.BRAND_IMAGE_IN_BRANCH_BRAND_INFO_PAGE).is_displayed()
        self._scroll_to_element(self.brand_locators.BRAND_NAME_IN_BRANCH_BRAND_INFO_PAGE)
        self.driver.find_element(*self.brand_locators.BRAND_NAME_IN_BRANCH_BRAND_INFO_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.BRAND_DESCRIPTION_IN_BRANCH_BRAND_INFO_PAGE).is_displayed()
        return self

    def verify_pro_business_plan(self):
        # Check for the Pro Business Plan element
        pro_business_plan_element = self.driver.find_element(*self.brand_locators.BRANCH_SUBSCRIPTION_PLAN_IS_PRO_BUSINESS_PLAN_IN_BRANCH_SETTINGS_PAGE)
        return pro_business_plan_element.is_displayed()

    def tap_branch_purchase_plan(self):
        self.driver.find_element(*self.brand_locators.BRANCH_SUBSCRIPTION_IN_BRANCH_SETTINGS_PAGE).click()
        time.sleep(1)
        return self

    def verify_plan_management_page(self):
        # Check for the Plan Management page element
        self.driver.find_element(*self.brand_locators.PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.HOTCOIN_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CREDIT_CARD_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.INVOICE_INFO_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CURRENT_PLAN_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.NEXT_PLAN_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.NEXT_DEDUCTION_DATE_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.VIEW_NEXT_PLAN_DETAILS_BUTTON_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.PLAN_CHANGE_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.DEDUCTION_RECORD_IN_PLAN_MANAGEMENT_PAGE).is_displayed()
        return self

    def tap_view_next_plan_details_button(self):
        self.driver.find_element(*self.brand_locators.VIEW_NEXT_PLAN_DETAILS_BUTTON_IN_PLAN_MANAGEMENT_PAGE).click()
        time.sleep(1)
        return self

    def verify_payment_details_dialog(self):
        # Check for the Payment Details dialog element
        self.driver.find_element(*self.brand_locators.PAYMENT_DETAILS_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.SUBSCRIPTION_PLAN_IN_PAYMENT_DETAILS_DIALOG('Pro商務方案*20位服務人員')).is_displayed()
        self.driver.find_element(*self.brand_locators.DISCOUNT_IN_PAYMENT_DETAILS_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.SMS_COST_IN_PAYMENT_DETAILS_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.TOTAL_COST_IN_PAYMENT_DETAILS_DIALOG).is_displayed()
        return self

    def tap_close_button_in_payment_details_dialog(self):
        self.driver.find_element(*self.brand_locators.CLOSE_BUTTON_IN_PAYMENT_DETAILS_DIALOG).click()
        time.sleep(1)
        return self

    def verify_payment_details_dialog_dismissed(self):
        try:
            # Check for the Payment Details dialog element
            self.driver.find_element(*self.brand_locators.PAYMENT_DETAILS_DIALOG)
            return False  # Dialog is still displayed
        except NoSuchElementException:
            return True

    def tap_plan_change_button(self):
        self.driver.find_element(*self.brand_locators.PLAN_CHANGE_IN_PLAN_MANAGEMENT_PAGE).click()
        time.sleep(1)
        return self

    def verify_plan_change_page(self):
        # Check for the Plan Change page element
        self.driver.find_element(*self.brand_locators.PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.PLAN_CHANGE_DESCRIPTION_IN_PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.PRO_BUSINESS_PLAN_TITLE_IN_PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.PRO_BUSINESS_PLAN_DESCRIPTION_IN_PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.PRO_BUSINESS_PLAN_BUTTON_IN_PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.STAR_NEW_PLAN_TITLE_IN_PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.STAR_NEW_PLAN_DESCRIPTION_IN_PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.STAR_NEW_PLAN_BUTTON_IN_PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.SMS_COST_DESCRIPTION_IN_PLAN_CHANGE_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.DOWN_GRADE_TO_FREE_TRIAL_PLAN_IN_PLAN_CHANGE_PAGE).is_displayed()
        return self

    def tap_pro_business_plan_button(self):
        self.driver.find_element(*self.brand_locators.PRO_BUSINESS_PLAN_BUTTON_IN_PLAN_CHANGE_PAGE).click()
        time.sleep(1)
        return self

    def verify_pro_business_plan_page(self):
        # Check for the Pro Business Plan page element
        self.driver.find_element(*self.brand_locators.DESCRIPTION_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.PRICE_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_1_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_2_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_3_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_4_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_5_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_6_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_7_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_8_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.TOLL_REMINDER_TEXT_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.DIFFERENT_PLAN_BUTTON_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.SELECT_THIS_PLAN_BUTTON_IN_PRO_BUSINESS_PLAN_PAGE).is_displayed()
        return self

    def verify_pro_business_plan_button_disabled(self):
        # Check for the Pro Business Plan button element
        pro_business_plan_button = self.driver.find_element(*self.brand_locators.SELECT_THIS_PLAN_BUTTON_IN_PRO_BUSINESS_PLAN_PAGE)
        return not pro_business_plan_button.is_enabled()

    def tap_different_plan_button(self):
        self.driver.find_element(*self.brand_locators.DIFFERENT_PLAN_BUTTON_IN_PRO_BUSINESS_PLAN_PAGE).click()
        time.sleep(1)
        return self

    def verify_pro_business_plan_content_in_plan_functionality_dialog(self):
        # Check for the Pro Business Plan content in the Plan Functionality dialog
        self.driver.find_element(*self.brand_locators.PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.PRO_BUSINESS_PLAN_TAB_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.STAR_NEW_PLAN_TAB_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FREE_TRIAL_TAB_PLAN_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.DESCRIPTION_IN_PRO_BUSINESS_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.PRICE_DETAILS_TEXT_1_IN_PRO_BUSINESS_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.PRICE_DETAILS_TEXT_2_IN_PRO_BUSINESS_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_1_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_2_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_3_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_4_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_5_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_6_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_7_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_8_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        return self

    def tap_star_new_tab(self):
        self.driver.find_element(*self.brand_locators.STAR_NEW_PLAN_TAB_IN_PLAN_FUNCTION_DIALOG).click()
        time.sleep(1)
        return self

    def verify_start_new_plan_content_in_plan_functionality_dialog(self):
        # Check for the Star New Plan content in the Plan Functionality dialog
        self.driver.find_element(*self.brand_locators.STAR_NEW_PLAN_TAB_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.DESCRIPTION_IN_START_NEW_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.PRICE_DETAILS_TEXT_1_IN_START_NEW_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.PRICE_DETAILS_TEXT_2_IN_START_NEW_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_1_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_2_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_3_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_4_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_5_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_6_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_7_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_8_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        return self

    def tap_free_plan_tab(self):
        self.driver.find_element(*self.brand_locators.FREE_TRIAL_TAB_PLAN_IN_PLAN_FUNCTION_DIALOG).click()
        time.sleep(1)
        return self

    def verify_free_plan_content_in_plan_functionality_dialog(self):
        # Check for the Free Trial Plan content in the Plan Functionality dialog
        self.driver.find_element(*self.brand_locators.FREE_TRIAL_TAB_PLAN_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.DESCRIPTION_IN_FREE_TRIAL_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.PRICE_DETAILS_TEXT_1_IN_FREE_TRIAL_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.PRICE_DETAILS_TEXT_2_IN_FREE_TRIAL_PLAN_TAB).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_1_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_2_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_3_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_4_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_5_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_6_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_7_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.FEATURE_TEXT_8_IN_PLAN_FUNCTION_DIALOG).is_displayed()
        return self

    def tap_close_plan_functionality_dialog_button(self):
        self.driver.find_element(*self.brand_locators.CLOSE_BUTTON_IN_PLAN_FUNCTION_DIALOG).click()
        time.sleep(1)
        return self

    def verify_plan_functionality_dialog_dismissed(self):
        try:
            # Check for the Plan Functionality dialog element
            self.driver.find_element(*self.brand_locators.PLAN_FUNCTION_DIALOG)
            return False  # Dialog is still displayed
        except NoSuchElementException:
            return True

    def tap_close_button_in_pro_business_plan_page(self):
        self.driver.find_element(*self.brand_locators.CLOSE_BUTTON_IN_PRO_BUSINESS_PLAN_PAGE).click()
        time.sleep(1)
        return self

    def tap_start_new_plan_button(self):
        self.driver.find_element(*self.brand_locators.STAR_NEW_PLAN_BUTTON_IN_PLAN_CHANGE_PAGE).click()
        time.sleep(1)
        return self

    def verify_start_new_plan_page(self):
        # Check for the Start New Plan page element
        self.driver.find_element(*self.brand_locators.DESCRIPTION_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.PRICE_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_1_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_2_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_3_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_4_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_5_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_6_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_7_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.CONTENT_8_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.TOLL_REMINDER_TEXT_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.DIFFERENT_PLAN_BUTTON_IN_START_NEW_PLAN_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.SELECT_THIS_PLAN_BUTTON_IN_START_NEW_PLAN_PAGE).is_displayed()
        return self

    def verify_start_new_plan_button_enabled(self):
        # Check for the Start New Plan button element
        start_new_plan_button = self.driver.find_element(*self.brand_locators.SELECT_THIS_PLAN_BUTTON_IN_START_NEW_PLAN_PAGE)
        return start_new_plan_button.is_enabled()

    def tap_pro_business_plan_tab(self):
        self.driver.find_element(*self.brand_locators.PRO_BUSINESS_PLAN_TAB_IN_PLAN_FUNCTION_DIALOG).click()
        time.sleep(1)
        return self

    def tap_close_button_in_start_new_plan_page(self):
        self.driver.find_element(*self.brand_locators.CLOSE_BUTTON_IN_START_NEW_PLAN_PAGE).click()
        time.sleep(1)
        return self

    def tap_downgrade_to_free_trial_plan(self):
        self.driver.find_element(*self.brand_locators.DOWN_GRADE_TO_FREE_TRIAL_PLAN_IN_PLAN_CHANGE_PAGE).click()
        time.sleep(2)
        return self

    def verify_cancel_payment_plan_dialog(self):
        # Check for the Cancel Payment Plan dialog element
        self.driver.find_element(*self.brand_locators.TITLE_IN_CANCEL_PAYMENT_PLAN_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.CONFIRM_BUTTON_IN_CANCEL_PAYMENT_PLAN_DIALOG).is_displayed()
        self.driver.find_element(*self.brand_locators.CANCEL_BUTTON_IN_CANCEL_PAYMENT_PLAN_DIALOG).is_displayed()
        return self

    def tap_cancel_button_in_cancel_payment_plan_dialog(self):
        self.driver.find_element(*self.brand_locators.CANCEL_BUTTON_IN_CANCEL_PAYMENT_PLAN_DIALOG).click()
        time.sleep(1)
        return self

    def verify_cancel_payment_plan_dialog_dismissed(self):
        try:
            # Check for the Cancel Payment Plan dialog element
            self.driver.find_element(*self.brand_locators.TITLE_IN_CANCEL_PAYMENT_PLAN_DIALOG)
            return False  # Dialog is still displayed
        except NoSuchElementException:
            return True

    def tap_close_button_in_plan_change_page(self):
        self.driver.find_element(*self.brand_locators.CLOSE_BUTTON_IN_PLAN_CHANGE_PAGE).click()
        time.sleep(1)
        return self

    def tap_payment_records_section(self):
        self.driver.find_element(*self.brand_locators.DEDUCTION_RECORD_IN_PLAN_MANAGEMENT_PAGE).click()
        time.sleep(3)
        return self

    def verify_payment_records_page(self):
        # Check for the Payment Records page element
        self.driver.find_element(*self.brand_locators.TITLE_IN_PAYMENT_RECORD_PAGE).is_displayed()
        self.driver.find_element(*self.brand_locators.ClOSE_BUTTON_IN_PAYMENT_RECORD_PAGE).is_displayed()
        return self

    def tap_close_button_in_payment_records_page(self):
        self.driver.find_element(*self.brand_locators.ClOSE_BUTTON_IN_PAYMENT_RECORD_PAGE).click()
        time.sleep(1)
        return self

    def tap_back_hotcake_app_button(self):
        self.driver.find_element(*self.brand_locators.BACK_HOTCAKE_APP_BUTTON).click()
        time.sleep(1)
        return self