import time
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


from pages.locators.android.navigation.more.allow_appointment_locators import AllowAppointmentLocators


class AllowAppointmentPage():
    def __init__(self, driver):
        self.driver = driver
        self.open_appointment_locators = AllowAppointmentLocators()
        
    def click_more_option(self):
        self.driver.find_element(*self.open_appointment_locators.MORE_OPTION).click()
        time.sleep(0.5)
        return self
    
    def click_allow_appointment_settings(self):
        self.driver.find_element(*self.open_appointment_locators.ALLOW_APPOINTMENT_SETTINGS).click()
        time.sleep(0.5)
        
    def click_toggle_and_select_open_times(self):
        # click edit personal icon
        self.driver.find_element(*self.open_appointment_locators.EDIT_PERSONAL_ICON).click()
        time.sleep(0.5)
        
        # click toggle
        self.driver.find_element(*self.open_appointment_locators.OPEN_APPOINTMENT_TOGGLE).click()
        time.sleep(0.5)
        
        # click open day section
        self.driver.find_element(*self.open_appointment_locators.OPEN_DAY_SECTION).click()
        time.sleep(0.5)
        
        # click target section date
        self.driver.find_element(*self.open_appointment_locators.TARGET_SECTION_DATE).click()
        selected_option = random.choice(self.open_appointment_locators.OPEN_DAY_OPTION)
        self.driver.find_element(*selected_option).click()
        time.sleep(1)
        
        # click target section time
        self.driver.find_element(*self.open_appointment_locators.TARGET_SECTION_TIME).click()
        # todo: 目前指定時間功能尚未開啟， 僅先測試點擊後確認
        self.driver.find_element(*self.open_appointment_locators.TARGET_SECTION_CONFIRM).click()
        
        # randomly select one option
        selected_month_option = random.choice(self.open_appointment_locators.OPEN_MONTH_OPTION)
        self.driver.find_element(*selected_month_option).click()
        time.sleep(1)
        
        # click save button
        self.driver.find_element(*self.open_appointment_locators.SAVE_BUTTON).click()
        
        return self
    
    def select_latest_reservation_time(self):
        self.driver.find_element(*self.open_appointment_locators.LATEST_RESERVATION_TIME).click()
        time.sleep(0.5)
        
        latest_reservation_time_option = random.choice(self.open_appointment_locators.LATEST_RESERVATION_TIME_OPTION)
        self.driver.find_element(*latest_reservation_time_option).click()
        time.sleep(1)
        
        return self
    
    def click_expand_advanced_settings(self):
        self.driver.find_element(*self.open_appointment_locators.EXPAND_ADVANCED_SETTINGS).click()
        time.sleep(0.5)
        
        return self
    
    def enter_quantity_selection(self):
        min_quantity = random.randint(1, 30)
        max_quantity = min_quantity + random.randint(1, 10)
        self.driver.find_element(*self.open_appointment_locators.MIN_QUANTITY_SECTION).send_keys(min_quantity)
        time.sleep(0.5)
        
        self.driver.find_element(*self.open_appointment_locators.MAX_QUANTITY_SECTION).send_keys(max_quantity)
        time.sleep(0.5)

        return self
    
    
    ##### OPEN TIME MANAGEMENT #####
    def click_open_time_tab(self):
        self.driver.find_element(*self.open_appointment_locators.OPEN_TIME_TAB).click()
        time.sleep(0.5)
        
        return self
    
    def select_display_date(self):
        self.driver.find_element(*self.open_appointment_locators.OPEN_CALENDAR_WINDOW).click()
        
        # click right arrow multiple times
        clicks = random.randint(1, 5)
        for _ in range(clicks):
            self.driver.find_element(*self.open_appointment_locators.ARROW_RIGHT).click()
            time.sleep(0.5)
        
        dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
        
        random.choice(dates).click()
        
        return self
    
    def add_new_open_time(self, num_slots=8):
        try:
            time.sleep(1)
            self.driver.find_element(*self.open_appointment_locators.ADD_NEW_OPEN_TIME).click()
            time.sleep(1)
            
            time_slots = self.driver.find_elements(*self.open_appointment_locators.TIME_SLOTS)
            
            # Make sure the number of slots to select is not greater than the number of available slots
            num_slots = min(num_slots, len(time_slots))
            
            selected_slots = random.sample(time_slots, num_slots)
            
            for slot in selected_slots:
                slot.click()
                time.sleep(0.5)
                
            self.driver.find_element(*self.open_appointment_locators.CLOSE_BUTTON).click()
            time.sleep(0.5)
        except:
            print("No add new open time button found")
        
        return self
    
    def select_specific_time_slot(self, time_str):
        """Select specific time slot from the calendar"""
        time_locators = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{time_str}']")
        self.driver.find_element(*time_locators).click()
        
        return self
    
    def get_calendar_dates(self):
        return self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
        
    
    def click_edit_then_copy_today(self):
        self.driver.find_element(*self.open_appointment_locators.EDIT_OPEN_TIME_BUTTON).click()
        time.sleep(0.5)
        
        # click copy today button
        self.driver.find_element(*self.open_appointment_locators.COPY_TODAY_BUTTON).click()
        time.sleep(0.5)
        
        selected_copy_option = random.choice(self.open_appointment_locators.COPY_TODAY_BUTTON_OPTIONS)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_copy_option}').click()
           
        if selected_copy_option == self.open_appointment_locators.COPY_TODAY_BUTTON_OPTIONS[0]:
            self.close_range()
            # randomly select multiple weekdays
            num_weekdays = random.randint(2, 4)
            selected_weekdays = random.sample(self.open_appointment_locators.WEEKDAYS, num_weekdays)
            for weekday in selected_weekdays:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, weekday).click()
                time.sleep(0.5)
        
            # click save button
            self.driver.find_element(*self.open_appointment_locators.SAVE_BUTTON).click()
            time.sleep(0.5)
        else:
            time.sleep(1)
            self.driver.find_element(*self.open_appointment_locators.RIGHT_ARROW).click()
            
            dates = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]')
            selected_dates = random.choices(dates, k=3)
            for date in selected_dates:
                date.click()
                time.sleep(0.5)
            self.driver.find_element(*self.open_appointment_locators.SAVE_BUTTON).click()
        return self
    
    def close_range(self):
        # click start section
            self.driver.find_element(*self.open_appointment_locators.START_SECTION).click()
            time.sleep(0.5)
           
            dates = self.get_calendar_dates()
            random.choice(dates).click()
        
            # click end date block
            self.driver.find_element(*self.open_appointment_locators.END_DATE_BLOCK).click()
            time.sleep(1)
        
            # click right arrow multiple times
            clicks = random.randint(1, 5)
            for _ in range(clicks):
                self.driver.find_element(*self.open_appointment_locators.RIGHT_ARROW).click()
                time.sleep(0.5)
            
            # click end date again
            random.choice(dates).click()
        
            # click outside to close the date window
            size = self.driver.get_window_size()
            self.driver.execute_script('mobile: clickGesture', {
                'x': int(size['width'] * 0.5),  
                'y': int(size['height'] * 0.9)   
            })
            
    
    def quick_close(self):
        self.driver.find_element(*self.open_appointment_locators.QUICK_CLOSE_BUTTON).click()
        time.sleep(0.5)
        
        quick_close_option = random.choice(self.open_appointment_locators.QUICK_CLOSE_BUTTON_OPTIONS)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{quick_close_option}').click()
        
        if quick_close_option == self.open_appointment_locators.QUICK_CLOSE_BUTTON_OPTIONS[0]:
            self.driver.find_element(*self.open_appointment_locators.CONFIRM_BUTTON).click()     
        elif quick_close_option == self.open_appointment_locators.QUICK_CLOSE_BUTTON_OPTIONS[1]:
            self.close_range()
            self.driver.find_element(*self.open_appointment_locators.SAVE_BUTTON).click()
        else:
            self.driver.find_element(*self.open_appointment_locators.CONFIRM_BUTTON).click()
        
        time.sleep(1)
        self.driver.find_element(*self.open_appointment_locators.CLOSE_BUTTON).click()
        return self
    
    
    ##### OPEN ITEMS MANAGEMENT #####
    def click_open_items_tab(self):
        self.driver.find_element(*self.open_appointment_locators.OPEN_ITEMS_TAB).click()
        time.sleep(0.5)
        return self
    
    def select_main_item(self):
        self.driver.find_element(*self.open_appointment_locators.MAIN_ITEM_SECTION).click()
        time.sleep(0.5)
        
        self.is_item_selection()
        return self
    
    def is_item_selection(self, is_item_selection=False):
        # clear all selected items
        self.driver.find_element(*self.open_appointment_locators.CLEAR_ALL_BUTTON).click()
        time.sleep(0.5)
        
        try:
            tab_container = self.driver.find_element(*self.open_appointment_locators.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location

            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
            y = location['y'] + int(size['height'] * 0.5)

            max_attempts = 3
            found_target = False

            for _ in range(max_attempts):
                self.driver.swipe(start_x, y, end_x, y, 100)
                time.sleep(0.5)
                try:
                    auto_test_tab = self.driver.find_element(*self.open_appointment_locators.AUTO_TEST_TAB)
                    if auto_test_tab.is_displayed():
                        auto_test_tab.click()
                        found_target = True
                        break
                except NoSuchElementException:
                    continue

            if not found_target:
                print("Could not find AUTO_TEST_TAB after maximum attempts")
                return self

        except Exception as e:
            print(f"Error swiping tabs: {str(e)}")
            return self
        
        # choose the testing option below the item
        try:
            if not is_item_selection:
                self.driver.find_element(*self.open_appointment_locators.TESTING1_ITEM_SELECT).click()
                self.driver.find_element(*self.open_appointment_locators.TESTING2_ITEM_SELECT).click()
            else:
                self.driver.find_element(*self.open_appointment_locators.TESTING3_ITEM_SELECT).click()
                self.driver.find_element(*self.open_appointment_locators.TESTING4_ITEM_SELECT).click()
                self.driver.find_element(*self.open_appointment_locators.TESTING5_ITEM_SELECT).click()
                
            time.sleep(1)
            self.driver.find_element(*self.open_appointment_locators.SERVICE_CONFIRM_BUTTON).click()
        except Exception as e:
            print(f"Error selecting services: {str(e)}")
        
       
    
    def select_online_reservation_type(self):
        self.driver.find_element(*self.open_appointment_locators.ONLINE_RESERVATION_TYPE_SECTION).click()
        selected_option = random.choice(self.open_appointment_locators.ONLINE_RESERVATION_TYPE_OPTION)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f'{selected_option}').click()
        time.sleep(0.5)
        return self
    
    def select_add_on_service_items(self):
        self.driver.find_element(*self.open_appointment_locators.ADD_ON_SERVICE_ITEMS_SECTION).click()
        time.sleep(0.5)
        
        self.is_item_selection(is_item_selection=True)
        return self
    
    def return_to_calendar_page(self):
        for _ in range(2):
            self.driver.find_element(*self.open_appointment_locators.CLOSE_BUTTON).click()
            time.sleep(0.5)
        return self
        
    