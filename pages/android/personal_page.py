import time

from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy


class PersonalPage:
  
  def __init__(self, driver):
    self.driver = driver
    
    
  # View basic personal information 
  PROFILE_PICTURE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')
  USERNAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("(?i)[\\\\w\\\\p{L}]+")')
  GREETING_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(".*保持好心情.*|.*開始美好.*|.*好好休息.*")')
  EMAIL_ADDRESS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(".*@.*")')


  # View brand list
  BRAND_LIST_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("品牌列表")')
  BRAND_HUNGER_SALON_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("hunger Salon-staging")')
  BRAND_HUNGER_SALON_PROFILE_PICTURE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
  BRANDS_PRO = (AppiumBy.ACCESSIBILITY_ID, 'Pro 分店, 品牌管理員')
  BRAND_STAR = (AppiumBy.ACCESSIBILITY_ID, 'Star分店, 品牌管理員')
  BRANCH_FREE = (AppiumBy.ACCESSIBILITY_ID, 'Free分店, 品牌管理員')
  
  # Quick functions
  ALL_RESERVATIONS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '所有預約')
  GOOGLE_CALENDAR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Google 日曆')
  PUSH_NOTIFICATION_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '推播設定')
  
  # Manage account settings
  SETTINGS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(18)')
  SETTINGS_POPUP = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(7)')
  ACCOUNT_SETTINGS_OPTION = (AppiumBy.ACCESSIBILITY_ID, '帳號設定')
  LANGUAGE_SETTINGS_OPTION = (AppiumBy.ACCESSIBILITY_ID, '語言設定')
  #LOGOUT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, '語言設定')
  
  
  # Check if Basic elements are displayed
  def is_profile_picture_displayed(self):
    return self.driver.find_element(*self.PROFILE_PICTURE)
  
  def is_username_displayed(self):
    return self.driver.find_element(*self.USERNAME)
  
  def get_greeting_message_message(self):
    elements = self.driver.find_elements(*self.GREETING_MESSAGE)
    for e in elements:
      text = e.text
      if "早安" in text or "保持好心情" in text or "晚安" in text:
          print("find greeting message", text) 
          return e.text 
    return None
  
  def is_email_address_displayed(self):
    return self.driver.find_element(*self.EMAIL_ADDRESS)
  
  
  
  # Check if Brand list elements are displayed
  def is_brand_list_title_displayed(self):
    return self.driver.find_element(*self.BRAND_LIST_TITLE)
  
  def is_brand_hunger_salon_title_displayed(self):
    return self.driver.find_element(*self.BRAND_HUNGER_SALON_TITLE)
  
  def is_brand_hunger_salon_profile_picture_displayed(self):
    return self.driver.find_element(*self.BRAND_HUNGER_SALON_PROFILE_PICTURE)
  
  def is_brands_pro_displayed(self):
    return self.driver.find_element(*self.BRANDS_PRO)
  
  def is_brand_star_displayed(self):
    return self.driver.find_element(*self.BRAND_STAR)
  
  def is_branch_free_displayed(self):
    return self.driver.find_element(*self.BRANCH_FREE)
