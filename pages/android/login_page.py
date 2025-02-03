import time

from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
  def __init__(self, driver):
      self.driver = driver

  login_button = (AppiumBy.ACCESSIBILITY_ID, '開始使用')
  email_input = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
  login_cancel_button = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView')
  email_next_button = (AppiumBy.ACCESSIBILITY_ID, '下一步')
  modify_email_button = (AppiumBy.ACCESSIBILITY_ID, '修改信箱')
  is_verification_code_page_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("驗證通行碼")')
  ver_code_input = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
  ver_submit_button = (AppiumBy.ACCESSIBILITY_ID, '送出')
  finish_button = (AppiumBy.ACCESSIBILITY_ID, '完成')
  login_success_popup = (AppiumBy.ACCESSIBILITY_ID, '登入成功')
  error_message = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 請填寫正確的電子郵件。")')
  error_window_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請檢查驗證通行碼是否輸入正確")')
  error_retry_button = (AppiumBy.ACCESSIBILITY_ID, '好')
 


  ### Logout ###
  setting_icon = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
  click_window_logout_button = (AppiumBy.ACCESSIBILITY_ID, '登出')
  sure_to_logout = (AppiumBy.ACCESSIBILITY_ID, '確定')



  def click_login_button(self):
      self.driver.find_element(*self.login_button).click()
  
  def enter_email(self, email):
      try:
          #self.driver.find_element(*self.email_input).clear()
          email_input = self.driver.find_element(*self.email_input)
          current_value = email_input.get_attribute("text")

          if current_value:
            self.driver.find_element(*self.email_next_button).click()
            return
      except NoSuchElementException:
        pass
      
      try:
          self.driver.find_element(*self.email_input).send_keys(email)
          self.driver.find_element(*self.email_next_button).click()
      except:
          pass

  def enter_ver_code(self, ver_code):
      #time.sleep(1)
      self.driver.find_element(*self.ver_code_input).send_keys(ver_code)
      self.driver.find_element(*self.ver_submit_button).click()

  def click_finish_button(self):
      self.driver.find_element(*self.finish_button).click()

  def handle_save_alert(self):
      self.driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': 'Save'})

  def is_logged_in(self):
      try:
          # Check if login success popup is displayed
          pop_up = self.driver.find_element(*self.login_success_popup)
          if pop_up.is_displayed():
              try:
                  # Handle push notification alert
                  android_push_notification = self.driver.find_element(
                      by=AppiumBy.XPATH, 
                      value='//android.widget.Button[@resource-id="android:id/button1"]'
                  )
                  android_push_notification.click()
              except NoSuchElementException:
                  pass
              return True
      except NoSuchElementException:
          try:
              time.sleep(1)
              
              # Check if first time logged in finish btn  is displayed
              first_time_logged_in_page_finish_btn = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='完成')
              if first_time_logged_in_page_finish_btn.is_displayed():
                  first_time_logged_in_page_finish_btn.click()

                   # Handle push notification alert
                  android_push_notification = self.driver.find_element(
                      by=AppiumBy.XPATH, 
                      value='//android.widget.Button[@resource-id="android:id/button1"]'
                  )
                  android_push_notification.click()
                  return True
          except NoSuchElementException:
              pass
      
      return False
   
      
  
  
  def get_email_error_message(self):
       try: 
            time.sleep(1)
            error_element = self.driver.find_element(*self.error_message)
            return error_element.text.strip()
        
       except NoSuchElementException:
            return None
        
       
        
  def error_ver_window(self):
        try:
            error_element = self.driver.find_element(*self.error_window_text)
            error_text = error_element.text.strip()
            self.driver.find_element(*self.error_retry_button).click()
            return error_text
            
        except NoSuchElementException:
            return None
       
  def click_login_cancel_button(self):
       login_button_cancel = self.driver.find_element(*self.login_cancel_button)
       login_button_cancel.click()
       
 
  def login(self, email, ver_code=None):
        '''run the valid login process'''
        self.click_login_button()

        try:
            # find email input and clear
            email_input = self.driver.find_element(*self.email_input)
            current_value = email_input.get_attribute("text")
            if current_value:
                email_input.clear()
            
            # enter email
            email_input.send_keys(email)
            
            # click next button
            self.driver.find_element(*self.email_next_button).click()
            
            try:
                self.click_finish_button()
            except:
                # verification code
                self.enter_ver_code(ver_code)
            
            # handle for ios login
            #self.handle_save_alert()
            time.sleep(3)
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
            email_input = self.driver.find_element(*self.email_input)
            current_value = email_input.get_attribute("text")
            if current_value:
                email_input.clear()
            
            # enter email
            email_input.send_keys(email)
            
            # click next button
            self.driver.find_element(*self.email_next_button).click()
            time.sleep(1)

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
            self.driver.find_element(*self.email_next_button).click()
            time.sleep(1)

        except Exception as e:
            print(f"發生未預期的錯誤: {str(e)}")
            raise
        
  def click_modify_email_button(self):
        self.driver.find_element(*self.modify_email_button).click()
        
  def is_verification_code_page(self):
      verification_code_page_title = self.driver.find_element(*self.is_verification_code_page_title)
      return verification_code_page_title.is_displayed()

  def login_with_invalid_email(self, email):
        """run the invalid login process"""
        self.click_login_button()
    
        try:
            email_input = self.driver.find_element(*self.email_input)
            current_value = email_input.get_attribute("text")
            if current_value:
               email_input.clear()

            email_input.send_keys(email)

            
        except NoSuchElementException as e:
            print(f"無法找到元素: {str(e)}")
            raise  
        
  def login_with_invalid_ver_code(self, ver_code=None):
        """run the invalid login process"""
        self.enter_ver_code(ver_code)
        

########### Just for logout ###########
  def click_logout_button(self):
        self.driver.find_element(*self.setting_icon).click()
        self.driver.find_element(*self.click_window_logout_button).click()
        self.driver.find_element(*self.sure_to_logout).click()
        
        
