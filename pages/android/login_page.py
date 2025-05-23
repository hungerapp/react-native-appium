import time

from selenium.common.exceptions import NoSuchElementException


from pages.locators.android.login.login_locators import LoginLocators
from pages.shared_components.common_action import CommonActions

class LoginPage(CommonActions):
  def __init__(self, driver):
      super().__init__(driver)
  
  def select_language(self):
      self.wait_for_element_visible(*LoginLocators.LANGUAGE_SETTING_BUTTON)
      self.click_element(*LoginLocators.LANGUAGE_SETTING_BUTTON)
      self.wait_for_element_visible(*LoginLocators.CHINESE_LANGUAGE)
      self.click_element(*LoginLocators.CHINESE_LANGUAGE)
      self.wait_for_element_visible(*LoginLocators.LANGUAGE_SAVE_BUTTON)
      self.click_element(*LoginLocators.LANGUAGE_SAVE_BUTTON)

  def continue_to_login_page(self):
      assert self.is_element_visible(*LoginLocators.LANGUAGE_SETTING_BUTTON), "Language setting button not found"
      assert self.is_element_visible(*LoginLocators.CONTACT_CS_BUTTON), "Contact customer service button not found"
      assert self.is_element_visible(*LoginLocators.LOGIN_BUTTON), "Start using the app button not found"

  def click_contact_cs_button(self):
      self.wait_for_element_clickable(*LoginLocators.CONTACT_CS_BUTTON)
      self.click_element(*LoginLocators.CONTACT_CS_BUTTON)
      try:
          self.click_element(*LoginLocators.CONTACT_CS_BACK_BUTTON)
      except:
          self.driver.back()
      
  def click_terms_and_conditions_button(self):
      self.wait_for_element_visible(*LoginLocators.TERMS_AND_CONDITIONS_BUTTON)
      self.click_element(*LoginLocators.TERMS_AND_CONDITIONS_BUTTON)

  def click_tc_back_button(self):
      self.wait_for_element_visible(*LoginLocators.TC_BACK_BUTTON)
      self.click_element(*LoginLocators.TC_BACK_BUTTON)

  def click_privacy_button(self):
      self.wait_for_element_visible(*LoginLocators.PRIVACY_BUTTON)
      self.click_element(*LoginLocators.PRIVACY_BUTTON)

  def click_privacy_back_button(self):
      self.wait_for_element_visible(*LoginLocators.PRIVACY_BACK_BUTTON)
      self.click_element(*LoginLocators.PRIVACY_BACK_BUTTON)

  def click_login_button(self):
      self.wait_for_element_clickable(*LoginLocators.LOGIN_BUTTON)
      self.click_element(*LoginLocators.LOGIN_BUTTON)

  def enter_email(self, email):
      try:
          email_input = self.find_element(*LoginLocators.EMAIL_INPUT)
          current_value = email_input.get_attribute("text")

          if current_value:
            self.click_element(*LoginLocators.EMAIL_NEXT_BUTTON)
            return
      except NoSuchElementException:
        pass

      try:
          self.send_keys_to_element(*LoginLocators.EMAIL_INPUT, email)
          self.click_element(*LoginLocators.EMAIL_NEXT_BUTTON)
      except:
          pass

  def enter_ver_code(self, ver_code):
          self.wait_for_element_visible(*LoginLocators.IS_VERIFICATION_CODE_PAGE_TITLE)
          ver_code_element = self.find_element(*LoginLocators.VER_CODE_INPUT)
          ver_code_element.send_keys(ver_code)
          self.wait_for_element_clickable(*LoginLocators.VER_SUBMIT_BUTTON)
          self.click_element(*LoginLocators.VER_SUBMIT_BUTTON)

  def click_finish_button(self):
      self.wait_for_element_clickable(*LoginLocators.FINISH_BUTTON)
      self.click_element(*LoginLocators.FINISH_BUTTON)

  def handle_save_alert(self):
      #self.driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Save'})
      pass

  def is_logged_in(self):
      try:
          # Check if the login success popup is displayed
          pop_up = self.is_element_visible(*LoginLocators.LOGIN_SUCCESS_POPUP)
          assert pop_up, "Login success popup not found"
          time.sleep(2)
          self.driver.find_element(*LoginLocators.FINISH_BUTTON).click()
          return None
      except NoSuchElementException:
          return False

  def login_with_unregistered_email(self, email):
       self.click_login_button()

       try:
            email_input = self.find_element(*LoginLocators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
               email_input.clear()

            self.send_keys_to_element(*LoginLocators.EMAIL_INPUT, email)
            self.click_element(*LoginLocators.EMAIL_NEXT_BUTTON)


       except NoSuchElementException as e:
            print(f"無法找到元素: {str(e)}")
            raise  

  def error_unregistered_message(self):
      error_element = self.get_element_text(*LoginLocators.ERROR_UNREGISTERED_WINDOW_TITLE)
      assert error_element, "Error unregistered window title not found"
      error_text = self.get_element_text(*LoginLocators.ERROR_UNREGISTERED_WINDOW_MESSAGE)
      self.click_element(*LoginLocators.ERROR_UNREGISTERED_WINDOW_BUTTON)
      return error_text.strip()



  def get_email_error_message(self):
       try: 
            error_element = self.get_element_text(*LoginLocators.ERROR_MESSAGE)
            return error_element.strip()

       except NoSuchElementException:
            return None

  def error_ver_window(self):
        try:
            error_element = self.get_element_text(*LoginLocators.ERROR_WINDOW_TEXT)
            self.click_element(*LoginLocators.ERROR_RETRY_BUTTON)
            return error_element.strip()
            
        except NoSuchElementException:
            return None

  def click_login_cancel_button(self):
       self.wait_for_element_visible(*LoginLocators.LOGIN_CANCEL_BUTTON)
       self.click_element(*LoginLocators.LOGIN_CANCEL_BUTTON)
       
 
  def login(self, email, ver_code=None):
        """run the valid login process"""
        self.click_login_button()

        try:
            # find email input and clear
            self.wait_for_element_visible(*LoginLocators.EMAIL_INPUT)
            email_input = self.find_element(*LoginLocators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
                email_input.clear()

            # enter email
            self.send_keys_to_element(*LoginLocators.EMAIL_INPUT, email)

            current_value = email_input.get_attribute("text")
            if current_value:
                pass

            # click next button
            self.wait_for_element_clickable(*LoginLocators.EMAIL_NEXT_BUTTON)
            self.click_element(*LoginLocators.EMAIL_NEXT_BUTTON)

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
            self.wait_for_element_visible(*LoginLocators.EMAIL_INPUT)
            email_input = self.find_element(*LoginLocators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
                email_input.clear()

            # enter email
            self.send_keys_to_element(*LoginLocators.EMAIL_INPUT, email)
            
            # click next button
            self.wait_for_element_clickable(*LoginLocators.EMAIL_NEXT_BUTTON)
            self.click_element(*LoginLocators.EMAIL_NEXT_BUTTON)

        except Exception as e:
            print(f"發生未預期的錯誤: {str(e)}")
            raise

  def login_with_another_valid_email(self, email, ver_code=None):
        '''run the valid login process'''

        try:
            # find email input and clear
            self.wait_for_element_visible(*LoginLocators.EMAIL_INPUT)
            email_input = self.find_element(*LoginLocators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
                email_input.clear()

            # enter email
            self.send_keys_to_element(*LoginLocators.EMAIL_INPUT, email)
            
            # click next button
            self.wait_for_element_clickable(*LoginLocators.EMAIL_NEXT_BUTTON)
            self.click_element(*LoginLocators.EMAIL_NEXT_BUTTON)

        except Exception as e:
            print(f"發生未預期的錯誤: {str(e)}")
            raise

  def click_modify_email_button(self):
        self.wait_for_element_visible(*LoginLocators.MODIFY_EMAIL_BUTTON)
        self.click_element(*LoginLocators.MODIFY_EMAIL_BUTTON)

  def is_verification_code_page(self):
      verification_code_page_title = self.is_element_visible(*LoginLocators.IS_VERIFICATION_CODE_PAGE_TITLE)
      return verification_code_page_title

  def login_with_invalid_email(self, email):
        """run the invalid login process"""
        self.click_login_button()

        try:
            self.is_element_visible(*LoginLocators.EMAIL_INPUT)
            email_input = self.find_element(*LoginLocators.EMAIL_INPUT)
            current_value = email_input.get_attribute("text")
            if current_value:
               email_input.clear()

            self.send_keys_to_element(*LoginLocators.EMAIL_INPUT, email)

            
        except NoSuchElementException as e:
            print(f"無法找到元素: {str(e)}")
            raise  
        
  def login_with_invalid_ver_code(self, ver_code=None):
        """run the invalid login process"""
        self.enter_ver_code(ver_code)
        

########### Just for logout ###########
  def click_logout_button(self):
        self.click_element(*LoginLocators.SETTING_ICON)
        self.click_element(*LoginLocators.CLICK_WINDOW_LOGOUT_BUTTON)
        self.click_element(*LoginLocators.SURE_TO_LOGOUT)
        
        
