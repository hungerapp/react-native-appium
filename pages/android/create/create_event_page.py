import time
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from pages.locators.android.create.create_event_locators import CreateEventLocators

class CreateEventPage:
    def __init__(self, driver):
        self.driver = driver
        self.create_event_locators = CreateEventLocators()
        
        
    def create_event_option(self):
        try:
          time.sleep(1.5)
          create_button = self.driver.find_element(*self.create_event_locators.CREATE_BTN)
          if create_button.is_displayed() and create_button.is_enabled():
              create_button.click()
              
          self.driver.find_element(*self.create_event_locators.CREATE_EVENT_OPTION).click()
                    
        except NoSuchElementException:
          raise NoSuchElementException("Unable to find create appointment button after multiple attempts")
      
        return self
    
    
    def click_event_section(self):
        time.sleep(0.5)
        self.driver.find_element(*self.create_event_locators.EVENT).click()

    
    def quickly_select_event(self):
        time.sleep(0.5)
        try:
            random_option = random.choice(self.create_event_locators.QUICK_OPTIONS)

            quick_select = self.driver.find_element(
            AppiumBy.XPATH,
            f"//android.widget.TextView[@text='{random_option}']"
            )
            quick_select.click()
            time.sleep(0.5)
            
            self.driver.find_element(*self.create_event_locators.SAVE_BUTTON).click()
        
        except Exception as e:
                print(f"快速選取失敗: {str(e)}")

    def enter_event_title(self, title=None):
        time.sleep(0.5)
        
        if title is not None:
            self.driver.find_element(*self.create_event_locators.EVENT_TITLE_INPUT).send_keys(title)
        
        time.sleep(0.5)
        self.driver.find_element(*self.create_event_locators.SAVE_BUTTON).click()
        

    
    def click_time_section(self):
        self.driver.find_element(*self.create_event_locators.TIME).click()
        time.sleep(1)
    
    def select_event_time(self, all_day=True):
        
        self.driver.find_element(*self.create_event_locators.SELECTED_DATE).click()
        
        # select random date
        direction = random.choice(['left', 'right'])
        if direction == 'left':
            arrow = self.driver.find_element(*self.create_event_locators.LEFT_DATE_ARROW)
        else:
            arrow = self.driver.find_element(*self.create_event_locators.RIGHT_DATE_ARROW)
            arrow.click()
            
        dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      
        random.choice(dates).click()
        
        # click outside to close the date window
        size = self.driver.get_window_size()
        self.driver.execute_script('mobile: clickGesture', {
            'x': int(size['width'] * 0.5),  
            'y': int(size['height'] * 0.9)   
        })
        
        time.sleep(0.5)
        
        if all_day:
            self.driver.find_element(*self.create_event_locators.ALL_DAY_TOGGLE).click()
        else:
            self.driver.find_element(*self.create_event_locators.CLICK_START_TIME).click()
            time.sleep(0.5)

            window_size = self.driver.get_window_size()
            width = window_size['width']
            height = window_size['height']
        
            # calculate the position of the time picker (more accurate positioning based on the image)
            picker_top = height * 0.45     # time picker middle position
            picker_height = height * 0.15   # picker visible area height
        
            # more accurate hour and minute positions (based on the image)
            hour_x = width * 0.33    # hour position (aligned with "01")
            minute_x = width * 0.67   # minute position (aligned with "00")
        
        
            # start time swipe operation
            # swipe hour
            self.driver.execute_script('mobile: swipeGesture', {
            'left': int(hour_x - 10),
            'top': int(picker_top),
            'width': 20,         # swipe area width
            'height': int(picker_height),
            'direction': 'up',
            'percent': 0.6,   
            'speed': 1000      
            })
            
            time.sleep(0.5)
        
            # swipe minute
            self.driver.execute_script('mobile: swipeGesture', {
            'left': int(minute_x - 10),
            'top': int(picker_top),
            'width': 20,
            'height': int(picker_height),
            'direction': 'up',
            'percent': 0.5,
            'speed': 1500
            })
        
            time.sleep(0.5)
        
            # click end time block
            self.driver.find_element(*self.create_event_locators.CLICK_END_TIME).click()
            time.sleep(1.5)
        
            # end time swipe operation
            # swipe hour
            self.driver.execute_script('mobile: swipeGesture', {
            'left': int(hour_x - 10),
            'top': int(picker_top),
            'width': 20,
            'height': int(picker_height),
            'direction': 'up',
            'percent': 0.95,
            'speed': 3000
            })
        
            time.sleep(0.5)
        
            # swipe minute
            self.driver.execute_script('mobile: swipeGesture', {
            'left': int(minute_x - 10),
            'top': int(picker_top),
            'width': 20,
            'height': int(picker_height),
            'direction': 'up',
            'percent': 0.5,
            'speed': 1500
            })
        
            time.sleep(0.5)
        
            # click outside to close the time window
            window_size = self.driver.get_window_size()
            self.driver.execute_script('mobile: clickGesture', {
            'x': int(window_size['width'] * 0.5),
            'y': int(window_size['height'] * 0.9)
            })
        self.driver.find_element(*self.create_event_locators.TIME_SAVE_BUTTON).click()
        time.sleep(1)
        
    def change_selected_time(self):
        self.driver.find_element(*self.create_event_locators.TIME).click()
        self.driver.find_element(*self.create_event_locators.SELECTED_DATE).click()

        # select random date
        direction = random.choice(['left', 'right'])
        if direction == 'left':
            arrow = self.driver.find_element(*self.create_event_locators.LEFT_DATE_ARROW)
        else:
            arrow = self.driver.find_element(*self.create_event_locators.RIGHT_DATE_ARROW)
            arrow.click()
                
        dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      
        random.choice(dates).click()
        
        # click outside to close the date window
        size = self.driver.get_window_size()
        self.driver.execute_script('mobile: clickGesture', {
            'x': int(size['width'] * 0.5),  
            'y': int(size['height'] * 0.9)   
        })
        
        time.sleep(0.5)
        self.driver.find_element(*self.create_event_locators.TIME_SAVE_BUTTON).click()
        
    
    def click_repeat_section(self):
        time.sleep(0.5)
        self.driver.find_element(*self.create_event_locators.REPEAT).click()
        self.driver.find_element(*self.create_event_locators.REPEAT_SAVE_BUTTON).click()
    
    def toggle_repeat_option(self, enable=False, multi_select=True):
        self.driver.find_element(*self.create_event_locators.REPEAT).click()
        time.sleep(0.5)
        repeat_toggle = self.driver.find_element(*self.create_event_locators.REPEAT_TOGGLE)
        if enable != repeat_toggle.is_selected():
            repeat_toggle.click()
            try:
                if multi_select:
                    num_selections = random.randint(2,4)
                    selected_days = random.sample(self.create_event_locators.WEEKDAYS, num_selections)
                    
                    for day in selected_days:
                        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, day).click()
                else:
                    selected_day = random.choice(self.create_event_locators.WEEKDAYS)
                    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, selected_day).click()
            except Exception as e:
                print(f"Toggle repeat option failed: {str(e)}")
                
                
                
        self.driver.find_element(*self.create_event_locators.REPEAT_SAVE_BUTTON).click()

    def click_repeat_toggle(self):
        time.sleep(1.5)
        self.driver.find_element(*self.create_event_locators.REPEAT).click()
        time.sleep(0.5)
        repeat_toggle = self.driver.find_element(*self.create_event_locators.REPEAT_TOGGLE)
        repeat_toggle.click()
        self.driver.find_element(*self.create_event_locators.REPEAT_SAVE_BUTTON).click()

        
    def click_save_button(self):
        time.sleep(0.5)
        self.driver.find_element(*self.create_event_locators.SAVE_BUTTON).click()
        
    def new_event_page_save_button(self):
        time.sleep(0.5)
        self.driver.find_element(*self.create_event_locators.NEW_EVENT_PAGE_SAVE_BUTTON).click()

    def verify_error_message(self):
        try:
            error_message = self.driver.find_element(*self.create_event_locators.ERROR_MESSAGE)
            actual_message = error_message.text.strip()
            expected_message = "此欄位為必填。"
            assert actual_message == expected_message, f"Expected message: {expected_message}, but got: {actual_message}"
            return True
            
        except NoSuchElementException:
            return False
    
    def verify_time_error_display(self):
        self.driver.find_element(*self.create_event_locators.TIME_SAVE_BUTTON).click()
        try:
            error_icon1 = self.driver.find_element(*self.create_event_locators.ERROR_ICON1)
            error_icon2 = self.driver.find_element(*self.create_event_locators.ERROR_ICON2)
            error_icon3 = self.driver.find_element(*self.create_event_locators.ERROR_ICON3)
            assert error_icon1.is_displayed() and error_icon2.is_displayed() and error_icon3.is_displayed(), "Expected error icon to be displayed"
            return True
        except NoSuchElementException:
            return False
        
    def click_repeat_back_button(self):
        self.driver.find_element(*self.create_event_locators.REPEAT_BACK_BUTTON).click()
        time.sleep(0.5)
        self.driver.find_element(*self.create_event_locators.BACK_TO_CALENDAR).click()
        self.driver.find_element(*self.create_event_locators.WINDOW_LEAVE_BUTTON).click()
    
    def modify_quick_select_settings(self):
        self.driver.find_element(*self.create_event_locators.MODIFY_QUICK_SELECT_ICON).click()
        time.sleep(0.5)
        
        
        