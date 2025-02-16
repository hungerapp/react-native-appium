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
    
    
    COUNTRY_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(3)')
    COUNTRY_CODE_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '+')]")
    CHANGED_COUNTRY_CODE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+")')
    COUNTRY_CODE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)') 
    SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入國家或號碼進行搜尋")')
    
    
    
    
    
    
    

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
