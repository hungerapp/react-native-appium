import time
import random
import string
import warnings

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from datetime import datetime, timedelta
from appium.webdriver.common.appiumby import AppiumBy

from pages.shared_components.common_use import CommonUseSection


class PersonalPage(CommonUseSection):
  
  def __init__(self, driver):
    self.driver = driver
    # Get window size
    window_size = self.driver.get_window_size()
    # Calculate center coordinates
    self.center_x = window_size['width'] // 2
    self.center_y = window_size['height'] // 2
    
    
  # View basic personal information 
  PROFILE_PICTURE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')
  USERNAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("ann")')
  GREETING_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(".*保持好心情.*|.*開始美好.*|.*好好休息.*")')
  EMAIL_ADDRESS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(".*@.*")')


  # View brand list
  BRAND_LIST_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("品牌列表")')
  BRAND_HUNGER_SALON_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("hunger Salon-staging")')
  BRAND_HUNGER_SALON_PROFILE_PICTURE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
  BRANCH_LIST = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
  BRANCH_ITEM_TEMPLATE = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup//android.widget.TextView[contains(@text, '{}')]"
  FIRST_LOGIN_POP_UP_WINDOW_CANCEL_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)')
  POP_UP_1CANCEL_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
  POP_UP_2CANCEL_ICON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView')
  FREE_WINDOW_BACK_TO_PERSONAL_PAGE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("返回主頁")')
  TALK_TO_YOU_LATER_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("稍後再說")')
  WAY_TO_GIVE_UP_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("忍痛放棄")')
  BACK_TO_PERSONAL_PAGE_BTN = (AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, '分店') or contains(@content-desc, 'Ffff') or contains(@content-desc, 'Ttt')]/descendant::com.horcrux.svg.PathView")
  UNEXPECTED_ERROR_BTN = (AppiumBy.ACCESSIBILITY_ID, '關閉')
  
  
  # Quick functions
  ALL_RESERVATIONS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '所有預約')
  GOOGLE_CALENDAR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Google 日曆')
  PUSH_NOTIFICATION_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '推播設定')
  
  # Push notification page
  PUSH_NOTTIFICATION_SAVE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
  
  # Manage account settings
  SETTINGS_BUTTON = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
  SETTINGS_POPUP = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(7)')
  ACCOUNT_SETTINGS_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帳號設定")')
  LANGUAGE_SETTINGS_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("語言設定")')
  LANGUAGE_CHINESE_OPTION = (AppiumBy.ACCESSIBILITY_ID, '繁體中文, 繁體中文(台灣)')
  LANGUAGE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
  
  
  
  
  # Check if Basic elements are displayed
  def is_profile_picture_displayed(self):
    time.sleep(2)
    assert self.driver.find_element(*self.PROFILE_PICTURE).is_displayed()
  
  def is_username_displayed(self):
    assert self.driver.find_element(*self.USERNAME).is_displayed()
  
  def get_greeting_message_message(self):
    elements = self.driver.find_elements(*self.GREETING_MESSAGE)
    for e in elements:
      text = e.text
      if "早安" in text or "保持好心情" in text or "晚安" in text:
          print("find greeting message", text) 
          return e.text 
    return None
  
  def is_email_address_displayed(self):
    assert self.driver.find_element(*self.EMAIL_ADDRESS).is_displayed()
  
  
  
  # Check if Brand list elements are displayed
  def is_brand_list_title_displayed(self):
    assert self.driver.find_element(*self.BRAND_LIST_TITLE).is_displayed()
  
  def is_brand_hunger_salon_title_displayed(self):
    assert self.driver.find_element(*self.BRAND_HUNGER_SALON_TITLE).is_displayed()
  
  def is_brand_hunger_salon_profile_picture_displayed(self):
    assert self.driver.find_element(*self.BRAND_HUNGER_SALON_PROFILE_PICTURE).is_displayed()
  
  # Branch name list
  BRANCH_NAMES = [
        #{"name": "Pro分店", "locator": (AppiumBy.ACCESSIBILITY_ID, 'Pro分店, 品牌管理員')},
        {"name": "Star分店", "locator": (AppiumBy.ACCESSIBILITY_ID, 'Star分店, 品牌管理員')},
        {"name": "Free分店", "locator": (AppiumBy.ACCESSIBILITY_ID, 'Free分店, 品牌管理員')},
        {"name": "Ultra分店", "locator": (AppiumBy.ACCESSIBILITY_ID, 'Ultra分店, 品牌管理員')}
    ]
  
  
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
    needs_final_back = False
    
    try:
      
        for branch_info in self.BRANCH_NAMES:
            try:
                element = self.driver.find_element(*branch_info["locator"])
                if element.is_displayed():
                    element.click()
                    visited_branches.add(branch_info["name"])
                    needs_final_back = True
                    
                    #time.sleep(0.3)
                    self._handle_popups()
                    self.click_back_to_personal_page()
                    #time.sleep(0.3)
                    
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
    
        unvisited_branches = [branch["name"] for branch in self.BRANCH_NAMES if branch["name"] not in visited_branches]
        if unvisited_branches:
            print(f"Warning: Could not visit branches: {', '.join(unvisited_branches)}")
            
    except Exception as e:
        print(f"Error in visit_all_branches_smart: {str(e)}")
    
    # ensure last time back to personal page
    if needs_final_back:
        try:
            self.click_back_to_personal_page()
        except :
            try:
                self.driver.find_element(*self.POP_UP_1CANCEL_ICON).click()
            except:
                self.driver.find_element(*self.POP_UP_2CANCEL_ICON).click()
            
    
    return results

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
        
  def _handle_popups(self):
    """Handle all possible popups and return buttons"""
    popup_locators = {
        "Cancel Style1 Button": self.POP_UP_1CANCEL_ICON,
        "Cancel Style2 Button": self.POP_UP_2CANCEL_ICON,
        "First Login Pop Up Window Cancel Button": self.FIRST_LOGIN_POP_UP_WINDOW_CANCEL_ICON,
        "Back to Home Button": self.FREE_WINDOW_BACK_TO_PERSONAL_PAGE_BTN,
        "Talk to you later": self.TALK_TO_YOU_LATER_BTN,
    }
    
    handled_popups = []
    for name, locator in popup_locators.items():
        try:
            element = self.driver.find_element(*locator)
            if element.is_displayed():
                element.click()
                time.sleep(0.5)  # Short delay to ensure click takes effect
                handled_popups.append(name)
        except:
            continue
            
    if handled_popups:
        print(f"Handled popups: {', '.join(handled_popups)}")
    
    return len(handled_popups) > 0  # Return whether any popup was handled               
  
  def click_back_to_personal_page(self):
    """Click back to personal page"""
    try:
        self.driver.find_element(*self.WAY_TO_GIVE_UP_BTN).click()
    except:
       self.driver.find_element(*self.BACK_TO_PERSONAL_PAGE_BTN).click()
    time.sleep(1)
    return self
  
  
  
  
  # Push notification
  def click_push_notification_button(self):
    """click push notification button"""
    max_attempts = 3
    attempt = 0
    scroll_direction = "up"  # initial scroll direction is 
    
    while attempt < max_attempts:
        try:
            element = self.driver.find_element(*self.PUSH_NOTIFICATION_BUTTON)
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
  
  # For Toggle locators
  TOGGLE_LOCATORS = {
        "wen_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "sally_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "bella_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "dami_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "ella_toggle": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[2]/android.view.ViewGroup'),
        "test_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "918mmm_toggle": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[7]/android.view.ViewGroup[2]/android.view.ViewGroup'),
        "new1_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[8]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "new2_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[9]/android.view.ViewGroup[2]/android.view.ViewGroup"),
        "cindy_toggle": (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[10]/android.view.ViewGroup[2]/android.view.ViewGroup")
  }
  
  def random_toggle_switches(self, num_toggles=None):
    """
    random toggle switches
    :param num_toggles: number of switches to toggle
    :return: return toggle results list
    """
    if num_toggles is None:
        num_toggles = random.randint(1, len(self.TOGGLE_LOCATORS))
        
    selected_toggles = random.sample(list(self.TOGGLE_LOCATORS.items()), num_toggles)
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
        save_button = self.driver.find_element(*self.PUSH_NOTTIFICATION_SAVE)
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
        settings_button = self.driver.find_element(*self.SETTINGS_BUTTON)
        if settings_button.is_displayed() and settings_button.is_enabled():
            settings_button.click()
                    
        # Verify settings popup
            if self.driver.find_element(*self.SETTINGS_POPUP).is_displayed():
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
    self.driver.find_element(*self.ACCOUNT_SETTINGS_OPTION).click()
    return self
  
  # Locators for account settings page
  NAME_INPUT = [
    (AppiumBy.XPATH, "//android.widget.EditText"),  # 通用的 EditText
    (AppiumBy.CLASS_NAME, "android.widget.EditText"),  # 使用 class name
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ann")'),  # 使用 UiSelector
    (AppiumBy.XPATH, "//android.widget.EditText[contains(@text, 'Ann')]"),
    (AppiumBy.XPATH, '//android.widget.EditText[@text="Ann"]'),
    (AppiumBy.XPATH, "//android.widget.EditText[@text='請輸入姓名']")# 包含特定文本
  ]
  
  GENDER_OPTIONS = {
    "男": (AppiumBy.ACCESSIBILITY_ID, "男"),
    "女": (AppiumBy.ACCESSIBILITY_ID, "女"),
    "其他": (AppiumBy.ACCESSIBILITY_ID, "其他")
  }
  EMPTY_NAME_ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 此欄位為必填。")')
  BIRTHDAY_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("生日")')
  CALENDAR_WINDOW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/pickers")')
  CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")')
  PHONE_INPUT_INITIAL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("\\d{9}")')
  PHONE_INPUT_CLEAR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入電話")')
  EMPTY_PHONE_ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 此欄位為必填。")')
  INVALID_PHONE_ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("格式錯誤")')
  SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)')
  ACCOUNT_SETTINGS_CANCEL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)')
  
  COUNTRY_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(4)')
  COUNTRY_CODE_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '+')]")
  CHANGED_COUNTRY_CODE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+")')
  COUNTRY_CODE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
  
  SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入國家或號碼進行搜尋")')
  
  def generate_random_name(self):
    """Generate random name"""
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    return f"Ann{random_suffix}"

  def clear_and_input_name(self):
    """清除并输入随机姓名"""
    try:
        time.sleep(2)  
        
        for locator_strategy, locator_value in self.NAME_INPUT:
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
        for locator_strategy, locator_value in self.NAME_INPUT:
            try:
                name_field = self.driver.find_element(locator_strategy, locator_value)
                if name_field.is_displayed():
                    print(f"Found name input field, current text: {name_field.text}")
                    
                    # click input field
                    name_field.click()
                    
                    # clear existing text
                    name_field.clear()
                    
                    error_msg = self.driver.find_element(*self.EMPTY_NAME_ERROR_MESSAGE)
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
        phone_field = self.driver.find_element(*self.PHONE_INPUT_INITIAL)
        phone_field.clear()
        
        if valid:
            # Generate a valid phone number
            phone_number = f"{random.randint(900000000, 999999999)}"
        else:
            # Generate an invalid phone number
            phone_number = f"{random.randint(10000, 99999)}"
            
        phone_field_clear = self.driver.find_element(*self.PHONE_INPUT_CLEAR)
        phone_field_clear.send_keys(phone_number)
        return phone_number
    except Exception as e:
        print(f"Input phone number error: {str(e)}")
        raise
  def get_empty_phone_error_message(self):
        """Get error message"""

        phone_field = self.driver.find_element(*self.PHONE_INPUT_INITIAL)
        phone_field.click()
        phone_field.clear()
        error_element = self.driver.find_element(*self.EMPTY_PHONE_ERROR_MESSAGE)
        assert error_element.text == " 此欄位為必填。", "Empty phone error message is not correct"
        return error_element.text
      
  def get_invalid_phone_error_message(self):
        """Get error message"""
        error_element = self.driver.find_element(*self.INVALID_PHONE_ERROR_MESSAGE)
        assert error_element.text == " 格式錯誤。", "Invalid phone error message is not correct"
        return error_element.text

  def save_account_settings(self):
        """Save settings"""
        self.driver.find_element(*self.SAVE_BUTTON).click()
        return self
      
  def cancel_account_settings (self):
        """Cancel account settings"""
        self.driver.find_element(*self.ACCOUNT_SETTINGS_CANCEL_BUTTON).click()
        time.sleep(2)
        return self
  
  def update_account_information_and_save_settings(self):
    
      try:  
            self.select_random_date()
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
        self.driver.find_element(*self.COUNTRY_SELECTOR).click()
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
            visible_options = self.driver.find_elements(*self.COUNTRY_CODE_OPTIONS)
            
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
        final_visible_options = self.driver.find_elements(*self.COUNTRY_CODE_OPTIONS)
        
        if final_visible_options:
            # Randomly select a visible option
            selected_option = random.choice(final_visible_options)
            self.selected_country_code = selected_option.text
            selected_option.click()
            time.sleep(0.5)
            
            # Click confirm button
            self.driver.find_element(*self.COUNTRY_CODE_CONFIRM_BUTTON).click()
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
        
        current_element = self.driver.find_element(*self.CHANGED_COUNTRY_CODE)
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
    self.driver.find_element(*self.COUNTRY_SELECTOR).click()
    
    try:
        # Common country code search terms
        COMMON_SEARCH_TERMS = [
            {"keyword": "台", "expected": "+886"},
            {"keyword": "香", "expected": "+852"},
            {"keyword": "日", "expected": "+81"},
            {"keyword": "美", "expected": "+1"},
            {"keyword": "英", "expected": "+44"},
            {"keyword": "新", "expected": "+65"},
            {"keyword": "澳", "expected": "+61"},
            {"keyword": "中", "expected": "+86"}
        ]
        
    
        search_term = random.choice(COMMON_SEARCH_TERMS)
        
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(search_term["keyword"])
        time.sleep(1)
        
        result = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{search_term["expected"]}")')
        
        self.selected_country_code = result.text
        result.click()
        
        self.driver.find_element(*self.COUNTRY_CODE_CONFIRM_BUTTON).click()
        time.sleep(0.5)
        
    except Exception as e:
        print(f"Search country code error: {str(e)}")
        raise

  def click_language_settings(self):
    self.driver.find_element(*self.LANGUAGE_SETTINGS_OPTION).click()
    
  def select_language(self):
    self.driver.find_element(*self.LANGUAGE_CHINESE_OPTION).click()
    self.driver.find_element(*self.LANGUAGE_CONFIRM_BUTTON).click()

  