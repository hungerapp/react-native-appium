import time
import random

from appium.webdriver.common.appiumby import AppiumBy

from pages.locators.android.navigation.more.export_locators import ExportLocators
from pages.shared_components.common_use import CommonUseSection
from pages.android.calendar.calendar_page import CalendarPage

class ExportPage(CommonUseSection):
    def __init__(self, driver):
        self.driver = driver
        self.export_locators = ExportLocators()
        
    def click_export_available_time_slots(self):
        self.driver.find_element(*self.export_locators.EXPORT_AVAILABLE_TIME_SLOTS).click()
        time.sleep(0.5)
        return self
    
    def select_a_staff_member(self):
        self.driver.find_element(*self.export_locators.SERVICE_PERSONNEL_SECTION).click()
        self.driver.find_element(*self.export_locators.SERVICE_TESTING_PERSON).click()
        time.sleep(0.5)
        return self
    
    def select_a_service_item(self):
        time.sleep(0.5)
        self.driver.find_element(*self.export_locators.SERVICE_ITEM_SECTION).click()
        self.select_service()
        return self
      
    def select_a_month(self):
        time.sleep(0.5)
        self.driver.find_element(*self.export_locators.MONTH_SECTION).click()
        # randomly select a month
        month_option = random.choice(self.export_locators.MONTH_OPTION)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{month_option}")').click()
        time.sleep(0.5)
        return self 
      
    def export(self):
        self.driver.find_element(*self.export_locators.EXPORT_CALENDAR).click()
        time.sleep(0.5)
        return self
    
    def save_the_image(self):
        self.driver.find_element(*self.export_locators.SAVE_IMAGE).click()
        time.sleep(0.5)
        return self
      
    def click_on_the_text_tab(self):
        self.driver.find_element(*self.export_locators.TEXT_TAB).click()
        time.sleep(0.5)
        return self
      
    def select_a_date_range(self):
        self.driver.find_element(*self.export_locators.DATE_RANGE_SECTION).click()
        time.sleep(0.5)
          
        # click start section
        self.driver.find_element(*self.export_locators.START_SECTION).click()
        time.sleep(0.5)
           
        dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      
        random.choice(dates).click()
        
        # click end date block
        self.driver.find_element(*self.export_locators.END_DATE_BLOCK).click()
        time.sleep(1)
        
        # click right arrow multiple times
        clicks = random.randint(1, 5)
        for _ in range(clicks):
            self.driver.find_element(*self.export_locators.RIGHT_ARROW).click()
            time.sleep(0.5)
            
        # click end date again
        random.choice(dates).click()
        
        # click outside to close the date window
        size = self.driver.get_window_size()
        self.driver.execute_script('mobile: clickGesture', {
            'x': int(size['width'] * 0.5),  
            'y': int(size['height'] * 0.9)   
        })
        
        # click save button
        self.driver.find_element(*self.export_locators.SAVE_BUTTON).click()
        time.sleep(0.5)
        
        return self       
    
    def copy_the_text(self):
        self.driver.find_element(*self.export_locators.COPY_TEXT).click()
        time.sleep(0.5)
        return self
    
    def return_to_calendar_page(self):
        for _ in range(2):
            self.driver.find_element(*self.export_locators.BACK_BUTTON).click()
            time.sleep(0.5)
        return self
        
        