import time
import random
import string
import warnings

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from datetime import datetime, timedelta
from appium.webdriver.common.appiumby import AppiumBy

from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.personal_page.personal_page_locators import PersonalPageLocators

class PersonalPage(CommonUseSection):
  
  def __init__(self, driver):
    self.driver = driver
    self.personal_page_locators = PersonalPageLocators()
    
    
    # Get window size
    window_size = self.driver.get_window_size()
    # Calculate center coordinates
    self.center_x = window_size['width'] // 2
    self.center_y = window_size['height'] // 2
    
  
  
  # Check if Basic elements are displayed
  def is_profile_picture_displayed(self):
    time.sleep(2)
    assert self.driver.find_element(*self.personal_page_locators.PROFILE_PICTURE).is_displayed()
  
  def is_username_displayed(self):
    assert self.driver.find_element(*self.personal_page_locators.USERNAME).is_displayed()
  
  def get_greeting_message_message(self):
    elements = self.driver.find_elements(*self.personal_page_locators.GREETING_MESSAGE)
    for e in elements:
      text = e.text
      if "早安" in text or "保持好心情" in text or "晚安" in text:
          print("find greeting message", text) 
          return e.text 
    return None
  
  def is_email_address_displayed(self):
    assert self.driver.find_element(*self.personal_page_locators.EMAIL_ADDRESS).is_displayed()
  
  
  
  # Check if Brand list elements are displayed
  def is_brand_list_title_displayed(self):
    assert self.driver.find_element(*self.personal_page_locators.BRAND_LIST_TITLE).is_displayed()
  
  def is_brand_hunger_salon_title_displayed(self):
    assert self.driver.find_element(*self.personal_page_locators.BRAND_HUNGER_SALON_TITLE).is_displayed()
  
  def is_brand_hunger_salon_profile_picture_displayed(self):
    assert self.driver.find_element(*self.personal_page_locators.BRAND_HUNGER_SALON_PROFILE_PICTURE).is_displayed()
  
  
  def _scroll_down(self):
    """Scroll down"""
    try:
        # get screen size
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] * 0.5
        start_y = screen_size['height'] * 0.7
        end_y = screen_size['height'] * 0.3
        
        # execute scroll
        self.driver.swipe(
            start_x, 
            start_y, 
            start_x, 
            end_y, 
            duration=500
        )
    except Exception as e:
        print(f"Scroll down error: {str(e)}")
        raise
  
  #click all branches
  def visit_all_branches_smart(self):
    """Smart visit all branches"""
    results = []
    visited_branches = set()

    
    try:
        for branch_info in self.personal_page_locators.BRANCH_NAMES:
            try:
                element = self.driver.find_element(*branch_info["locator"])
                if element.is_displayed():
                    time.sleep(2)
                    element.click()
                    visited_branches.add(branch_info["name"])
                 
                    # Handle specific branch scenarios
                    if branch_info["name"] == "Free分店":
                        self.driver.find_element(*self.personal_page_locators.POP_UP_CANCEL_ICON).click()
                        self.driver.find_element(*self.personal_page_locators.FREE_WINDOW_BACK_TO_PERSONAL_PAGE_BTN).click()
                    elif branch_info["name"] == "Star分店":
                        self.driver.find_element(*self.personal_page_locators.POP_UP_CANCEL_ICON).click()
                        self.driver.find_element(*self.personal_page_locators.BACK_TO_PERSONAL_PAGE_BTN).click()
                        
                    else:
                        self.driver.find_element(*self.personal_page_locators.POP_UP_CANCEL_ICON).click()
                        self.driver.find_element(*self.personal_page_locators.BACK_TO_PERSONAL_PAGE_BTN).click()

                    
                    results.append({
                        "branch_name": branch_info["name"],
                        "status": "success"
                    })
            except Exception as e:
                print(f"Error clicking branch {branch_info['name']}: {str(e)}")
                results.append({
                    "branch_name": branch_info["name"],
                    "status": "error",
                    "error": str(e)
                })
    
        unvisited_branches = [branch["name"] for branch in self.personal_page_locators.BRANCH_NAMES if branch["name"] not in visited_branches]
        if unvisited_branches:
            print(f"Warning: Could not visit branches: {', '.join(unvisited_branches)}")
        
        # finally click Pro branch
        self.driver.find_element(*self.personal_page_locators.PRO_BRANCH_NAME).click()
        self.driver.find_element(*self.personal_page_locators.POP_UP_CANCEL_ICON).click()
        self.driver.find_element(*self.personal_page_locators.BACK_TO_PERSONAL_PAGE_BTN).click()
            
    except Exception as e:
        print(f"Error in visit_all_branches_smart: {str(e)}")

  def _scroll_to_top(self):
    """Scroll to top"""
    try:
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] * 0.5
        start_y = screen_size['height'] * 0.3
        end_y = screen_size['height'] * 0.7
        
        # scroll to top
        self.driver.swipe(
            start_x, 
            start_y, 
            start_x, 
            end_y, 
            duration=500
        )
    except Exception as e:
        print(f"Scroll to top error: {str(e)}")             
  
  
  # Google Calendar
  def click_google_calendar_button(self):
    self.driver.find_element(*self.personal_page_locators.GOOGLE_CALENDAR_BUTTON).click()
    return self
  
  def integrate_google_calendar(self):
    time.sleep(2)
    self.driver.find_element(*self.personal_page_locators.INTEGRATE_GOOGLE_CALENDAR_BUTTON).click()
    time.sleep(1)
    for _ in range (2):
        self.driver.back()
    return self
  
   
  
  # Push notification
  def click_push_notification_button(self):
    """click push notification button"""
    max_attempts = 3
    attempt = 0
    scroll_direction = "up"  # initial scroll direction is 
    
    while attempt < max_attempts:
        try:
            element = self.driver.find_element(*self.personal_page_locators.PUSH_NOTIFICATION_BUTTON)
            if element.is_displayed():
                element.click()
                return self
        except NoSuchElementException:
            pass
        
        # execute scroll
        try:
            screen_size = self.driver.get_window_size()
            start_x = screen_size['width'] * 0.5
            
            if scroll_direction == "down":
                # scroll down
                start_y = screen_size['height'] * 0.7
                end_y = screen_size['height'] * 0.3
            else:
                # scroll up
                start_y = screen_size['height'] * 0.3
                end_y = screen_size['height'] * 0.7
            
            self.driver.swipe(
                start_x,
                start_y,
                start_x,
                end_y,
                duration=500
            )
            
            time.sleep(1)  
            
            # switch scroll direction after each attempt
            scroll_direction = "down" if scroll_direction == "up" else "up"
            attempt += 1
            
        except Exception as e:
            print(f"Error scrolling to find push notification button: {str(e)}")
            raise
    
    raise NoSuchElementException("After multiple up and down scrolls, still not found push notification button")
  
  
  def random_toggle_switches(self, num_toggles=None):
    """
    random toggle switches
    :param num_toggles: number of switches to toggle
    :return: return toggle results list
    """
    if num_toggles is None:
        num_toggles = random.randint(1, len(self.personal_page_locators.TOGGLE_LOCATORS))
        
    selected_toggles = random.sample(list(self.personal_page_locators.TOGGLE_LOCATORS.items()), num_toggles)
    toggled_results = []
    
    for toggle_name, toggle_locator in selected_toggles:
        try:
            # try to find element
            toggle = self.driver.find_element(*toggle_locator)
            
            # get element location
            location = toggle.location
            size = toggle.size
            
            # calculate element center point
            target_y = location['y'] + (size['height'] / 2)
            
            # get screen size
            screen_size = self.driver.get_window_size()
            start_x = screen_size['width'] * 0.5
            
            # if element is out of screen, scroll to it
            if target_y > screen_size['height']:
                self.driver.swipe(
                    start_x,
                    screen_size['height'] * 0.7,
                    start_x,
                    screen_size['height'] * 0.3,
                    duration=500
                )
                time.sleep(0.5)
            
            # check element and click
            toggle = self.driver.find_element(*toggle_locator)
            if toggle.is_displayed() and toggle.is_enabled():
                original_state = toggle.is_selected()
                toggle.click()
                time.sleep(0.5)
                
                new_state = toggle.is_selected()
                toggled_results.append({
                    "name": toggle_name,
                    "original_state": original_state,
                    "new_state": new_state,
                    "success": original_state != new_state
                })
            else:
                toggled_results.append({
                    "name": toggle_name,
                    "error": "Element not visible or not clickable"
                })
                
        except Exception as e:
            toggled_results.append({
                "name": toggle_name,
                "error": str(e)
            })
    
    # check actual toggle success number
    successful_toggles = len([r for r in toggled_results if "success" in r and r["success"]])
    if successful_toggles < num_toggles:
        print(f"Warning: Requested to toggle {num_toggles} switches, but only {successful_toggles} were successfully toggled")
    
    return toggled_results
     
  def save_notification_settings(self):
        """Click save button"""
        save_button = self.driver.find_element(*self.personal_page_locators.PUSH_NOTTIFICATION_SAVE)
        save_button.click()
        time.sleep(3)
        return self

  def toggle_num(self, num_toggles=None):
        """Toggle and save"""
        results = self.random_toggle_switches(num_toggles)
        return results    
      
  # Manage account settings -> Maybe seperated into different files
  def click_setting_icon(self):
    """Click settings icon and verify settings popup is displayed"""

    # try to find and click settings button
    try:
        time.sleep(1)
        settings_button = self.driver.find_element(*self.personal_page_locators.SETTINGS_BUTTON)
        if settings_button.is_displayed() and settings_button.is_enabled():
            settings_button.click()
                    
        # Verify settings popup
            if self.driver.find_element(*self.personal_page_locators.SETTINGS_POPUP).is_displayed():
                print("Successfully clicked settings button and displayed settings popup")
            return self
    except NoSuchElementException:
      raise NoSuchElementException("Unable to find settings button after multiple attempts")

  def _perform_scroll(self, direction):
    """Helper method to perform scroll"""
    try:
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] * 0.5
        
        if direction == "down":
            start_y = screen_size['height'] * 0.7
            end_y = screen_size['height'] * 0.3
        else:
            start_y = screen_size['height'] * 0.3
            end_y = screen_size['height'] * 0.7
        
        self.driver.swipe(
            start_x,
            start_y,
            start_x,
            end_y,
            duration=500
        )
        time.sleep(1)
    except Exception as e:
        print(f"Error during scroll: {str(e)}")
  
  def click_account_settings(self):
    """Click account settings"""
    self.driver.find_element(*self.personal_page_locators.ACCOUNT_SETTINGS_OPTION).click()
    return self
  
  
  def generate_random_name(self):
    """Generate random name"""
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    return f"Ann{random_suffix}"

  def clear_and_input_name(self):
    try:
        time.sleep(2)  
        
        for locator_strategy, locator_value in self.personal_page_locators.NAME_INPUT:
            try:
                name_field = self.driver.find_element(locator_strategy, locator_value)
                if name_field.is_displayed():
                    print(f"Found name input field, current text: {name_field.text}") 
                    
                    # click input field
                    name_field.click()
                    
                    # clear existing text
                    name_field.clear()
                    
                    # input new text
                    random_name = self.generate_random_name()
                    name_field.send_keys(random_name)
                    
                    print(f"Successfully input new name: {random_name}")
                    return random_name
            except Exception as e:
                print(f"Failed to locate strategy: {str(e)}")
                continue
                
        raise NoSuchElementException("Not found name input field")
        
    except Exception as e:
        print(f"Error inputting name: {str(e)}")
        raise
        
  def get_empty_name_error_message(self):
        """Get empty name error message"""
        for locator_strategy, locator_value in self.personal_page_locators.NAME_INPUT:
            try:
                name_field = self.driver.find_element(locator_strategy, locator_value)
                if name_field.is_displayed():
                    print(f"Found name input field, current text: {name_field.text}")
                    
                    # click input field
                    name_field.click()
                    
                    # clear existing text
                    name_field.clear()
                    
                    error_msg = self.driver.find_element(*self.personal_page_locators.EMPTY_NAME_ERROR_MESSAGE)
                    assert error_msg.text == " 此欄位為必填。", "Empty name error message is not correct"
                    return error_msg.text
                  
            except Exception as e:
                print(f"Failed to locate strategy: {str(e)}")
                continue
                
        raise NoSuchElementException("Not found name input field")

  def _perform_random_swipe(self, start_x, start_y, max_offset=50):
    """執行隨機滑動"""
    try:
        actions = ActionChains(self.driver)
        pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
        
        
        end_x = start_x + random.randint(-max_offset, max_offset)
        end_y = start_y + random.randint(-800, 800)  
        
        actions.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
    except Exception as e:
        print(f"Random swipe error: {str(e)}")
        raise

  def input_phone_number(self, valid=True):
    """Input phone number"""
    try:
        phone_field = self.driver.find_element(*self.personal_page_locators.PHONE_INPUT_INITIAL)
        phone_field.clear()
        
        if valid:
            # Generate a valid phone number
            phone_number = f"{random.randint(900000000, 999999999)}"
        else:
            # Generate an invalid phone number
            phone_number = f"{random.randint(10000, 99999)}"
            
        phone_field_clear = self.driver.find_element(*self.personal_page_locators.PHONE_INPUT_CLEAR)
        phone_field_clear.send_keys(phone_number)
        return phone_number
    except Exception as e:
        print(f"Input phone number error: {str(e)}")
        raise
  def get_empty_phone_error_message(self):
        """Get error message"""

        phone_field = self.driver.find_element(*self.personal_page_locators.PHONE_INPUT_INITIAL)
        phone_field.click()
        phone_field.clear()
        error_element = self.driver.find_element(*self.personal_page_locators.EMPTY_PHONE_ERROR_MESSAGE)
        assert error_element.text == " 此欄位為必填。", "Empty phone error message is not correct"
        return error_element.text
      
  def get_invalid_phone_error_message(self):
        """Get error message"""
        error_element = self.driver.find_element(*self.personal_page_locators.INVALID_PHONE_ERROR_MESSAGE)
        assert error_element.text == " 格式錯誤。", "Invalid phone error message is not correct"
        return error_element.text

  def save_account_settings(self):
        """Save settings"""
        self.driver.find_element(*self.personal_page_locators.SAVE_BUTTON).click()
        return self
      
  def cancel_account_settings (self):
        """Cancel account settings"""
        self.driver.find_element(*self.personal_page_locators.ACCOUNT_SETTINGS_CANCEL_BUTTON).click()
        time.sleep(2)
        return self
  
  def update_account_information_and_save_settings(self):
    
      try:  
            # click birthday field to open date picker
            self.driver.find_element(*self.personal_page_locators.BIRTHDAY_FIELD).click()
            self.swipe_calendar_component()
            
            self.clear_and_input_name()
            self.select_random_gender()
            self.input_phone_number(valid=True)
            self.save_account_settings()
            
      except Exception as e:
            error_msg = f"Update failed: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

  def select_random_country_code(self):
    """Select random country code"""
    try:
        self.driver.find_element(*self.personal_page_locators.COUNTRY_SELECTOR).click()
        time.sleep(1)
        
        self._random_scroll_and_select()
        
        return self.selected_country_code
            
    except Exception as e:
        print(f"Select country code error: {str(e)}")
        raise

  def _random_scroll_and_select(self):
    """Random scroll and select visible country code options"""
    try:
        # Get window size
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.5
        
        # Define scroll area
        scroll_start_y = window_size['height'] * 0.7
        scroll_end_y = window_size['height'] * 0.3
        
        # Random scroll 2-4 times
        num_scrolls = random.randint(2, 4)
        
        # Record seen options to avoid duplicates
        seen_options = set()
        
        for _ in range(num_scrolls):
            # Get current visible options
            visible_options = self.driver.find_elements(*self.personal_page_locators.COUNTRY_CODE_OPTIONS)
            
            # Record current visible options
            for option in visible_options:
                seen_options.add(option.text)
            
            # Randomly decide scroll direction
            if random.choice([True, False]):
                # Scroll up
                self.driver.swipe(start_x, scroll_start_y, start_x, scroll_end_y, duration=500)
            else:
                # Scroll down
                self.driver.swipe(start_x, scroll_end_y, start_x, scroll_start_y, duration=500)
            time.sleep(0.5)
        
        # Get final visible options
        final_visible_options = self.driver.find_elements(*self.personal_page_locators.COUNTRY_CODE_OPTIONS)
        
        if final_visible_options:
            # Randomly select a visible option
            selected_option = random.choice(final_visible_options)
            self.selected_country_code = selected_option.text
            selected_option.click()
            time.sleep(0.5)
            
            # Click confirm button
            self.driver.find_element(*self.personal_page_locators.COUNTRY_CODE_CONFIRM_BUTTON).click()
            time.sleep(0.5)
        else:
            raise NoSuchElementException("No country code options visible after scrolling")
            
    except Exception as e:
        print(f"Scroll and select country code error: {str(e)}")
        raise

  def is_country_code_changed(self):
    """Verify country code is changed"""
    try:
        time.sleep(1) 
        
        current_element = self.driver.find_element(*self.personal_page_locators.CHANGED_COUNTRY_CODE)
        current_code = current_element.text #get country code only
        
        # Extract country code from full text (e.g. from "Russia +7" extract "+7")
        selected_code = "+" + self.selected_country_code.split("+")[-1].strip().split()[0]

        # Compare country code
        is_matched = current_code == selected_code
        
        if is_matched:
            print(f"Country code is successfully updated to: {current_code}")
        else:
            print(f"Country code update failed - Expected: {selected_code}, Actual: {current_code}")
            
        return is_matched
        
    except Exception as e:
        print(f"Verify country code error: {str(e)}")
        return False

  def search_country_code(self):
    """Search and select a random country code"""
    self.driver.find_element(*self.personal_page_locators.COUNTRY_SELECTOR).click()
    
    try: 
        search_term = random.choice(self.personal_page_locators.COMMON_SEARCH_TERMS)
        
        search_input = self.driver.find_element(*self.personal_page_locators.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(search_term["keyword"])
        time.sleep(1)
        
        result = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{search_term["expected"]}")')
        
        self.selected_country_code = result.text
        result.click()
        
        self.driver.find_element(*self.personal_page_locators.COUNTRY_CODE_CONFIRM_BUTTON).click()
        time.sleep(0.5)
        
    except Exception as e:
        print(f"Search country code error: {str(e)}")
        raise

  def click_language_settings(self):
    self.driver.find_element(*self.personal_page_locators.LANGUAGE_SETTINGS_OPTION).click()
    
  def select_language(self):
    self.driver.find_element(*self.personal_page_locators.LANGUAGE_CHINESE_OPTION).click()
    self.driver.find_element(*self.personal_page_locators.LANGUAGE_CONFIRM_BUTTON).click()

  