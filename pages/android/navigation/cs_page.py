import time
import random
import string

from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

from pages.locators.android.navigation.cs_locators import CS_Locators


class CSPage():
      def __init__(self, driver):
          self.driver = driver
          self.cs_locators = CS_Locators()
  
      def click_cs_option(self):
          self.driver.find_element(*self.cs_locators.CS_OPTION).click()
          return self

      def click_message_section(self):
          self.driver.find_element(*self.cs_locators.MESSAGE_SECTION).click()
          time.sleep(0.5)
          return self
    
      def past_message(self):
          try:
            self.driver.find_element(*self.cs_locators.SEND_MESSAGE_TO_US_BUTTON).click()
            time.sleep(1)
            select_option = random.choice(self.cs_locators.CS_SEND_OPTIONS)
            self.driver.find_element(*select_option).click()
            time.sleep(1)
            self.driver.back()
            time.sleep(0.5)
            self.driver.back()
            time.sleep(0.5)
          except:
            self.driver.back()
            time.sleep(0.5)
        
      
        
      def click_recent_message_section(self):
          self.driver.find_element(*self.cs_locators.RECENT_MESSAGE_SECTION).click()
          return self
  
      def enter_message(self):
          time.sleep(1)  
          input_field = self.driver.find_element(*self.cs_locators.RECENT_MESSAGE_INPUT_FIELD)
            
          chars = string.ascii_letters + string.digits + '測試訊息'
          message = ''.join(random.choice(chars) for _ in range(10))
            
          input_field.click()
          time.sleep(0.5)
          input_field.send_keys(message)
          time.sleep(1)

          self.driver.find_element(*self.cs_locators.SEND_MESSAGE_BUTTON).click()
          time.sleep(1) 
        
          self.send_gif()
          self.message_back_button()
          return self
    
      def send_gif(self):
          time.sleep(0.5)
          self.driver.find_element(*self.cs_locators.GIF_BUTTON).click()
      
          # click first gif in the gif list
          self.driver.find_element(*self.cs_locators.GIF_LIST).click()
          self.driver.find_element(*self.cs_locators.SEND_GIF_BUTTON).click()
          return self
  
      def message_back_button(self):
          self.driver.find_element(*self.cs_locators.RECENT_MESSAGE_BACK_BUTTON).click()
          return self

      # HYPER LINK
  
      def tap_instagram_link(self):
          self.driver.find_element(*self.cs_locators.INSTAGRAM_LINK).click()
          time.sleep(1)
          self.driver.back()
          time.sleep(1)
          return self
  
      def tap_pricing_link(self):
          self.driver.find_element(*self.cs_locators.PRICING_LINK).click()
          time.sleep(1)
          self.driver.back()
          time.sleep(1)
          return self
    
      def tap_help_center_link(self):
          self.driver.find_element(*self.cs_locators.HELP_CENTER_LINK).click()
          time.sleep(1)
          self.driver.back()
          time.sleep(1)
          return self
  
      def meeting_link(self):
          scroll_command = ('new UiScrollable(new UiSelector().scrollable(true))'
                        '.scrollIntoView(new UiSelector().textContains("30分鐘"))')
        
          self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_command)
          self.driver.find_element(*self.cs_locators.MEETING_LINK).click()
          time.sleep(1)
          self.driver.back()
      
      
          # back again to go back to calendar page
          self.driver.back()
          return self