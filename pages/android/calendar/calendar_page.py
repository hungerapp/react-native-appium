import random
import time

from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy

from pages.locators.android.calendar.calendar_locators import CalendarLocators
from pages.shared_components.common_action import CommonActions


class CalendarPage:
    def __init__(self, driver):
        self.driver = driver
        self.current_display_mode = None
        self.calendar_locators = CalendarLocators()
        self.common_actions = CommonActions(driver)

    
    def open_month_selection(self):
        time.sleep(2)
        self.driver.find_element(*self.calendar_locators.DATE_SELECTOR).click()

    def change_month_display_mode(self):
        clicks_arrow = random.randint(1, 4)
        for _ in range(clicks_arrow):
            self.driver.find_element(*self.calendar_locators.ARROW).click()
            time.sleep(0.5)
        
        time.sleep(0.5)
        random_month = random.choice(self.calendar_locators.MONTHS)
        self.driver.find_element(*random_month).click()
    
    def change_calendar_display(self):
        time.sleep(1.5)
        self.driver.find_element(*self.calendar_locators.DISPLAY_MODES[0]).click()
        
    def select_target_display_mode(self):
        """Select a random display mode from the window"""
        select_window = self.driver.find_element(*self.calendar_locators.SELECT_WINDOW)
        if select_window.is_displayed() and select_window.is_enabled():
            self.current_display_mode = 5
            self.driver.find_element(*self.calendar_locators.DISPLAY_MODES[5]).click()

    def switch_back_to_month_mode(self):
        """Switch back to the month display mode"""
        if self.current_display_mode is None:
            time.sleep(2)
            current_mode_button = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="列表 (日)"]')
            current_mode_button.click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="月"]').click() 

    def filter_personnel(self):
        time.sleep(0.5)
        self.driver.find_element(*self.calendar_locators.FILTER_ICON).click()

    def select_personnel(self):
        choice = random.choice(list(self.calendar_locators.PERSONNEL_OPTIONS.keys()))
        
        if isinstance(self.calendar_locators.PERSONNEL_OPTIONS[choice], list):
            time.sleep(0.5)
            for element_id in self.calendar_locators.PERSONNEL_OPTIONS[choice]:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, element_id).click()
        else:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.calendar_locators.PERSONNEL_OPTIONS[choice]).click()
            
        
            
            
    def edit_personnel_colors(self):
        edit_color = self.driver.find_element(*self.calendar_locators.EDIT_COLOR)
        edit_color.click()
       
        color_xpath = random.choice(self.calendar_locators.COLOR_XPATHS)
        time.sleep(0.5)
        color_choice = self.driver.find_element(AppiumBy.XPATH, color_xpath)
        color_choice.click()
        
        self.driver.find_element(*self.calendar_locators.FILTER_SAVE_BUTTON).click()
        
    def change_personnel_filter(self):
        time.sleep(0.5)
        self.driver.find_element(*self.calendar_locators.FILTER_ICON).click()
        self.driver.find_element(*self.calendar_locators.SELECT_ALL_PERSONNEL).click()
        time.sleep(0.5)
        self.driver.find_element(*self.calendar_locators.FILTER_SAVE_BUTTON).click()
    
    def perform_swipe_left_or_right(self, direction=None, times=None):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        # 定義滑動的中心位置
        start_x = width * 0.6 if direction == 'left' else width * 0.4
        y = height * 0.6

        swipe_times = times if times else random.randint(3, 4)
        swipe_direction = direction if direction else random.choice(['left', 'right'])

        for _ in range(swipe_times):
            self.driver.execute_script("mobile: swipeGesture", {
                'left': start_x,
                'top': y,
                'width': width * 0.5,
                'height': 10,
                'direction': swipe_direction,
                'percent': 0.6
            })
            time.sleep(1) 
    
    def navigate_to_today(self):
        time.sleep(1)
        self.driver.find_element(*self.calendar_locators.TODAY_ICON).click()


    def view_orders(self):
        """Click on a random point in the calendar area"""
        try:

            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']
            
            # Calculate the coordinates of the calendar area
            calendar_top = height * 0.3     # Avoid the top title area
            calendar_bottom = height * 0.7   # Avoid the bottom navigation area
            calendar_left = width * 0.1      # Left boundary
            calendar_right = width * 0.9     # Right boundary
            
            # Randomly select a point in the calendar area
            x = random.uniform(calendar_left, calendar_right)
            y = random.uniform(calendar_top, calendar_bottom)
            
            # Execute click gesture
            self.driver.execute_script('mobile: clickGesture', {
                'x': x,
                'y': y
            })
            
            time.sleep(2)
            
        except Exception as e:
            raise Exception(f"Cannot click on the calendar area: {str(e)}")

    def click_back_button(self):
        self.driver.back()
        time.sleep(1)
        
    def long_press_date(self):
        time.sleep(1)
        try:
            element = self.driver.find_element(
            *self.calendar_locators.LONG_PRESS_DATE
            )
        
            actions = ActionChains(self.driver)
            actions.click_and_hold(element)
            actions.pause(2)  
            actions.release()
            actions.perform()
        
        except Exception as e:
            print(f"長按操作失敗: {str(e)}")
            raise
    
    def add_appointment(self):
        time.sleep(1)
        add_appointment_option = self.driver.find_element(*self.calendar_locators.ADD_APPOINTMENT_OPTION)
        if add_appointment_option.is_displayed():
            time.sleep(0.5)
            add_appointment_option.click()
        else:
            print("Add appointment option is not visible or enabled")
              
        
    def add_event(self):
        self.driver.find_element(*self.calendar_locators.ADD_EVENT_OPTION).click()

    def refresh_calendar(self):
        self.driver.find_element(*self.calendar_locators.REFRESH_BUTTON).click()

    def click_close_tutorial_popup(self):
        if self.common_actions.wait_for_element_visible(*self.calendar_locators.TUTORIAL_POPUP_CLOSE_BUTTON):
            self.common_actions.click_element(*self.calendar_locators.TUTORIAL_POPUP_CLOSE_BUTTON)
        return self

    def tap_branch_button(self):
        self.common_actions.wait_for_element_visible(*self.calendar_locators.BRANCH_BUTTON)
        self.common_actions.click_element(*self.calendar_locators.BRANCH_BUTTON)
        return self

    def tap_navigation_bar_settings_icon(self):
        self.common_actions.wait_for_element_visible(*self.calendar_locators.SETTINGS_OPTION_IN_NAVIGATION)
        self.common_actions.click_element(*self.calendar_locators.SETTINGS_OPTION_IN_NAVIGATION)
        self.common_actions.wait_for_element_disappear(*self.calendar_locators.SETTINGS_OPTION_IN_NAVIGATION)
        return self

    def verify_calendar_page(self):
        self.common_actions.wait_for_element_visible(*self.calendar_locators.SETTINGS_OPTION_IN_NAVIGATION)
        return self


