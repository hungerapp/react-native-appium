import time

from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

from pages.locators.android.login.login_locators import LoginLocators

class LoginPage:
  def __init__(self, driver):
      self.driver = driver
      self.login_locators = LoginLocators()
  
  def select_language(self):
      self.driver.find_element(*self.login_locators.LANGUAGE_SETTING_BUTTON).click()
      time.sleep(1)
      self.driver.find_element(*self.login_locators.CHINESE_LANGUAGE).click()
      self.driver.find_element(*self.login_locators.LANGUAGE_SAVE_BUTTON).click()

  def continue_to_login_page(self):
      language_setting_btn = self.driver.find_element(*self.login_locators.LANGUAGE_SETTING_BUTTON)
      contact_cs_btn = self.driver.find_element(*self.login_locators.CONTACT_CS_BUTTON)
      
      assert language_setting_btn.is_displayed(), "Language setting button not found"
      assert contact_cs_btn.is_displayed(), "Contact customer service button not found"
      assert self.driver.find_element(*self.login_locators.LOGIN_BUTTON) is not None, "Start using the app button not found"
      # click button move to login step
      #driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='開始使用').click()
      
  def click_contact_cs_button(self):
      self.driver.find_element(*self.login_locators.CONTACT_CS_BUTTON).click()
      time.sleep(1)
      self.driver.find_element(*self.login_locators.CONTACT_CS_BACK_BUTTON).click()

      
  def click_terms_and_conditions_button(self):
      self.driver.find_element(*self.login_locators.TERMS_AND_CONDITIONS_BUTTON).click()
  
  def click_tc_back_button(self):
      self.driver.find_element(*self.login_locators.TC_BACK_BUTTON).click()

  def click_privacy_button(self):
      self.driver.find_element(*self.login_locators.PRIVACY_BUTTON).click()

  def click_privacy_back_button(self):
      self.driver.find_element(*self.login_locators.PRIVACY_BACK_BUTTON).click()

  def click_login_button(self):
      self.driver.find_element(*self.login_locators.LOGIN_BUTTON).click()
  
  def enter_email(self, email):
      try:
          email_input = self.driver.find_element(*self.login_locators.EMAIL_INPUT)
          current_value = email_input.get_attribute("text")

          if current_value:
            self.driver.find_element(*self.login_locators.EMAIL_NEXT_BUTTON).click()
            return
      except NoSuchElementException:
        pass
      
      try:
          self.driver.find_element(*self.login_locators.EMAIL_INPUT).send_keys(email)
          self.driver.find_element(*self.login_locators.EMAIL_NEXT_BUTTON).click()
      except:
          pass

  def enter_ver_code(self, ver_code):
      self.driver.find_element(*self.login_locators.VER_CODE_INPUT).send_keys(ver_code)
      self.driver.find_element(*self.login_locators.VER_SUBMIT_BUTTON).click()

  def click_finish_button(self):
      self.driver.find_element(*self.login_locators.FINISH_BUTTON).click()

  def handle_save_alert(self):
      #self.driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Save'})
      pass

  def is_logged_in(self):
      try:
          # Check if login success popup is displayed
          time.sleep(1)
          pop_up = self.driver.find_element(*self.login_locators.LOGIN_SUCCESS_POPUP)
          assert pop_up.is_displayed(), "Login success popup not found"
      except NoSuchElementException:
          try:
              time.sleep(1)
              
              # Check if first time logged in finish btn  is displayed
              first_time_logged_in_page_finish_btn = self.driver.find_element(*self.login_locators.FINISH_BUTTON)
              if first_time_logged_in_page_finish_btn.is_displayed():
                  first_time_logged_in_page_finish_btn.click()
          except NoSuchElementException:
              pass
      
      return False
  
  def login_with_unregistered_email(self, email):
       self.click_login_button()
       time.sleep(1)
    
       try:
            email_input = self.driver.find_element(*self.login_locators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
               email_input.clear()

            email_input.send_keys(email)
            self.driver.find_element(*self.login_locators.EMAIL_NEXT_BUTTON).click()

            
       except NoSuchElementException as e:
            print(f"無法找到元素: {str(e)}")
            raise  
        
      
  def error_unregistered_message(self):
      error_element = self.driver.find_element(*self.login_locators.ERROR_UNREGISTERED_WINDOW_TITLE)
      assert error_element.is_displayed(), "Error unregistered window title not found"
      error_text = self.driver.find_element(*self.login_locators.ERROR_UNREGISTERED_WINDOW_MESSAGE).text.strip()
      self.driver.find_element(*self.login_locators.ERROR_UNREGISTERED_WINDOW_BUTTON).click()
      return error_text

  
  
  def get_email_error_message(self):
       try: 
            time.sleep(1)
            error_element = self.driver.find_element(*self.login_locators.ERROR_MESSAGE)
            return error_element.text.strip()
        
       except NoSuchElementException:
            return None
        
       
        
  def error_ver_window(self):
        try:
            error_element = self.driver.find_element(*self.login_locators.ERROR_WINDOW_TEXT)
            error_text = error_element.text.strip()
            self.driver.find_element(*self.login_locators.ERROR_RETRY_BUTTON).click()
            return error_text
            
        except NoSuchElementException:
            return None
       
  def click_login_cancel_button(self):
       login_button_cancel = self.driver.find_element(*self.login_locators.LOGIN_CANCEL_BUTTON)
       login_button_cancel.click()
       
 
  def login(self, email, ver_code=None):
        '''run the valid login process'''
        self.click_login_button()

        try:
            # find email input and clear
            email_input = self.driver.find_element(*self.login_locators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
                email_input.clear()
            
            # enter email
            email_input.send_keys(email)
            
            # click next button
            self.driver.find_element(*self.login_locators.EMAIL_NEXT_BUTTON).click()
            
            try:
                # verification code
                self.enter_ver_code(ver_code)
                
            except:
                self.click_finish_button()
            
            return True
            
        except NoSuchElementException as e:
            print(f"無法找到元素: {str(e)}")
            raise
        except Exception as e:
            print(f"發生未預期的錯誤: {str(e)}")
            raise

  def login_with_valid_email(self, email, ver_code=None):
        '''run the valid login process'''
        self.click_login_button()

        try:
            # find email input and clear
            email_input = self.driver.find_element(*self.login_locators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
                email_input.clear()
            
            # enter email
            email_input.send_keys(email)
            
            # click next button
            self.driver.find_element(*self.login_locators.EMAIL_NEXT_BUTTON).click()
            time.sleep(2)

        except Exception as e:
            print(f"發生未預期的錯誤: {str(e)}")
            raise
        
  def login_with_another_valid_email(self, email, ver_code=None):
        '''run the valid login process'''

        try:
            # find email input and clear
            email_input = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')
            current_value = email_input.get_attribute("text")
            if current_value:
                email_input.clear()
            
            # enter email
            email_input.send_keys(email)
            
            # click next button
            self.driver.find_element(*self.login_locators.EMAIL_NEXT_BUTTON).click()
            time.sleep(1)

        except Exception as e:
            print(f"發生未預期的錯誤: {str(e)}")
            raise
        
  def click_modify_email_button(self):
        time.sleep(0.5)
        self.driver.find_element(*self.login_locators.MODIFY_EMAIL_BUTTON).click()
        
  def is_verification_code_page(self):
      verification_code_page_title = self.driver.find_element(*self.login_locators.IS_VERIFICATION_CODE_PAGE_TITLE)
      return verification_code_page_title.is_displayed()

  def login_with_invalid_email(self, email):
        """run the invalid login process"""
        self.click_login_button()
        time.sleep(1)
    
        try:
            email_input = self.driver.find_element(*self.login_locators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
               email_input.clear()

            email_input.send_keys(email)

            
        except NoSuchElementException as e:
            print(f"無法找到元素: {str(e)}")
            raise  
        
  def login_with_invalid_ver_code(self, ver_code=None):
        """run the invalid login process"""
        time.sleep(2)
        self.enter_ver_code(ver_code)
        

########### Just for logout ###########
  def click_logout_button(self):
        time.sleep(1)
        self.driver.find_element(*self.login_locators.SETTING_ICON).click()
        self.driver.find_element(*self.login_locators.CLICK_WINDOW_LOGOUT_BUTTON).click()
        self.driver.find_element(*self.login_locators.SURE_TO_LOGOUT).click()
        
        
