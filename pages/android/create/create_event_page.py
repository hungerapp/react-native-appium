import time
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from pages.locators.android.create.create_event_locators import CreateEventLocators
from pages.shared_components.common_use import CommonUseSection
from pages.shared_components.common_action import CommonActions


class CreateEventPage(CommonUseSection):
    def __init__(self, driver):
        super().__init__(driver)
        self.common_actions = CommonActions(driver)
        
    ############# Used Gestures #############
    def swipe_and_close_time_picker(self):
        window_size = self.common_actions.get_screen_size()
        width = window_size[0]
        height = window_size[1]
        

        picker_top = height * 0.45     # time picker middle position
        picker_height = height * 0.15   # picker visible area height
        
        # more accurate hour and minute positions (based on the image)
        hour_x = width * 0.33    # hour position (aligned with "01")
        minute_x = width * 0.67   # minute position (aligned with "00")
        
        
        # start time swipe operation
        # swipe hour
        self.swipe_gesture(
          x=int(hour_x - 5),
          y=int(picker_top),
          width=20, # swipe area width
          height=int(picker_height),
          direction='up',
          percent=0.6,   
          speed=1000      
          )
        time.sleep(0.5)
        
        # swipe minute
        self.swipe_gesture(
          x=int(minute_x - 5),
          y=int(picker_top),
          width=20,
          height=int(picker_height),
          direction='up',
          percent=0.5,
          speed=1000
          )
        time.sleep(1)
        
        # click end time block
        self.common_actions.click_element(*CreateEventLocators.CLICK_END_TIME)
        time.sleep(1.5)
        
        # end time swipe operation
        # swipe hour
        self.swipe_gesture(
          x=int(hour_x - 5),
          y=int(picker_top),
          width=20,
          height=int(picker_height),
          direction='up',
          percent=0.98,
          speed=3000
          )
        time.sleep(0.5)
        
        # swipe minute
        self.swipe_gesture(
          x=int(minute_x - 5),
          y=int(picker_top),
          width=20,
          height=int(picker_height),
          direction='up',
          percent=0.85,
          speed=2000
          )
        time.sleep(0.5)
        
        # click outside to close the time window
        window_size = self.common_actions.get_screen_size()
        self.common_actions.tap(int(window_size[0] * 0.5), int(window_size[1] * 0.9))
    ###############################################   
    
    def create_event_option(self):
        try:
          self.common_actions.is_element_visible(*CreateEventLocators.CREATE_BTN)
          self.common_actions.click_element(*CreateEventLocators.CREATE_BTN)
              
          self.common_actions.click_element(*CreateEventLocators.CREATE_EVENT_OPTION)
                    
        except NoSuchElementException:
          raise NoSuchElementException("Unable to find create appointment button after multiple attempts")
      
        return self
    
    def click_event_section(self):
        self.common_actions.is_element_visible(*CreateEventLocators.EVENT)
        self.common_actions.click_element(*CreateEventLocators.EVENT)

    def quickly_select_event(self):
        try:
            time.sleep(0.5)
            random_option = random.choice(CreateEventLocators.QUICK_OPTIONS)
            quick_select = self.driver.find_element(
            AppiumBy.XPATH,
            f"//android.widget.TextView[@text='{random_option}']"
            )
            quick_select.click()
            
            self.common_actions.click_element(*CreateEventLocators.SAVE_BUTTON)
        
        except Exception as e:
            print(f"Quickly select event failed: {str(e)}")

    def enter_event_title(self, title=None):
        if title is not None:
            self.common_actions.send_keys_to_element(*CreateEventLocators.EVENT_TITLE_INPUT, title)
        
        self.common_actions.click_element(*CreateEventLocators.SAVE_BUTTON)
        
    def click_time_section(self):
        self.common_actions.is_element_visible(*CreateEventLocators.TIME)
        self.common_actions.click_element(*CreateEventLocators.TIME)
    
    def select_event_time(self, all_day=True):
        self.common_actions.is_element_visible(*CreateEventLocators.SELECTED_DATE)
        self.common_actions.click_element(*CreateEventLocators.SELECTED_DATE)
        self.choose_date()
        
        if all_day:
            self.common_actions.is_element_visible(*CreateEventLocators.ALL_DAY_TOGGLE)
            self.common_actions.click_element(*CreateEventLocators.ALL_DAY_TOGGLE)
        else:
            self.common_actions.is_element_visible(*CreateEventLocators.CLICK_START_TIME)
            self.common_actions.click_element(*CreateEventLocators.CLICK_START_TIME)
            time.sleep(0.5)
            self.swipe_and_close_time_picker()
        self.common_actions.click_element(*CreateEventLocators.TIME_SAVE_BUTTON)
        
    def change_selected_time(self):
        self.common_actions.is_element_visible(*CreateEventLocators.TIME)
        self.common_actions.click_element(*CreateEventLocators.TIME)
        self.common_actions.is_element_visible(*CreateEventLocators.SELECTED_DATE)
        self.common_actions.click_element(*CreateEventLocators.SELECTED_DATE)
        self.choose_date()
        self.common_actions.click_element(*CreateEventLocators.TIME_SAVE_BUTTON)
        
    def click_repeat_section(self):
        self.common_actions.is_element_visible(*CreateEventLocators.REPEAT)
        self.common_actions.click_element(*CreateEventLocators.REPEAT)
        self.common_actions.click_element(*CreateEventLocators.REPEAT_SAVE_BUTTON)
    
    def toggle_repeat_option(self, enable=False, multi_select=True):
        self.common_actions.is_element_visible(*CreateEventLocators.REPEAT)
        self.common_actions.click_element(*CreateEventLocators.REPEAT)
        time.sleep(0.5)
        repeat_toggle = self.common_actions.find_element(*CreateEventLocators.REPEAT_TOGGLE)
        if enable != repeat_toggle.is_selected():
            repeat_toggle.click()
            try:
                if multi_select:
                    num_selections = random.randint(2,4)
                    selected_days = random.sample(CreateEventLocators.WEEKDAYS, num_selections)
                    
                    for day in selected_days:
                        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, day).click()
                else:
                    selected_day = random.choice(CreateEventLocators.WEEKDAYS)
                    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, selected_day).click()
            except Exception as e:
                print(f"Toggle repeat option failed: {str(e)}")
              
        self.common_actions.click_element(*CreateEventLocators.REPEAT_SAVE_BUTTON)

    def click_repeat_toggle(self):
        self.common_actions.is_element_visible(*CreateEventLocators.REPEAT)
        self.common_actions.click_element(*CreateEventLocators.REPEAT)
        self.common_actions.is_element_visible(*CreateEventLocators.REPEAT_TOGGLE)
        self.common_actions.click_element(*CreateEventLocators.REPEAT_TOGGLE)
        self.common_actions.click_element(*CreateEventLocators.REPEAT_SAVE_BUTTON)

    def click_save_button(self):
        self.common_actions.is_element_visible(*CreateEventLocators.SAVE_BUTTON)
        self.common_actions.click_element(*CreateEventLocators.SAVE_BUTTON)
        
    def new_event_page_save_button(self):
        self.common_actions.is_element_visible(*CreateEventLocators.NEW_EVENT_PAGE_SAVE_BUTTON)
        self.common_actions.click_element(*CreateEventLocators.NEW_EVENT_PAGE_SAVE_BUTTON)

    def verify_error_message(self):
        try:
            error_message = self.common_actions.get_element_text(*CreateEventLocators.ERROR_MESSAGE)
            actual_message = error_message.strip()
            expected_message = "此欄位為必填。"
            assert actual_message == expected_message, f"Expected message: {expected_message}, but got: {actual_message}"
            return True
            
        except NoSuchElementException:
            return False
    
    def verify_time_error_display(self):
        self.common_actions.is_element_visible(*CreateEventLocators.TIME_SAVE_BUTTON)
        self.common_actions.click_element(*CreateEventLocators.TIME_SAVE_BUTTON)
        try:
            error_icon1 = self.driver.find_element(*CreateEventLocators.ERROR_ICON1)
            error_icon2 = self.driver.find_element(*CreateEventLocators.ERROR_ICON2)
            error_icon3 = self.driver.find_element(*CreateEventLocators.ERROR_ICON3)
            assert error_icon1.is_displayed() and error_icon2.is_displayed() and error_icon3.is_displayed(), "Expected error icon to be displayed"
            return True
        except NoSuchElementException:
            return False
        
    def click_repeat_back_button(self):
        self.common_actions.is_element_visible(*CreateEventLocators.REPEAT_BACK_BUTTON)
        self.common_actions.click_element(*CreateEventLocators.REPEAT_BACK_BUTTON)
        self.common_actions.is_element_visible(*CreateEventLocators.BACK_TO_CALENDAR)
        self.common_actions.click_element(*CreateEventLocators.BACK_TO_CALENDAR)
        self.common_actions.is_element_visible(*CreateEventLocators.WINDOW_LEAVE_BUTTON)
        self.common_actions.click_element(*CreateEventLocators.WINDOW_LEAVE_BUTTON)
    
    def modify_quick_select_settings(self):
        self.common_actions.is_element_visible(*CreateEventLocators.MODIFY_QUICK_SELECT_ICON)
        self.common_actions.click_element(*CreateEventLocators.MODIFY_QUICK_SELECT_ICON)

        
        
        
        