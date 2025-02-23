import random
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class CommonUseSection:
    GENDER_OPTIONS = {
        "男": (AppiumBy.ACCESSIBILITY_ID, "男"),
        "女": (AppiumBy.ACCESSIBILITY_ID, "女"),
        "其他": (AppiumBy.ACCESSIBILITY_ID, "其他")
    }
    BIRTHDAY_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("生日")')
    CALENDAR_WINDOW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/pickers")')
  
    
    COUNTRY_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(3)')
    COUNTRY_CODE_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '+')]")
    CHANGED_COUNTRY_CODE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+")')
    COUNTRY_CODE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)') 
    SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入國家或號碼進行搜尋")')
    
    
    
    
    SERVICE_PERSON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    SERVICE_TESTING_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SERVICE_PAGE_TOGGLE_SWITCH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(31)')
    SERVICE_PAGE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)')
    
    SERVICE_PERSONNEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    QA_TEST_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SELECT_ALL_OPTION = (AppiumBy.ACCESSIBILITY_ID, '全部選取')
    PERSONNEL_OPTIONS = [
        (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲'),
        (AppiumBy.ACCESSIBILITY_ID, 'Bella #美甲'),
        # Add more personnel options as needed
    ]
    PERSONNEL_SAVE_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    
    

    def __init__(self, driver):
        self.driver = driver

    def select_random_gender(self):
        """Select random gender"""
        try:
            gender = random.choice(list(self.GENDER_OPTIONS.keys()))
            self.driver.find_element(*self.GENDER_OPTIONS[gender]).click()
            time.sleep(0.5)
            return gender
        except Exception as e:
            print(f"Select gender error: {str(e)}")
            raise
        
    def select_random_date(self):
        """Random scroll to select date"""
        try:
            # Click birthday field to open date picker
            self.driver.find_element(*self.BIRTHDAY_FIELD).click()
        
            # Get date picker window
            calendar_window = self.driver.find_element(*self.CALENDAR_WINDOW)
            window_rect = calendar_window.rect
        
            # calculate year, month, day x coordinates
            year_x = window_rect['x'] + (window_rect['width'] * 0.17)  # left side year field
            month_x = window_rect['x'] + (window_rect['width'] * 0.5)  # middle month field
            day_x = window_rect['x'] + (window_rect['width'] * 0.83)   # right side day field
        
            # calculate y coordinate center point
            center_y = window_rect['y'] + window_rect['height'] / 2
        
            # random scroll each field
            date_columns = [
            {"name": "年", "x": year_x},
            {"name": "月", "x": month_x},
            {"name": "日", "x": day_x}
            ]
        
            for column in date_columns:
                swipe_times = random.randint(3, 6)
                for _ in range(swipe_times):
                    self._perform_random_swipe(
                    start_x=column["x"],
                    start_y=center_y,
                    max_offset=50, # limit horizontal random offset
                    )
                    time.sleep(0.5)
        
            # click confirm
            self.driver.find_element(*self.CONFIRM_BUTTON).click()
        
            # Return updated date text
            return self.driver.find_element(*self.BIRTHDAY_FIELD).text
        
        except Exception as e:
            print(f"Select date error: {str(e)}")
            raise
        
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
    
    # only select one service person
    def select_service_person(self):
        self.driver.find_element(*self.SERVICE_PERSON).click()
        
        # click toggle switch 
        time.sleep(1.5)
        self.driver.find_element(*self.SERVICE_PAGE_TOGGLE_SWITCH).click()
        
        # select service testing person
        service_testing_person = self.driver.find_element(*self.SERVICE_TESTING_PERSON)
        if service_testing_person:
            service_testing_person.click()
            
        # click save button
        self.driver.find_element(*self.SERVICE_PAGE_SAVE_BTN).click()
        
        return self
    
    # select multiple service person
    def select_service_multiple_personnel(self, single_choice):
        self.driver.find_element(*self.SERVICE_PERSONNEL).click()
        # Choose single or multiple selection as needed
        if single_choice:
            self.driver.find_element(*self.QA_TEST_PERSONNEL).click()
        else:
            selected_options = random.sample(self.PERSONNEL_OPTIONS, 2)
            for option in selected_options:
                self.driver.find_element(*option).click()
                
        self.driver.find_element(*self.PERSONNEL_SAVE_BUTTON).click()
        time.sleep(0.5)
        return self
    
    