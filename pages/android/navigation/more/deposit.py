import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy

from pages.locators.android.navigation.more.deposit_locators import DepositLocators
from pages.android.create.create_checkout_page import CreateCheckoutPage


class DepositPage():
    def __init__(self, driver):
        self.driver = driver
        self.deposit_locators = DepositLocators()
        self.create_checkout_page = CreateCheckoutPage(driver)
        
    def tap_deposit(self):
        self.driver.find_element(*self.deposit_locators.DEPOSIT_BUTTON).click()
        time.sleep(0.5)
        return self

    def tap_unpaid_tab(self):
        self.driver.find_element(*self.deposit_locators.UNPAID_TAB).click()
        time.sleep(0.5)
        return self

    def edit_deposit_amount(self):
        self.driver.find_element(*self.deposit_locators.EDIT_AMOUNT_BUTTON).click()
        time.sleep(0.5)
        
        self.create_checkout_page.enter_deposit_amount()
        return self

    def handle_payment(self):
        selected_option = random.choice(self.deposit_locators.OPTIONS)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{selected_option}")').click()
        time.sleep(0.5)
        
        if selected_option == self.deposit_locators.OPTIONS[0]:
            # confirm payment
            self.handle_payment_options()
            
        elif selected_option == self.deposit_locators.OPTIONS[1]:
            # do not collect
            self.driver.find_element(*self.deposit_locators.CONFIRM_BUTTON).click()
        else:
            # cancel appointment
            self.driver.find_element(*self.deposit_locators.CONFIRM_BUTTON).click()
        return self
      
    def handle_payment_options(self):
        try:
          time.sleep(1)
          selected_payment = random.choice(self.deposit_locators.PAYMENT_OPTIONS)
          self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{selected_payment}")').click()
          
          if selected_payment == "銀行匯款":
             random_numbers = ''.join(str(random.randint(1, 9)) for _ in range(5))
                
             transfer_input = self.driver.find_element(*self.deposit_locators.TRANSFER_NUMBER_INPUT)
             if transfer_input.is_displayed():
                transfer_input.send_keys(random_numbers)
                time.sleep(0.5)
            
          self.driver.find_element(*self.deposit_locators.CONFIRM_BUTTON).click()

          return self
            
        except Exception as e:
            print(f"Error occurred when handling payment options: {e}")


    def tap_paid_tab(self):
        self.driver.find_element(*self.deposit_locators.PAID_TAB).click()
        time.sleep(0.5)
        return self

    def tap_paid_invoice(self):
        self.driver.find_element(*self.deposit_locators.PAID_INVOICE_ITEM).click()
        time.sleep(0.5)
        return self

    def return_to_calendar(self):
        for _ in range(2):
            self.driver.find_element(*self.deposit_locators.BACK_BUTTON).click()
            time.sleep(0.5)
        return self
        
        
        
    