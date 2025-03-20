import time
import random
import string

from pages.locators.android.navigation.more.brand_setting_locators import BrandSettingLocators


class BrandSettingPage:
  def __init__(self, driver):
      self.driver = driver
      self.brand_setting_locators = BrandSettingLocators()
  
  def tap_more_option(self):
      self.driver.find_element(*self.brand_setting_locators.MORE_OPTION).click()
      time.sleep(0.5)
      return self

  def tap_brand_settings(self):
      self.driver.find_element(*self.brand_setting_locators.BRAND_SETTINGS).click()
      time.sleep(0.5)
      return self

  def edit_brand_name(self):
      brand_name_field = self.driver.find_element(*self.brand_setting_locators.BRAND_NAME)
      brand_name_field.clear()
      input_field = self.driver.find_element(*self.brand_setting_locators.BRAND_TITLE_INPUT)
      
      # generate random brand name
      brand_name = "hunger Salon-staging" +''.join(random.choices(string.ascii_letters + string.digits, k=4))
      input_field.send_keys(brand_name)
      time.sleep(0.5)
      return self

  def edit_brand_description(self, description):
      brand_description_field = self.driver.find_element(*self.brand_setting_locators.BRAND_DESCRIPTION)
      brand_description_field.click()
      
      # clear brand description
      self.driver.find_element(*self.brand_setting_locators.CLEAR_BUTTON).click()
      
      # input brand description
      time.sleep(0.5)
      input_field_modal = self.driver.find_element(*self.brand_setting_locators.MODAL_INPUT)
      input_field_modal.send_keys(description)
      self.driver.find_element(*self.brand_setting_locators.MODAL_SAVE_BUTTON).click()
      time.sleep(1)
      return self

  def save_changes(self):
      self.driver.find_element(*self.brand_setting_locators.SAVE_BUTTON).click()
      time.sleep(0.5)
      return self
    
    
    