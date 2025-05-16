import random
import string
import time
import math

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.shared_components.common_use import CommonUseSection
from pages.shared_components.common_action import CommonActions
from pages.locators.android.create.create_checkout_locators import CreateCheckoutLocators

class CreateCheckoutPage(CommonUseSection):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.common_actions = CommonActions(driver)

    def click_create_checkout(self):
        try:
            self.common_actions.is_element_visible(*CreateCheckoutLocators.CREATE_BTN)
            self.common_actions.click_element(*CreateCheckoutLocators.CREATE_BTN)
            self.common_actions.is_element_visible(*CreateCheckoutLocators.CREATE_CHECKOUT_OPTION)
            self.common_actions.click_element(*CreateCheckoutLocators.CREATE_CHECKOUT_OPTION)
                            
        except TimeoutException:
            raise NoSuchElementException("Unable to find create checkout button or option after waiting")
        return self
      
    def select_sell_item(self):
        self.common_actions.click_element(*CreateCheckoutLocators.WINDOW_SECTION['sell_item_option'])
        
    def select_sell_ticket(self):
        self.common_actions.click_element(*CreateCheckoutLocators.WINDOW_SECTION['sell_ticket_option'])

    def select_deposit(self):
        self.common_actions.click_element(*CreateCheckoutLocators.WINDOW_SECTION['deposit_option'])

    def select_sales_owner(self, is_performance_change=False):
        if is_performance_change:
           # change performance personnel
           self.common_actions.is_element_visible(*CreateCheckoutLocators.PERFORMANCE_PERSONNEL)
           self.common_actions.click_element(*CreateCheckoutLocators.PERFORMANCE_PERSONNEL)
           self.common_actions.click_element(*CreateCheckoutLocators.PERFORMANCE_CHANGE_PERSONNEL_SALLY)
           self.common_actions.click_element(*CreateCheckoutLocators.SALES_OWNER_SAVE_BUTTON)
        else:
           # select sales owner
           self.common_actions.is_element_visible(*CreateCheckoutLocators.DESIGNATED_APPOINTMENT_TOGGLE)
           self.common_actions.click_element(*CreateCheckoutLocators.DESIGNATED_APPOINTMENT_TOGGLE)
           self.common_actions.click_element(*CreateCheckoutLocators.SALES_OWNER_SELECT_QA_TESTER)
           self.common_actions.click_element(*CreateCheckoutLocators.SALES_OWNER_SAVE_BUTTON)
    
        return self
    
    def non_selected_member_section(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.NON_SELECTED_MEMBER_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.NON_SELECTED_MEMBER_SECTION)
        
    def select_item(self):
        self.swipe_and_find_tab(CreateCheckoutLocators.AUTO_TEST_TAB)
        # choose the testing option below the item
        try:
            selected_options = random.sample(CreateCheckoutLocators.TEST_PRODUCT_OPTIONS, 2)
            
            for option in selected_options:
                service = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, option)
                service.click()
                time.sleep(0.5)
                
            self.view_item_details()
            
        except Exception as e:
            print(f"Error selecting services: {str(e)}")

    def view_item_details(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.TESTING_ITEM_INFO)
        self.common_actions.click_element(*CreateCheckoutLocators.TESTING_ITEM_INFO)
        assert self.common_actions.get_element_text(*CreateCheckoutLocators.ITEM_INFO_TITLE) == "測試1"
        assert self.common_actions.is_element_visible(*CreateCheckoutLocators.ITEM_INFO_PRICE)
        assert self.common_actions.is_element_visible(*CreateCheckoutLocators.ITEM_INFO_REQUEST_PRICE)
        
        # click back button back to the item list
        self.common_actions.click_element(*CreateCheckoutLocators.ITEM_INFO_BACK_BUTTON)
        
        # click the save button to save the item
        self.common_actions.click_element(*CreateCheckoutLocators.SAVE_ITEM_BTN)

    def search_non_existing_member(self, phone_number):
        search_input = self.common_actions.find_element(*CreateCheckoutLocators.MEMBER_SEARCH)
        search_input.click()
        search_input.send_keys(phone_number)
        assert self.common_actions.get_element_text(*CreateCheckoutLocators.MEMBER_SEARCH_NOT_FOUND) == "查無資料" , "Displayed member search not found"
        
        self.common_actions.click_element(*CreateCheckoutLocators.CLEAR_INPUT_SEARCH)
        
    def search_existing_member(self, phone_number):
        search_input = self.common_actions.find_element(*CreateCheckoutLocators.MEMBER_SEARCH)
        search_input.click()
        search_input.send_keys(phone_number)
        self.click_search_result()
           
    def click_search_result(self):
        try: 
            self.common_actions.is_element_visible(*CreateCheckoutLocators.MEMBER_SEARCH_RESULT)
            self.common_actions.click_element(*CreateCheckoutLocators.MEMBER_SEARCH_RESULT)
        except Exception as e:
            print(f"Error clicking search result: {str(e)}")
            raise
        
    def click_non_selected_member_section(self): 
        self.common_actions.is_element_visible(*CreateCheckoutLocators.NON_SELECTED_MEMBER_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.NON_SELECTED_MEMBER_SECTION)
    
    def add_new_member(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.ADD_MEMBER_BUTTON)
        self.common_actions.click_element(*CreateCheckoutLocators.ADD_MEMBER_BUTTON)
        self.new_member()

    def delete_selected_member(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.DELETE_MEMBER_BUTTON)
        self.common_actions.click_element(*CreateCheckoutLocators.DELETE_MEMBER_BUTTON)
        
        # click the non-selected member again to enter the member list
        self.common_actions.is_element_visible(*CreateCheckoutLocators.NON_SELECTED_MEMBER_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.NON_SELECTED_MEMBER_SECTION)
        
    def clear_all_items(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.ITEM_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.ITEM_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.SELECT_ITEM_BTN)
        self.common_actions.click_element(*CreateCheckoutLocators.CLEAR_ITEMS_BTN)

    def clear_all_tickets(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.TICKET_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.TICKET_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.SELECT_TICKETS_BTN)
        self.common_actions.click_element(*CreateCheckoutLocators.CLEAR_TICKETS_BTN)
        
    def ticket_section(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.TICKET_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.TICKET_SECTION)
        
    def adjust_item(self, existing_member=False):
        self.update_items_amount()
        time.sleep(0.5)
        self.update_items_quantity()
        time.sleep(0.5)
        self.add_new_discount(existing_member)
        time.sleep(0.5)
        self.remove_item()

    def select_payment_with_price_adjustment(self, is_above_price=False):
        """
        Args:
            is_above_price (bool): True if the payment amount is above the item price, False if it is below the item price
        """
        
        # click to enter payment page
        self.common_actions.is_element_visible(*CreateCheckoutLocators.PAYMENT_METHOD)
        self.common_actions.click_element(*CreateCheckoutLocators.PAYMENT_METHOD)
        
        # use regex to match any number
        TOTAL_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("\\d{1,3}(,\\d{3})*").instance(0)')

        total_amount_text = self.driver.find_element(*TOTAL_AMOUNT).text
        total_amount = int(total_amount_text.replace(",", ""))

        if is_above_price:
            cash_amount = total_amount + random.randint(10, 20000)
        else:
            if total_amount <= 1:
                cash_amount = 1
            else:
                min_amount = min(10, total_amount - 1)
                if min_amount < 1:
                    min_amount = 1
                cash_amount = random.randint(min_amount, total_amount - 1)

        # adjust the cash amount
        self.common_actions.is_element_visible(*CreateCheckoutLocators.CASH_SECTION['edit_btn'])
        self.common_actions.click_element(*CreateCheckoutLocators.CASH_SECTION['edit_btn'])
        self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['clear'])
        time.sleep(0.5)
        self.driver.find_element(*CreateCheckoutLocators.CASH_SECTION['input_field']).send_keys(str(cash_amount))
        time.sleep(1)
        self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['confirm'])
        
        error_element = self.driver.find_element(*CreateCheckoutLocators.PAYMENT_ERROR_MESSAGE(is_above_price))
        error_text = error_element.text.strip()
        diff = error_text.split("NT$")[1].strip().replace(",", "")


        if is_above_price:
            self.common_actions.is_element_visible(*CreateCheckoutLocators.CASH_SECTION['edit_btn'])
            self.common_actions.click_element(*CreateCheckoutLocators.CASH_SECTION['edit_btn'])
            self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['clear'])
            restore_amount = cash_amount - int(diff)
            self.driver.find_element(*CreateCheckoutLocators.CASH_SECTION['input_field']).send_keys(str(restore_amount))
            self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['confirm'])
        else:
            self.common_actions.is_element_visible(*CreateCheckoutLocators.CREDIT_CARD_SECTION['edit_btn'])
            self.common_actions.click_element(*CreateCheckoutLocators.CREDIT_CARD_SECTION['edit_btn'])
            self.driver.find_element(*CreateCheckoutLocators.CREDIT_CARD_SECTION['input_field']).send_keys(str(diff))
            self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['confirm'])

        return self

    def input_record_content(self):
        time.sleep(0.5)
        record_input = self.driver.find_element(*CreateCheckoutLocators.CHECKOUT_SECTION['record_content'])
        record_input.click()
        time.sleep(0.5)
        # checkout content modal input
        self.common_actions.is_element_visible(*CreateCheckoutLocators.CHECKOUT_SECTION['content_input'])
        self.common_actions.click_element(*CreateCheckoutLocators.CHECKOUT_SECTION['content_input'])
        char = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?" + "QA測試文字在這裡qa_test"
        random_text = ''.join(random.choice(char) for _ in range(20))
        
        self.driver.find_element(*CreateCheckoutLocators.CHECKOUT_SECTION['content_input']).send_keys(random_text)
        time.sleep(0.5)
        self.common_actions.click_element(*CreateCheckoutLocators.CHECKOUT_SECTION['save_button'])
        
    def cancel_record_content(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.CHECKOUT_SECTION['record_content'])
        self.common_actions.click_element(*CreateCheckoutLocators.CHECKOUT_SECTION['record_content'])
        time.sleep(0.5)
        # checkout content modal input
        self.common_actions.is_element_visible(*CreateCheckoutLocators.CHECKOUT_SECTION['content_input'])
        self.common_actions.click_element(*CreateCheckoutLocators.CHECKOUT_SECTION['content_input'])
        char = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?" + "QA測試文字在這裡qa_test"
        random_text = ''.join(random.choice(char) for _ in range(20))
        
        self.driver.find_element(*CreateCheckoutLocators.CHECKOUT_SECTION['content_input']).send_keys(random_text)
        time.sleep(0.5)
        self.common_actions.click_element(*CreateCheckoutLocators.CHECKOUT_SECTION['cancel_button'])
        time.sleep(0.5)
        
        self.common_actions.click_element(*CreateCheckoutLocators.CHECKOUT_SECTION['window_leave_button'])
    
    def calculate_change_amount(self):
        
        TOTAL_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("\\d{1,3}(,\\d{3})*").instance(0)')

        total_amount_text = self.driver.find_element(*TOTAL_AMOUNT).text
        total_amount = int(total_amount_text.replace(",", ""))
        
        self.common_actions.is_element_visible(*CreateCheckoutLocators.CALCULATE_ICON)
        self.common_actions.click_element(*CreateCheckoutLocators.CALCULATE_ICON)
        
        payment_amount = random.randint(total_amount + 1, total_amount * 2)
    
        self.driver.find_element(*CreateCheckoutLocators.CASH_SECTION['input_field']).send_keys(str(payment_amount))
    
        expected_change = payment_amount - total_amount
    
        CHANGE_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textMatches("\\d{1,3}(,\\d{3})*")')
        change_amount_text = self.driver.find_element(*CHANGE_AMOUNT).text
        actual_change = int(change_amount_text.replace(",", ""))
    
        assert actual_change == expected_change, f"Expected change amount {expected_change}, but got {actual_change}"
        
        self.common_actions.click_element(*CreateCheckoutLocators.CALCULATE_CHANGE_BACK_ICON)
        
    def adjust_sales_performance(self):
        self.common_actions.click_element(*CreateCheckoutLocators.SALES_PERFORMANCE)
        self.change_performance_posting_date()
        self.select_sales_owner(is_performance_change=True)
        self.change_total_sales_performance()
        self.common_actions.click_element(*CreateCheckoutLocators.TOTAL_PERFORMANCE_CONFIRM_BUTTON)
        
    def change_performance_posting_date(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.POSTING_SECTION)
        self.common_actions.click_element(*CreateCheckoutLocators.POSTING_SECTION)
        self.choose_date()
    
    def change_total_sales_performance(self):
        # due to the edit icon is not stable, so we need to try to click the icon
        time.sleep(1)
        try:
            self.driver.find_element(*CreateCheckoutLocators.SALES_PERFORMANCE_EDIT1_ICON).click()
        except NoSuchElementException:
            self.driver.find_element(*CreateCheckoutLocators.SALES_PERFORMANCE_EDIT2_ICON).click()
        time.sleep(1)
        self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['clear'])
        random_amount = random.randint(1, 1000)
        self.driver.find_element(*CreateCheckoutLocators.CASH_SECTION['input_field']).send_keys(str(random_amount))
        self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['confirm'])
        
    def adjust_bonus_points(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.BONUS_POINTS)
        self.common_actions.click_element(*CreateCheckoutLocators.BONUS_POINTS)
    
        bonus_points_input = random.choice([True, False])
        if bonus_points_input:
            random_amount = random.randint(10, 100)
            self.driver.find_element(*CreateCheckoutLocators.BONUS_POINTS_INPUT_FIELD).click()
            self.driver.find_element(*CreateCheckoutLocators.BONUS_POINTS_INPUT_FIELD).clear()
            self.driver.find_element(*CreateCheckoutLocators.BONUS_POINTS_INPUT_FIELD).send_keys(str(random_amount))
        else:
            random_option = random.choice(CreateCheckoutLocators.BONUS_POINTS_QUICK_SELECT_OPTIONS)
            self.driver.find_element(*random_option).click()
        
        time.sleep(0.5)
        self.driver.find_element(*CreateCheckoutLocators.BONUS_POINTS_CONFIRM_BUTTON).click()
        return self
        
    def select_payment_method(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.PAYMENT_METHOD)
        self.common_actions.click_element(*CreateCheckoutLocators.PAYMENT_METHOD)

    def proceed_to_checkout(self):
        self.common_actions.click_element(*CreateCheckoutLocators.CHECKOUT_BUTTON)
        self.common_actions.click_element(*CreateCheckoutLocators.MOVE_TO_SIGNATURE_BUTTON)


    def clear_signature(self):
        self.common_actions.click_element(*CreateCheckoutLocators.CLEAR_SIGNATURE)

    def confirm_checkout(self):
        self.common_actions.click_element(*CreateCheckoutLocators.CONFIRM_CHECKOUT)
        

# sell ticker use function 
    def select_ticket(self):      
        time.sleep(1)
        # ticket 1:
        self.common_actions.is_element_visible(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket1']['select'])
        self.common_actions.click_element(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket1']['select'])
    
        self.common_actions.is_element_visible(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket1']['input'])
        self.common_actions.click_element(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket1']['input'])
        self.driver.find_element(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket1']['input']).clear()
        random_quantity = str(random.randint(2, 200))
        self.driver.find_element(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket1']['input']).send_keys(random_quantity)
        time.sleep(0.5)
        self.driver.hide_keyboard()
        
        # ticket 2:
        self.common_actions.is_element_visible(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket2']['select'])
        self.common_actions.click_element(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket2']['select'])
    
        clicks = random.randint(1, 5)
        for _ in range(clicks):
            self.driver.find_element(*CreateCheckoutLocators.TICKET_ELEMENTS['ticket2']['plus']).click()
            time.sleep(1)
            
        self.driver.find_element(*CreateCheckoutLocators.TICKET_INFO).click()
        actual_text = ''.join(self.driver.find_element(*CreateCheckoutLocators.TICKET_INFO_TITLE).text.split())
        expected_text = ''.join("自動化測試票券".split())
    
        assert actual_text == expected_text, f"預期標題為 '自動化測試票券'，但實際為 '{actual_text}'"
        
        self.common_actions.is_element_visible(*CreateCheckoutLocators.TICKET_INFO_BACK)
        self.common_actions.click_element(*CreateCheckoutLocators.TICKET_INFO_BACK)       
                
        self.common_actions.is_element_visible(*CreateCheckoutLocators.SELECT_TICKETS_SAVE_ICON)
        self.common_actions.click_element(*CreateCheckoutLocators.SELECT_TICKETS_SAVE_ICON)
        return self
      
      
                
    # deposit checkout use function
    def enter_deposit_amount(self):
        self.driver.find_element(*CreateCheckoutLocators.DEPOSIT_AMOUNT_INPUT).click()
        random_amount = str(random.randint(1, 10000))
        self.driver.find_element(*CreateCheckoutLocators.DEPOSIT_AMOUNT_INPUT).send_keys(random_amount)
        self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['clear'])
        self.driver.find_element(*CreateCheckoutLocators.DEPOSIT_AMOUNT_INPUT).send_keys(random_amount)
        self.common_actions.click_element(*CreateCheckoutLocators.COMMON_BUTTONS['confirm'])
        return self
        
    def edit_deposit_amount(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.EDIT_DEPOSIT_AMOUNT_ICON)
        self.common_actions.click_element(*CreateCheckoutLocators.EDIT_DEPOSIT_AMOUNT_ICON)
        time.sleep(0.5)
        self.enter_deposit_amount()
        return self
    
    def edit_sales_amount(self):
        self.common_actions.is_element_visible(*CreateCheckoutLocators.EDIT_SALES_AMOUNT_ICON)
        self.common_actions.click_element(*CreateCheckoutLocators.EDIT_SALES_AMOUNT_ICON)
        time.sleep(0.5)
        self.enter_deposit_amount()
        return self
    