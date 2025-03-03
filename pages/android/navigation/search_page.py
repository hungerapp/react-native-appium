import time

from appium.webdriver.common.appiumby import AppiumBy


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        
    SEARCH_OPTION = (AppiumBy.ACCESSIBILITY_ID, '搜尋')
    SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("搜尋")')
    SEARCH_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("王貝克 (Beck)").instance(0)')
    MEMBER_TAB = (AppiumBy.XPATH, '//android.view.View[@content-desc="會員"]/android.view.ViewGroup')
    MEMBER_RESULT = (AppiumBy.ACCESSIBILITY_ID, '+886 972 205690, 王貝克 先生 (Beck)')
    MEMBER_PASSPORT_BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    MEMBER_PASSPORT_BACK2_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    NO_DATA_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("目前沒有資料")')  
    BACK_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/com.horcrux.svg.SvgView')
    
    
    

    def tap_search_option(self):
        self.driver.find_element(*self.SEARCH_OPTION).click()
        return self
    
    def enter_search_number(self, number):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        time.sleep(1)
        search_input.send_keys(number)
        
        # press enter
        time.sleep(2)
        self.driver.press_keycode(66)
        return self
    
    def tap_search_result(self, is_member_tab=False):
        if not is_member_tab:
            self.driver.find_element(*self.SEARCH_RESULT).click()
            self.driver.find_element(*self.MEMBER_PASSPORT_BACK_BUTTON).click()
        else:
            self.driver.find_element(*self.MEMBER_RESULT).click()
            self.driver.find_element(*self.MEMBER_PASSPORT_BACK2_BUTTON).click()
        
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
        self.driver.find_element(*self.BACK_BUTTON).click()
        time.sleep(2)
        return self
    
    def is_no_data_displayed(self):
        try:
            return self.driver.find_element(*self.NO_DATA_TEXT).is_displayed()
        except:
            return False