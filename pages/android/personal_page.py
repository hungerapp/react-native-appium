import time
import random
import string

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.appiumby import AppiumBy

from pages.shared_components.common_use import CommonUseSection
from pages.shared_components.common_action import CommonActions
from pages.locators.android.personal_page.personal_page_locators import PersonalPageLocators

class PersonalPage(CommonUseSection):
  
  def __init__(self, driver):
    super().__init__(driver)
    self.common_action = CommonActions(driver)
    
  
  ############# Used Gestures #############
  def _scroll_down(self):
    """Scroll down"""
    try:
        screen_size = self.common_action.get_screen_size()
        start_x = screen_size[0] * 0.5
        start_y = screen_size[1] * 0.7
        end_y = screen_size[1] * 0.3
        
        # execute scroll
        self.common_action.swipe(
            start_x, 
            start_y, 
            start_x, 
            end_y, 
            duration=500
        )
    except Exception as e:
        print(f"[PersonalPage][_scroll_down] error: {str(e)}")
        raise
    
  def _scroll_to_top(self):
    """Scroll to top"""
    try:
        screen_size = self.common_action.get_screen_size()
        start_x = screen_size[0] * 0.5
        start_y = screen_size[1] * 0.3
        end_y = screen_size[1] * 0.7
        
        # scroll to top
        self.common_action.swipe(
            start_x, 
            start_y, 
            start_x, 
            end_y, 
            duration=500
        )
    except Exception as e:
        print(f"[PersonalPage][_scroll_to_top] error: {str(e)}")
        raise
    
  def _perform_random_swipe(self, start_x, start_y, max_offset=50):
    """Perform random swipe"""
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
        print(f"[PersonalPage][_perform_random_swipe] error: {str(e)}")
        raise
      
  ###############################################
  
  # Check if Basic elements are displayed (profile picture, username, greeting message, email address)
  def is_profile_picture_displayed(self):
    assert self.common_action.is_element_visible(*PersonalPageLocators.PROFILE_PICTURE)
  
  def is_username_displayed(self):
    assert self.common_action.is_element_visible(*PersonalPageLocators.USERNAME)
  
  def get_greeting_message_message(self):
    elements = self.driver.find_elements(*PersonalPageLocators.GREETING_MESSAGE)
    for e in elements:
      text = e.text
      if "早安" in text or "保持好心情" in text or "晚安" in text:
          print("find greeting message", text) 
          return e.text 
    return None
  
  def is_email_address_displayed(self):
    assert self.common_action.is_element_visible(*PersonalPageLocators.EMAIL_ADDRESS)
  
  # Check if Brand list elements are displayed (brand list title, brand hunger title, brand profile picture)
  def is_brand_list_title_displayed(self):
    assert self.common_action.is_element_visible(*PersonalPageLocators.BRAND_LIST_TITLE)
  
  def is_brand_hunger_salon_title_displayed(self):
    assert self.common_action.is_element_visible(*PersonalPageLocators.BRAND_HUNGER_SALON_TITLE)
  
  def is_brand_hunger_salon_profile_picture_displayed(self):
    assert self.common_action.is_element_visible(*PersonalPageLocators.BRAND_HUNGER_SALON_PROFILE_PICTURE)

  def visit_all_branches_smart(self):
    """click star free ultra branch"""
    results = []
    visited_branches = set()
   
    try:
        for branch_info in PersonalPageLocators.BRANCH_NAMES:
            try:
                element = self.common_action.find_element(*branch_info["locator"])
                if element.is_displayed():
                    element.click()
                    visited_branches.add(branch_info["name"])
                 
                    # Handle specific branch scenarios
                    if branch_info["name"] == "Free分店":
                        self.common_action.click_element(*PersonalPageLocators.POP_UP_CANCEL_ICON)
                        self.common_action.click_element(*PersonalPageLocators.FREE_WINDOW_BACK_TO_PERSONAL_PAGE_BTN)
                    elif branch_info["name"] == "Star分店":
                        self.common_action.click_element(*PersonalPageLocators.POP_UP_CANCEL_ICON)
                        self.common_action.click_element(*PersonalPageLocators.BACK_TO_PERSONAL_PAGE_BTN)
                    else:
                        self.common_action.click_element(*PersonalPageLocators.POP_UP_CANCEL_ICON)
                        self.common_action.click_element(*PersonalPageLocators.BACK_TO_PERSONAL_PAGE_BTN)

                    results.append({
                        "branch_name": branch_info["name"],
                        "status": "success"
                    })
            except Exception as e:
                print(f"[PersonalPage][visit_all_branches_smart] error clicking branch {branch_info['name']}: {str(e)}")
                results.append({
                    "branch_name": branch_info["name"],
                    "status": "error",
                    "error": str(e)
                })
    
        unvisited_branches = [branch["name"] for branch in PersonalPageLocators.BRANCH_NAMES if branch["name"] not in visited_branches]
        if unvisited_branches:
            print(f"[PersonalPage][visit_all_branches_smart] Warning: Could not visit branches: {', '.join(unvisited_branches)}")
        
        # finally click Pro branch
        self.common_action.click_element(*PersonalPageLocators.PRO_BRANCH_NAME)
        self.common_action.click_element(*PersonalPageLocators.POP_UP_CANCEL_ICON)
        self.common_action.click_element(*PersonalPageLocators.BACK_TO_PERSONAL_PAGE_BTN)
            
    except Exception as e:
        print(f"[PersonalPage][visit_all_branches_smart] error: {str(e)}")
        raise
        
  # Google Calendar
  def click_google_calendar_button(self):
    self.common_action.click_element(*PersonalPageLocators.GOOGLE_CALENDAR_BUTTON)
    return self
  
  def integrate_google_calendar(self):
    self.common_action.click_element(*PersonalPageLocators.INTEGRATE_GOOGLE_CALENDAR_BUTTON)
    time.sleep(1)
    for _ in range (2):
        time.sleep(0.5)
        self.driver.back()
    return self
  
  # Push notification
  def click_push_notification_button(self):
    self.common_action.click_element(*PersonalPageLocators.PUSH_NOTIFICATION_BUTTON)
    return self
  
  def random_toggle_switches(self, num_toggles=None):
    """
    random toggle switches
    :param num_toggles: number of switches to toggle
    :return: return toggle results list
    """
    if num_toggles is None:
        num_toggles = random.randint(1, len(PersonalPageLocators.TOGGLE_LOCATORS))
        
    selected_toggles = random.sample(list(PersonalPageLocators.TOGGLE_LOCATORS.items()), num_toggles)
    toggled_results = []
    
    for toggle_name, toggle_locator in selected_toggles:
        try:
            # try to find element
            toggle = self.common_action.find_element(*toggle_locator)
            
            # get element location
            location = toggle.location
            size = toggle.size
            
            # calculate element center point
            target_y = location['y'] + (size['height'] / 2)
            
            # get screen size
            screen_size = self.common_action.get_screen_size()
            start_x = screen_size[0] * 0.5
            
            # if element is out of screen, scroll to it
            if target_y > screen_size[1]:
                self.common_action.swipe(
                    start_x,
                    screen_size[1] * 0.7,
                    start_x,
                    screen_size[1] * 0.3,
                    duration=500
                )
                time.sleep(0.5)
            
            # check element and click
            toggle = self.common_action.find_element(*toggle_locator)
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
        save_button = self.common_action.find_element(*PersonalPageLocators.PUSH_NOTIFICATION_SAVE)
        save_button.click()
        return self

  def toggle_num(self, num_toggles=None):
        """Toggle and save"""
        results = self.random_toggle_switches(num_toggles)
        return results    

  def click_setting_icon(self):
    """Click settings icon and verify settings popup is displayed"""

    # try to find and click settings button
    try:
        self.common_action.click_element(*PersonalPageLocators.SETTINGS_BUTTON)
                    
        # Verify settings popup
        if self.common_action.is_element_visible(*PersonalPageLocators.SETTINGS_POPUP):
            print("Successfully clicked settings button and displayed settings popup")
            return self
    except NoSuchElementException:
      raise NoSuchElementException("Unable to find settings button after multiple attempts")
  
  def click_account_settings(self):
    """Click account settings"""
    self.common_action.click_element(*PersonalPageLocators.ACCOUNT_SETTINGS_OPTION)
    return self
  
  def generate_random_name(self):
    """Generate random name"""
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    return f"QAtest{random_suffix}"

  def clear_and_input_name(self):
    try:
        name_field = self.common_action.find_element(*PersonalPageLocators.NAME_INPUT)
        if name_field.is_displayed():
            print(f"Found name input field, current text: {name_field.text}") 
            
            # clear existing text
            name_field.clear()
            
            # input new text
            random_name = self.generate_random_name()
            time.sleep(2)
            name_field.send_keys(random_name)
            
            print(f"Successfully input new name: {random_name}")
            return random_name
            
        raise NoSuchElementException("Name input field is not visible")
        
    except Exception as e:
        print(f"[PersonalPage][clear_and_input_name] error: {str(e)}")
        raise
        
  def get_empty_name_error_message(self):
        """Get empty name error message"""
        try:
            name_field = self.common_action.find_element(*PersonalPageLocators.NAME_INPUT)
            if name_field.is_displayed():
                print(f"Found name input field, current text: {name_field.text}")
                
                # clear existing text
                name_field.clear()
                
                error_msg = self.common_action.get_element_text(*PersonalPageLocators.EMPTY_NAME_ERROR_MESSAGE)
                assert error_msg == " 此欄位為必填。", "Empty name error message is not correct"
                return error_msg
              
        except Exception as e:
            print(f"[PersonalPage][get_empty_name_error_message] error: {str(e)}")
            raise
          
  def input_phone_number(self, valid: bool = True):
    """Input phone number"""
    try:
        self.common_action.clear_text(*PersonalPageLocators.PHONE_INPUT_INITIAL)
        
        if valid:
            # Generate a valid phone number
            phone_number = f"{random.randint(900000000, 999999999)}"
        else:
            # Generate an invalid phone number
            phone_number = f"{random.randint(10000, 99999)}"
        
        phone_input = self.common_action.find_element(*PersonalPageLocators.PHONE_INPUT_INITIAL)
        phone_input.send_keys(phone_number)
        return phone_number
    except Exception as e:
        print(f"[PersonalPage][input_phone_number] error: {str(e)}")
        raise
    
  def get_empty_phone_error_message(self):
        """Get error message"""
        
        self.common_action.clear_text(*PersonalPageLocators.PHONE_INPUT_INITIAL)
        error_element = self.common_action.get_element_text(*PersonalPageLocators.EMPTY_PHONE_ERROR_MESSAGE)
        assert error_element == " 此欄位為必填。", "Empty phone error message is not correct"
        return error_element
      
  def get_invalid_phone_error_message(self):
        """Get error message"""
        error_element = self.common_action.get_element_text(*PersonalPageLocators.INVALID_PHONE_ERROR_MESSAGE)
        assert error_element == " 格式錯誤。", "Invalid phone error message is not correct"
        return error_element

  def save_account_settings(self):
        """Save settings"""
        self.common_action.click_element(*PersonalPageLocators.SAVE_BUTTON)
        return self
      
  def cancel_account_settings (self):
        """Cancel account settings"""
        self.common_action.click_element(*PersonalPageLocators.ACCOUNT_SETTINGS_CANCEL_BUTTON)
        return self
  
  def update_account_information_and_save_settings(self):
    
      try:  
            # click birthday field to open date picker
            self.common_action.click_element(*PersonalPageLocators.BIRTHDAY_FIELD)
            self.swipe_calendar_component()
            
            self.select_random_gender()
            self.clear_and_input_name()
            self.input_phone_number(valid=True)
            self.save_account_settings()
            
      except Exception as e:
            error_msg = f"[PersonalPage][update_account_information_and_save_settings] Update failed: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

  def search_country_code(self):
    """Search and select a random country code"""
    self.common_action.click_element(*PersonalPageLocators.COUNTRY_SELECTOR)
    
    try: 
        search_term = random.choice(PersonalPageLocators.COMMON_SEARCH_TERMS)
        
        search_input = self.common_action.find_element(*PersonalPageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(search_term["keyword"])
        time.sleep(1)
        
        result = self.common_action.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{search_term["expected"]}")')
        
        self.selected_country_code = result.text
        result.click()
        
        self.common_action.click_element(*PersonalPageLocators.COUNTRY_CODE_CONFIRM_BUTTON)
        
    except Exception as e:
        print(f"Search country code error: {str(e)}")
        raise
    
  def click_language_settings(self):
    self.common_action.click_element(*PersonalPageLocators.LANGUAGE_SETTINGS_OPTION)
    
  def select_language(self):
    self.common_action.click_element(*PersonalPageLocators.LANGUAGE_CHINESE_OPTION)
    self.common_action.click_element(*PersonalPageLocators.LANGUAGE_CONFIRM_BUTTON)

  