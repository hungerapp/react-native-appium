import time
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from pages.shared_components.common_use import CommonUseSection


class BrandPage:
    def __init__(self, driver):
        self.common_use = CommonUseSection(driver)
        self.driver = driver
        self.SETTINGS_OPTION_IN_NAVIGATION = (AppiumBy.ACCESSIBILITY_ID, '設定')

        self.BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, '//*[@text="分店設定"]')
        self.BRANCH_NAME_IN_BRANCH_SETTINGS_PAGE = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='chevron-right'])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView")
        self.BRANCH_NAME_VALUE_IN_BRANCH_SETTINGS_PAGE = lambda text: (AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")

        self.BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店和品牌資訊"]')
        self.CONFIRM_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.ACCESSIBILITY_ID, 'check')
        self.BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
        self.BRANCH_NAME_VALUE_IN_BRANCH_BRAND_INFO_PAGE = lambda text: (AppiumBy.XPATH, f"//android.widget.EditText[@text='{text}']")
        self.BRANCH_DESCRIPTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店介紹"]/../android.view.ViewGroup')
        self.BRANCH_DESCRIPTION_VALUE_IN_BRANCH_BRAND_INFO_PAGE = lambda text: (AppiumBy.XPATH, f"//android.widget.TextView[@text='{text}']")
        self.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="分店電話"]')
        self.BRANCH_PHONE_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="顯示分店電話-switch-button"]')
        self.BRANCH_PHONE_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="分店電話"]/../android.widget.EditText')
        self.BRANCH_PHONE_COUNTY_CODE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="caret-down"]')
        self.BRANCH_ADDRESS_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="顯示分店地址-switch-button"]')
        self.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="國家"]')
        self.BRANCH_ADDRESS_CITY_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="城市"]/../android.view.ViewGroup')
        self.BRANCH_ADDRESS_DISTRICT_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="地區"]/../android.view.ViewGroup')
        self.BRANCH_ADDRESS_DISTRICT_WARM_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text=" 此欄位為必填。"]')
        self.BRANCH_ADDRESS_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@text="地址"]/../android.widget.EditText')
        self.EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@content-desc="展開品牌設定"]')
        self.CLOSE_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@content-desc="收起品牌設定"]')
        self.BRAND_SETTINGS_SECTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="android:id/parentPanel"]')
        self.BRAND_IMAGE_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//*[@resource-id="com.hunger.hotcakeapp.staging:id/action_bar_root"]//android.widget.ImageView')
        self.BRAND_NAME_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="品牌名稱"]')
        self.BRAND_DESCRIPTION_IN_BRANCH_BRAND_INFO_PAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="品牌介紹"]')

        self.TEXT_IN_BRANCH_DESCRIPTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="modal-surface"]//android.widget.EditText')
        self.CONFIRM_BUTTON_IN_BRANCH_DESCRIPTION_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="circle-check"]//com.horcrux.svg.GroupView')

        self.SEARCH_COUNTRY_CODE_IN_BRANCH_PHONE_COUNTY_CODE_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="magnifying-glass"]/../android.view.ViewGroup//android.widget.EditText')
        self.CONFIRM_BUTTON_IN_BRANCH_PHONE_COUNTY_CODE_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="國碼-modal-right-button "]')

        self.BRANCH_ADDRESS_CITY_IN_DIALOG = (AppiumBy.XPATH, '//*[@text="城市"]/../android.view.ViewGroup//android.widget.ScrollView')
        self.BRANCH_ADDRESS_CITY_OPTION_IN_DIALOG = lambda index: (AppiumBy.XPATH, f'//*[@text="城市"]/../android.view.ViewGroup//android.widget.ScrollView//android.view.ViewGroup//android.view.ViewGroup[{index}]')

        self.BRANCH_ADDRESS_DISTRICT_IN_DIALOG = (AppiumBy.XPATH, '//*[@resource-id="地區-close-button"]/../android.view.ViewGroup//android.widget.ScrollView')
        self.BRANCH_ADDRESS_DISTRICT_OPTION_IN_DIALOG = lambda index: (AppiumBy.XPATH, f'//*[@resource-id="地區-close-button"]/../android.view.ViewGroup//android.widget.ScrollView//android.view.ViewGroup//android.view.ViewGroup[{index}]//*[@resource-id="circle"]')






    def tap_settings_option(self):
        self.driver.find_element(*self.SETTINGS_OPTION_IN_NAVIGATION).click()
        time.sleep(0.5)
        return self

    def verify_branch_settings_page(self):
        time.sleep(1)
        try:
            # Check for the Branch Settings page element
            branch_settings_element = self.driver.find_element(*self.BRANCH_SETTINGS_PAGE)
            return branch_settings_element.is_displayed()
        except NoSuchElementException:
            print("Branch Settings page not found")
            return False
        except Exception as e:
            print(f"Error verifying Branch Settings page: {e}")
            return False

    def tap_branch_name_in_branch_setting_page(self):
        self.driver.find_element(*self.BRANCH_NAME_IN_BRANCH_SETTINGS_PAGE).click()
        time.sleep(0.5)
        return self

    def verify_branch_branch_info_page(self):
        time.sleep(1)
        try:
            # Check for the Branch Name element which should be visible on the Branch Settings page
            branch_name_element = self.driver.find_element(*self.BRANCH_BRAND_INFO_PAGE)
            return branch_name_element.is_displayed()
        except NoSuchElementException:
            print("Branch Name element not found")
            return False
        except Exception as e:
            print(f"Error verifying Branch Name in Branch Settings page: {e}")
            return False

    def tap_confirm_edit_button_in_branch_brand_info_page(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        return self

    def verify_return_to_branch_settings_page(self):
        time.sleep(1)
        try:
            # Check for the Branch Name element which should be visible on the Branch Settings page
            branch_name_element = self.driver.find_element(*self.BRANCH_NAME_IN_BRANCH_SETTINGS_PAGE)
            return branch_name_element.is_displayed()
        except Exception as e:
            print(f"Failed to verify return to Branch Settings page: {e}")
            return False

    def enter_new_branch_name_in_branch_brand_info_page(self, new_branch_name):
        self.driver.find_element(*self.BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE).clear()
        time.sleep(0.5)
        # Enter new branch name
        self.driver.find_element(*self.BRANCH_NAME_FIELD_IN_BRANCH_BRAND_INFO_PAGE).send_keys(new_branch_name)
        time.sleep(0.5)
        return self

    def verify_branch_name_updated_in_branch_brand_info_page(self, branch_name):
        time.sleep(1)
        try:
            # Generate the locator dynamically with the expected text
            branch_name_locator = self.BRANCH_NAME_VALUE_IN_BRANCH_BRAND_INFO_PAGE(branch_name)
            branch_name_element = self.driver.find_element(*branch_name_locator)
            return branch_name_element.is_displayed()
        except Exception as e:
            print(f"Error verifying branch name update: {e}")
            return False

    def verify_branch_name_updated_in_branch_setting_page(self, expected_name):
        time.sleep(1)
        try:
            # Generate the locator dynamically with the expected text
            branch_name_locator = self.BRANCH_NAME_VALUE_IN_BRANCH_SETTINGS_PAGE(expected_name)
            branch_name_element = self.driver.find_element(*branch_name_locator)
            return branch_name_element.is_displayed()
        except Exception as e:
            print(f"Error verifying branch name update: {e}")
            return False

    def tap_branch_description_in_branch_information_page(self):
        self.driver.find_element(*self.BRANCH_DESCRIPTION_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        return self

    def enter_new_branch_description_in_description_dialog(self, new_branch_description):
        self.driver.find_element(*self.TEXT_IN_BRANCH_DESCRIPTION_DIALOG).clear()
        time.sleep(0.5)
        # Enter new branch name
        self.driver.find_element(*self.TEXT_IN_BRANCH_DESCRIPTION_DIALOG).send_keys(new_branch_description)
        time.sleep(0.5)

    def tap_confirm_button_in_description_dialog(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_IN_BRANCH_DESCRIPTION_DIALOG).click()
        time.sleep(0.5)
        return self

    def verify_branch_description_updated(self, branch_description):
        time.sleep(1)
        try:
            # Generate the locator dynamically with the expected text
            description_locator = self.BRANCH_DESCRIPTION_VALUE_IN_BRANCH_BRAND_INFO_PAGE(branch_description)
            description_element = self.driver.find_element(*description_locator)
            return description_element.is_displayed()
        except Exception as e:
            print(f"Error verifying branch description update: {e}")
            return False

    def tap_branch_phone_toggle(self):
        try:
            self.driver.find_element(*self.BRANCH_PHONE_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE).click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Failed to tap Branch Phone Toggle: {e}")
            return False

    def is_branch_phone_toggle_off(self):
        try:
            # Check if the phone section exists and is displayed
            phone_section = self.driver.find_element(*self.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            if not phone_section.is_displayed():
                print("Branch Phone Info Section is not displayed, no action taken")
                return True
            # Since section exists, check for the toggle
            toggle = self.driver.find_element(*self.BRANCH_PHONE_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE)
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
            section_element = self.driver.find_element(*self.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            return section_element.is_displayed()
        except NoSuchElementException:
            return False

    def is_branch_phone_toggle_on(self):
        """Check if branch phone toggle is on; turn it on if section is not visible."""
        try:
            try:
                section_element = self.driver.find_element(*self.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
                section_exists = section_element.is_displayed()
            except NoSuchElementException:
                section_exists = False
            toggle = self.driver.find_element(*self.BRANCH_PHONE_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE)
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
            section_element = self.driver.find_element(*self.BRANCH_PHONE_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
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
        self.driver.find_element(*self.BRANCH_PHONE_COUNTY_CODE_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        # Find search field and enter '台'
        search_field = self.driver.find_element(*self.SEARCH_COUNTRY_CODE_IN_BRANCH_PHONE_COUNTY_CODE_DIALOG)
        search_field.clear()
        search_field.send_keys("台灣")
        time.sleep(0.5)
        # Select Taiwan from search results
        taiwan_option = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'台灣') and contains(@text,'+886')]")
        self.driver.find_element(*taiwan_option).click()
        tap_confirm_button = self.driver.find_element(*self.CONFIRM_BUTTON_IN_BRANCH_PHONE_COUNTY_CODE_DIALOG)
        tap_confirm_button.click()
        time.sleep(0.5)
        return self

    def enter_new_branch_phone_number(self, branch_phone_number):
        self.driver.find_element(*self.BRANCH_PHONE_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE).clear()
        time.sleep(0.5)
        # Enter new branch phone number
        self.driver.find_element(*self.BRANCH_PHONE_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE).send_keys(branch_phone_number)
        time.sleep(0.5)
        return self

    def tap_branch_address_toggle(self):
        try:
            self.driver.find_element(*self.BRANCH_ADDRESS_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE).click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Failed to tap Branch Address Toggle: {e}")
            return False

    def is_branch_address_toggle_off(self):
        try:
            # Check if the address section exists and is displayed
            address_section = self.driver.find_element(*self.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            if not address_section.is_displayed():
                print("Branch Address Info Section is not displayed, no action taken")
                return True
            # Since section exists, check for the toggle
            toggle = self.driver.find_element(*self.BRANCH_ADDRESS_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE)
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
            section_element = self.driver.find_element(*self.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            return section_element.is_displayed()
        except NoSuchElementException:
            return False

    def is_branch_address_toggle_on(self):
        """Check if branch address toggle is on; turn it on if section is not visible."""
        try:
            try:
                section_element = self.driver.find_element(*self.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
                section_exists = section_element.is_displayed()
            except NoSuchElementException:
                section_exists = False
            toggle = self.driver.find_element(*self.BRANCH_ADDRESS_TOGGLE_IN_BRANCH_BRAND_INFO_PAGE)
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
            section_element = self.driver.find_element(*self.BRANCH_ADDRESS_INFO_SECTION_IN_BRANCH_BRAND_INFO_PAGE)
            return not section_element.is_displayed()
        except NoSuchElementException:
            return True

    def tap_branch_address_city_in_branch_brand_info_page(self):
        self.driver.find_element(*self.BRANCH_ADDRESS_CITY_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        return self

    def scroll_city_dialog(self):
        scrollable_element = self.BRANCH_ADDRESS_CITY_IN_DIALOG
        self._scroll_element_down(scrollable_element)
        self._scroll_element_up(scrollable_element)
        time.sleep(1)

    def select_random_city(self):
        """
        Randomly selects a city option from the city dialog and checks for district warning.
        For options 1-14, selects directly.
        For options 15-22, scrolls to bottom first and selects with adjusted index (n-7).

        Returns:
            self: Supports method chaining
        """
        try:
            # Generate random number between 0-22
            random_num = random.randint(0, 22)

            if random_num == 0:
                # Skip selection if 0
                return self

            if random_num >= 15:
                # For numbers 15-22, scroll to bottom first
                self._scroll_element_down(self.BRANCH_ADDRESS_CITY_IN_DIALOG)

                # Adjust the index (subtract 7)
                adjusted_index = random_num - 7
                city_option = self.BRANCH_ADDRESS_CITY_OPTION_IN_DIALOG(adjusted_index)
            else:
                # For numbers 1-14, use directly
                city_option = self.BRANCH_ADDRESS_CITY_OPTION_IN_DIALOG(random_num)

            # Click on the selected city option
            self.driver.find_element(*city_option).click()
            time.sleep(1)

            # Check if district warning is displayed
            try:
                warning = self.driver.find_element(*self.BRANCH_ADDRESS_DISTRICT_WARM_IN_BRANCH_BRAND_INFO_PAGE)
                if warning.is_displayed():
                    print("District field warning displayed: This field is required")
            except NoSuchElementException:
                print("District warning not displayed")
            except Exception as e:
                print(f"Error checking district warning: {e}")

            return self

        except Exception as e:
            print(f"Failed to select random city: {e}")
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
        self.driver.find_element(*self.BRANCH_ADDRESS_DISTRICT_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        return self

    def scroll_district_dialog(self):
        scrollable_element = self.BRANCH_ADDRESS_DISTRICT_IN_DIALOG
        self._scroll_element_down(scrollable_element)
        self._scroll_element_up(scrollable_element)
        time.sleep(1)

    def select_random_district(self):
        """
        Randomly selects a district option from the district dialog.

        Returns:
            self: Supports method chaining
        """
        try:
            # Generate random number between 1-2
            random_num = random.randint(0, 2)

            # Use the class-level property with the random index
            district_option = self.BRANCH_ADDRESS_DISTRICT_OPTION_IN_DIALOG(random_num)

            # Click on the selected district option
            self.driver.find_element(*district_option).click()
            time.sleep(1)
            return self

        except Exception as e:
            print(f"Failed to select random district: {e}")
            return self

    def enter_new_branch_address(self, branch_address):
        self._scroll_to_element(self.BRANCH_ADDRESS_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE)
        self.driver.find_element(*self.BRANCH_ADDRESS_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE).clear()
        time.sleep(0.5)
        # Enter new branch address
        self.driver.find_element(*self.BRANCH_ADDRESS_TEXT_FIELD_IN_BRANCH_BRAND_INFO_PAGE).send_keys(branch_address)
        time.sleep(0.5)
        return self

    def _scroll_to_element(self, element_locator, max_swipes=3, timeout=3):
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
        self._scroll_to_element(self.EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        self.driver.find_element(*self.EXPAND_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE).click()
        time.sleep(0.5)
        close_button = self.driver.find_element(*self.CLOSE_BRAND_SETTINGS_BUTTON_IN_BRANCH_BRAND_INFO_PAGE)
        close_button.is_displayed()
        return self

    def verify_brand_settings_section_expanded(self):
        self._scroll_to_element(self.BRAND_IMAGE_IN_BRANCH_BRAND_INFO_PAGE)
        self.driver.find_element(*self.BRAND_IMAGE_IN_BRANCH_BRAND_INFO_PAGE).is_displayed()
        self._scroll_to_element(self.BRAND_NAME_IN_BRANCH_BRAND_INFO_PAGE)
        self.driver.find_element(*self.BRAND_NAME_IN_BRANCH_BRAND_INFO_PAGE).is_displayed()
        self.driver.find_element(*self.BRAND_DESCRIPTION_IN_BRANCH_BRAND_INFO_PAGE).is_displayed()
        return self

