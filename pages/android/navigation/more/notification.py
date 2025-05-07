import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy


from pages.locators.android.navigation.more.notification_locators import NotificationLocators

class NotificationPage():
    def __init__(self, driver):
        self.driver = driver
        self.notification_locators = NotificationLocators()
        
    def tap_on_notification(self):
        self.driver.find_element(*self.notification_locators.NOTIFICATION).click()
        time.sleep(0.5)
        return self
    
    def click_view_latest_features_button(self):
        self.driver.find_element(*self.notification_locators.VIEW_LATEST_FEATURES_BUTTON).click()
        time.sleep(1)
        return self
    
    def redirect_and_back(self):
        self.driver.find_element(*self.notification_locators.BACK_TO_HOTCAKE_BUTTON).click()
        time.sleep(0.5)
        return self
        
    def click_any_notification(self):
        self.driver.find_element(*self.notification_locators.ANY_NOTIFICATION).click()
        time.sleep(0.5)
        return self
    
    def on_notification_page(self):
        try:
            time.sleep(0.5)
            assert self.driver.find_element(*self.notification_locators.NOTIFICATION_TITLE).is_displayed()
        except:
            raise Exception("Notification title is not displayed")
        return self
    
    def see_notification(self):
        try:
            assert self.driver.find_element(*self.notification_locators.NOTIFICATION_MESSAGE_TAG).is_displayed()
        except:
            raise Exception("Notification message tag is not displayed")
        return self
      
    def click_mark_all_as_read_button(self):
        self.driver.find_element(*self.notification_locators.MARK_ALL_AS_READ_BUTTON).click()
        time.sleep(0.5)
        return self
    
    def return_to_calendar_page(self):
        self.driver.find_element(*self.notification_locators.BACK_BUTTON).click()
        time.sleep(0.5)
        return self
    
    
    
    
    