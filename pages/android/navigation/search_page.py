import time

from appium.webdriver.common.appiumby import AppiumBy


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        
    SEARCH_OPTION = (AppiumBy.ACCESSIBILITY_ID, '搜尋')
    SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜尋")')
    SEARCH_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("+886 972 205690").instance(0)')
    MEMBER_TAB = (AppiumBy.XPATH, '//android.view.View[@content-desc="會員"]/android.view.ViewGroup')
    MEMBER_RESULT = (AppiumBy.ACCESSIBILITY_ID, '+886 972 205690, 王貝克')
    NO_DATA_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("目前沒有資料")')  
    
    
    

    def tap_search_option(self):
        self.driver.find_element(*self.SEARCH_OPTION).click()
        return self
    
    def enter_search_name(self, name):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        time.sleep(1)
        search_input.send_keys(name)
        
        # press enter
        time.sleep(2)
        self.driver.press_keycode(66)
        return self
    
    def enter_search_number(self, number):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        time.sleep(1)
        search_input.send_keys(number)
        
        # press enter
        time.sleep(1.5)
        self.driver.press_keycode(66)
        return self
    
    def tap_search_result(self, is_member_tab=False):
        if not is_member_tab:
            self.driver.find_element(*self.SEARCH_RESULT).click()
            time.sleep(0.5)
            self.driver.back()
        else:
            self.driver.find_element(*self.MEMBER_RESULT).click()
            time.sleep(0.5)
            self.driver.back()
        
        time.sleep(1)
        return self
      
    
    def tap_member_tab(self):
        self.driver.find_element(*self.MEMBER_TAB).click()
        time.sleep(2)
        return self
    
    def scroll_down(self):
        self.driver.execute_script('mobile: scrollGesture', {
            'left': 100, 
            'top': 600, 
            'width': 200, 
            'height': 800,
            'direction': 'down',
            'percent': 0.95
        })
        return self
    
    def click_back(self):
        self.driver.back()
        time.sleep(0.5)

    
    def is_no_data_displayed(self):
        try:
            return self.driver.find_element(*self.NO_DATA_TEXT).is_displayed()
        except:
            return False