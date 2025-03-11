import time
import random
import string

from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CSPage():
  def __init__(self, driver):
    self.driver = driver
    
  # locator
  CS_OPTION = (AppiumBy.ACCESSIBILITY_ID, "客服")
  MESSAGE_SECTION = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[1]/android.view.View')
  PAST_MESSAGE = [ 
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Profile image for Fin").instance(0)'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Profile image for Fin").instance(1)'),
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Profile image for Fin").instance(2)')
  ]
  SEND_MESSAGE_TO_US_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("傳訊息給我們")')
  CS_SEND_OPTIONS = [
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("方案與價格")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新手教學")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("通知與提醒")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LINE官方帳號")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("😃 呼叫夯客教練")')
  ]
  MESSAGE_BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button")')
  RECENT_MESSAGE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Profile image for Fin")')
  RECENT_MESSAGE_BACK_BUTTON = (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button')
  RECENT_MESSAGE_INPUT_FIELD = (AppiumBy.XPATH, '//android.widget.EditText')
  SEND_MESSAGE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')
  GIF_BUTTON = (AppiumBy.XPATH, '//android.widget.EditText/android.widget.Button[1]')
  GIF_LIST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("(附圖)").instance(0)')
  SEND_GIF_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Send')
  
  # hyper link
  INSTAGRAM_LINK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("追蹤夯客Instagram")')
  PRICING_LINK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("價格與方案")')
  HELP_CENTER_LINK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("幫助中心")')
  MEETING_LINK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("30分鐘")')
  
  
  
  
  
  
  
  def click_cs_option(self):
      self.driver.find_element(*self.CS_OPTION).click()
      return self

  def click_message_section(self):
      self.driver.find_element(*self.MESSAGE_SECTION).click()
      time.sleep(0.5)
      return self
    
  def past_message(self):
      random_message = random.choice(self.PAST_MESSAGE)
      try:
        self.driver.find_element(*self.SEND_MESSAGE_TO_US_BUTTON).click()
        time.sleep(1)
        select_option = random.choice(self.CS_SEND_OPTIONS)
        self.driver.find_element(*select_option).click()
        time.sleep(1)
      except Exception as e:
        self.driver.find_element(*random_message).click()
        time.sleep(1)
      
      self.driver.find_element(*self.MESSAGE_BACK_BUTTON).click()
      
      # click back button to go back to the cs page again
      self.driver.find_element(*self.MESSAGE_BACK_BUTTON).click()
      
        
  def click_recent_message_section(self):
      self.driver.find_element(*self.RECENT_MESSAGE_SECTION).click()
      return self
  
  def enter_message(self):
      time.sleep(1)  
      input_field = self.driver.find_element(*self.RECENT_MESSAGE_INPUT_FIELD)
            
      chars = string.ascii_letters + string.digits + '測試訊息'
      message = ''.join(random.choice(chars) for _ in range(10))
            
      input_field.click()
      time.sleep(0.5)
      input_field.send_keys(message)
      time.sleep(1)

      self.driver.find_element(*self.SEND_MESSAGE_BUTTON).click()
      time.sleep(1) 
        
      self.send_gif()
      self.message_back_button()
      return self
    
  def send_gif(self):
      time.sleep(0.5)
      self.driver.find_element(*self.GIF_BUTTON).click()
      
      # click first gif in the gif list
      self.driver.find_element(*self.GIF_LIST).click()
      self.driver.find_element(*self.SEND_GIF_BUTTON).click()
      return self
  
  def message_back_button(self):
      self.driver.find_element(*self.RECENT_MESSAGE_BACK_BUTTON).click()
      return self

  # HYPER LINK
  
  def tap_instagram_link(self):
      self.driver.find_element(*self.INSTAGRAM_LINK).click()
      time.sleep(1)
      self.driver.back()
      time.sleep(1)
      return self
  
  def tap_pricing_link(self):
      self.driver.find_element(*self.PRICING_LINK).click()
      time.sleep(1)
      self.driver.back()
      time.sleep(1)
      return self
    
  def tap_help_center_link(self):
      self.driver.find_element(*self.HELP_CENTER_LINK).click()
      time.sleep(1)
      self.driver.back()
      time.sleep(1)
      return self
  
  def meeting_link(self):
      scroll_command = ('new UiScrollable(new UiSelector().scrollable(true))'
                        '.scrollIntoView(new UiSelector().textContains("30分鐘"))')
        
      self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_command)
      self.driver.find_element(*self.MEETING_LINK).click()
      time.sleep(1)
      self.driver.back()
      
      
      # back again to go back to calendar page
      self.driver.back()
      return self