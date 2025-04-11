import random
import string
import time

from appium.webdriver.common.appiumby import AppiumBy

from pages.locators.android.navigation.record_locators import RecordLocators


class RecordPage:
      def __init__(self, driver):
          self.driver = driver
          self.record_locators = RecordLocators()
        
      def tap_records_option(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['records_nav_option']).click()
          time.sleep(0.5)
          return self

      def tap_recent_appointment(self):
          time.sleep(1)
          appointments = self.driver.find_elements(*self.record_locators.RECORD_ELEMENTS['appointment_number'])
          if appointments:
             random.choice(appointments).click()
          time.sleep(2)
          # back to record page
          self.driver.back()
          return self

      def switch_to_canceled_tab(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['recently_canceled_tab']).click()
          time.sleep(0.5)
          return self

      def tap_canceled_order(self):
          time.sleep(1)
          canceled_orders = self.driver.find_elements(*self.record_locators.RECORD_ELEMENTS['canceled_orders'])
          if canceled_orders:
             random.choice(canceled_orders).click()
          time.sleep(1)
          # back to record page
          self.driver.back()
        
          return self

      def click_billing_tab(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['billing_tab']).click()
          time.sleep(0.5)
          return self
    
      def click_filter_icon(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['filter_icon']).click()
          time.sleep(0.5)
          return self

      def click_filter_and_select_staff(self):
        
          random_staff = random.choice(self.record_locators.FILTER_STAFF_OPTIONS)
          self.driver.find_element(*random_staff).click()
          time.sleep(0.5)
        
          # click save button
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['save_button']).click()
          time.sleep(1)
          return self
      
      
      def claim_request_tab(self):
          time.sleep(1)
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['claim_request_tab']).click()
          return self

      def search_billing_number(self, number):
          search_icon = self.driver.find_element(
              *self.record_locators.RECORD_ELEMENTS['search_icon']
          )
          search_icon.click()
          time.sleep(1)
        
          search_field = self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['search_field'])
          search_field.send_keys(number)
          time.sleep(2)
          self.driver.back()
          return self

      def view_billing_details(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['view_details']).click()
          time.sleep(0.5)
          return self

      def export_details(self, is_expand=False):
          if is_expand:
              self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['expand_details']).click()
              time.sleep(3)
              self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['export_button']).click()
              self.navigate_back(times=3)
          else:
              time.sleep(1)
              self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['export_button']).click()
              time.sleep(2)
              self.navigate_back(times=2)
       
          return self
    
      def navigate_back(self, times):
          for _ in range(times):
              self.driver.back()
              time.sleep(0.5)
          return self

      def check_payment_method(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['check_payment']).click()
          time.sleep(1)
          self.navigate_back(times=2)
        
          return self


      def view_checkout_details(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['view_checkout']).click()
          time.sleep(0.5)

          return self
      
      def view_request_checkout(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['view_request_checkout']).click()
          time.sleep(0.5)

          return self

      def delete_checkout_request(self):
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['delete_request']).click()
          self.driver.find_element(*self.record_locators.RECORD_ELEMENTS['delete_checkout_confirm']).click()
          time.sleep(1)
          return self

      def return_to_calendar(self):
          self.navigate_back(times=1)
          return self