import random
import string
import time
import math


from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

from pages.shared_components.common_use import CommonUseSection
from pages.locators.android.create.create_checkout_locators import CreateCheckoutLocators

class CreateCheckoutPage(CommonUseSection):
    
    def __init__(self, driver):
        self.driver = driver
        self.create_checkout_locators = CreateCheckoutLocators()

    def click_create_checkout(self):
        try:
            time.sleep(1)
            wait = WebDriverWait(self.driver, 15)
            create_button = wait.until(
                EC.element_to_be_clickable(self.create_checkout_locators.CREATE_BTN)
            )
            create_button.click()
            
            checkout_option = wait.until(
                EC.element_to_be_clickable(self.create_checkout_locators.CREATE_CHECKOUT_OPTION)
            )
            checkout_option.click()
            
            logger.info("Successfully clicked create checkout button and option")
                    
        except TimeoutException:
            logger.error("Timeout waiting for create checkout button or option to be clickable")
            raise NoSuchElementException("Unable to find create checkout button or option after waiting")
        except Exception as e:
            logger.error(f"Error clicking create checkout: {str(e)}")
            raise
      
        return self
      
    def select_sell_item(self):
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.WINDOW_SECTION['sell_item_option']).click()
        
    def select_sell_ticket(self):
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.WINDOW_SECTION['sell_ticket_option']).click()

    def select_deposit(self):
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.WINDOW_SECTION['deposit_option']).click()

    def select_sales_owner(self, is_performance_change=False):
        time.sleep(0.5)
        if is_performance_change:
           # change performance personnel
           self.driver.find_element(*self.create_checkout_locators.PERFORMANCE_PERSONNEL).click()
           time.sleep(1)
           self.driver.find_element(*self.create_checkout_locators.PERFORMANCE_CHANGE_PERSONNEL_SALLY).click()
           self.driver.find_element(*self.create_checkout_locators.SALES_OWNER_SAVE_BUTTON).click()
        else:
           # select sales owner
           time.sleep(0.5)
           self.driver.find_element(*self.create_checkout_locators.DESIGNATED_APPOINTMENT_TOGGLE).click()
           time.sleep(0.5)
           self.driver.find_element(*self.create_checkout_locators.SALES_OWNER_SELECT_QA_TESTER).click()
           self.driver.find_element(*self.create_checkout_locators.SALES_OWNER_SAVE_BUTTON).click()
    
        return self
    
    def non_selected_member_section(self):
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.NON_SELECTED_MEMBER_SECTION).click()
        

    def select_item(self):
        try:
            tab_container = self.driver.find_element(*self.create_checkout_locators.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location

            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
            y = location['y'] + int(size['height'] * 0.5)

            max_attempts = 3
            found_target = False

            for _ in range(max_attempts):
                self.driver.swipe(start_x, y, end_x, y, 100)
                time.sleep(0.5)
                try:
                    auto_test_tab = self.driver.find_element(*self.create_checkout_locators.AUTO_TEST_TAB)
                    if auto_test_tab.is_displayed():
                        auto_test_tab.click()
                        found_target = True
                        break
                except NoSuchElementException:
                    continue

            if not found_target:
                print("Could not find AUTO_TEST_TAB after maximum attempts")
                return self

        except Exception as e:
            print(f"Error swiping tabs: {str(e)}")
            return self
          
        # choose the testing option below the item
        try:
            selected_options = random.sample(self.create_checkout_locators.TEST_PRODUCT_OPTIONS, 2)
            
            for option in selected_options:
                service = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, option)
                service.click()
                time.sleep(0.5)
                
            self.view_item_details()
            
        except Exception as e:
            print(f"Error selecting services: {str(e)}")


    def view_item_details(self):
        self.driver.find_element(*self.create_checkout_locators.TESTING_ITEM_INFO).click()
        time.sleep(1)
        assert self.driver.find_element(*self.create_checkout_locators.ITEM_INFO_TITLE).text.strip() == "測試1"
        assert self.driver.find_element(*self.create_checkout_locators.ITEM_INFO_PRICE).is_displayed()
        assert self.driver.find_element(*self.create_checkout_locators.ITEM_INFO_REQUEST_PRICE).is_displayed()
        
        # click back button back to the item list
        self.driver.find_element(*self.create_checkout_locators.ITEM_INFO_BACK_BUTTON).click()
        
        time.sleep(1)
        # click the save button to save the item
        self.driver.find_element(*self.create_checkout_locators.SAVE_ITEM_BTN).click()

    def search_non_existing_member(self, phone_number):
        search_input = self.driver.find_element(*self.create_checkout_locators.MEMBER_SEARCH)
        search_input.click()
        search_input.send_keys(phone_number)
        time.sleep(1)
        assert self.driver.find_element(*self.create_checkout_locators.MEMBER_SEARCH_NOT_FOUND).text.strip() == "查無資料" , "Displayed member search not found"
        
        clear_input = self.driver.find_element(*self.create_checkout_locators.CLEAR_INPUT_SEARCH)
        clear_input.click()
        
    def search_existing_member(self, phone_number):
        time.sleep(0.5)
        search_input = self.driver.find_element(*self.create_checkout_locators.MEMBER_SEARCH)
        search_input.click()
        search_input.send_keys(phone_number)
        self.click_search_result()
    
        
    def click_search_result(self):
        try:
            time.sleep(1)  
            result = self.driver.find_element(*self.create_checkout_locators.MEMBER_SEARCH_RESULT)
            if result.is_displayed():
                result.click()
                time.sleep(0.5) 
        except Exception as e:
            print(f"點擊搜尋結果時發生錯誤: {str(e)}")
            raise
        
    def click_non_selected_member_section(self):
        self.driver.find_element(*self.create_checkout_locators.NON_SELECTED_MEMBER_SECTION).click()
    
    def add_new_member(self):
         self.driver.find_element(*self.create_checkout_locators.ADD_MEMBER_BUTTON).click()
         time.sleep(1)
         self.new_member()

    def delete_selected_member(self):
        self.driver.find_element(*self.create_checkout_locators.DELETE_MEMBER_BUTTON).click()
        time.sleep(1)
        # click the non-selected member again to enter the member list
        self.driver.find_element(*self.create_checkout_locators.NON_SELECTED_MEMBER_SECTION).click()
        
    def clear_all_items(self):
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.ITEM_SECTION).click()
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.SELECT_ITEM_BTN).click()
        self.driver.find_element(*self.create_checkout_locators.CLEAR_ITEMS_BTN).click()
        
    def clear_all_tickets(self):
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.TICKET_SECTION).click()
        self.driver.find_element(*self.create_checkout_locators.SELECT_TICKETS_BTN).click()
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.CLEAR_TICKETS_BTN).click()
        
    def ticket_section(self):
        self.driver.find_element(*self.create_checkout_locators.TICKET_SECTION).click()
        
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
        self.driver.find_element(*self.create_checkout_locators.PAYMENT_METHOD).click()
        time.sleep(0.5)
        
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
        self.driver.find_element(*self.create_checkout_locators.CASH_SECTION['edit_btn']).click()
        self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['clear']).click()
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.CASH_SECTION['input_field']).send_keys(str(cash_amount))
        self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['confirm']).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.create_checkout_locators.PAYMENT_ERROR_MESSAGE(is_above_price))
        )
        error_element = self.driver.find_element(*self.create_checkout_locators.PAYMENT_ERROR_MESSAGE(is_above_price))
        error_text = error_element.text.strip()
        diff = error_text.split("NT$")[1].strip().replace(",", "")

        time.sleep(2)

        if is_above_price:
            self.driver.find_element(*self.create_checkout_locators.CASH_SECTION['edit_btn']).click()
            self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['clear']).click()
            restore_amount = cash_amount - int(diff)
            self.driver.find_element(*self.create_checkout_locators.CASH_SECTION['input_field']).send_keys(str(restore_amount))
            self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['confirm']).click()
        else:
            self.driver.find_element(*self.create_checkout_locators.CREDIT_CARD_SECTION['edit_btn']).click()
            self.driver.find_element(*self.create_checkout_locators.CREDIT_CARD_SECTION['input_field']).send_keys(str(diff))
            self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['confirm']).click()

        return self

    def input_record_content(self):
        time.sleep(0.5)
        record_input = self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['record_content'])
        record_input.click()
        time.sleep(0.5)
        # checkout content modal input
        self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['content_input']).click()
        char = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?" + "QA測試文字在這裡qa_test"
        random_text = ''.join(random.choice(char) for _ in range(20))
        
        self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['content_input']).send_keys(random_text)
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['save_button']).click()
        

    def cancel_record_content(self):
        record_input = self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['record_content'])
        record_input.click()
        time.sleep(0.5)
        # checkout content modal input
        self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['content_input']).click()
        char = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?" + "QA測試文字在這裡qa_test"
        random_text = ''.join(random.choice(char) for _ in range(20))
        
        self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['content_input']).send_keys(random_text)
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['cancel_button']).click()
        time.sleep(0.5)
        
        self.driver.find_element(*self.create_checkout_locators.CHECKOUT_SECTION['window_leave_button']).click()
    
    def calculate_change_amount(self):
        
        TOTAL_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("\\d{1,3}(,\\d{3})*").instance(0)')

        total_amount_text = self.driver.find_element(*TOTAL_AMOUNT).text
        total_amount = int(total_amount_text.replace(",", ""))
        
        self.driver.find_element(*self.create_checkout_locators.CALCULATE_ICON).click()
        time.sleep(0.5)
        
        payment_amount = random.randint(total_amount + 1, total_amount * 2)
    
        self.driver.find_element(*self.create_checkout_locators.CASH_SECTION['input_field']).send_keys(str(payment_amount))
    
        expected_change = payment_amount - total_amount
    
        CHANGE_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textMatches("\\d{1,3}(,\\d{3})*")')
        change_amount_text = self.driver.find_element(*CHANGE_AMOUNT).text
        actual_change = int(change_amount_text.replace(",", ""))
    
        assert actual_change == expected_change, f"Expected change amount {expected_change}, but got {actual_change}"
        
        self.driver.find_element(*self.create_checkout_locators.CALCULATE_CHANGE_BACK_ICON).click()
        time.sleep(0.5)
        
    def adjust_sales_performance(self):
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.SALES_PERFORMANCE).click()
        self.change_performance_posting_date()
        self.select_sales_owner(is_performance_change=True)
        self.change_total_sales_performance()
        self.driver.find_element(*self.create_checkout_locators.TOTAL_PERFORMANCE_CONFIRM_BUTTON).click()
        
    def change_performance_posting_date(self):
        # randomly click left or right arrow icon to change the performance posting date
        self.driver.find_element(*self.create_checkout_locators.POSTING_SECTION).click()
        time.sleep(2)
        
        # click right arrow multiple times
        clicks = random.randint(1, 5)
        for _ in range(clicks):
            self.driver.find_element(*self.create_checkout_locators.RIGHT_ARROW).click()
            time.sleep(0.5)
        
        dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      
        random.choice(dates).click()
        
        # click outside to close the date window
        size = self.driver.get_window_size()
        tap_x = int(size['width'] * 0.5)
        tap_y = int(size['height'] * 0.9)
        
        # Method 1: Using W3C Actions API (preferred method for newer Appium versions)
        self.driver.execute_script('mobile: longClickGesture', {
            'x': tap_x,
            'y': tap_y,
            'duration': 100
        })
        
        # Method 2: Alternative - use tap coordinates method
        # self.driver.tap([(tap_x, tap_y)], 100)
    
    def change_total_sales_performance(self):
        # due to the edit icon is not stable, so we need to try to click the icon
        time.sleep(0.5)
        try:
            self.driver.find_element(*self.create_checkout_locators.SALES_PERFORMANCE_EDIT1_ICON).click()
        except NoSuchElementException:
            self.driver.find_element(*self.create_checkout_locators.SALES_PERFORMANCE_EDIT2_ICON).click()
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['clear']).click()
        random_amount = random.randint(1, 1000)
        self.driver.find_element(*self.create_checkout_locators.CASH_SECTION['input_field']).send_keys(str(random_amount))
        self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['confirm']).click()
        

    def adjust_bonus_points(self):
        self.driver.find_element(*self.create_checkout_locators.BONUS_POINTS).click()
        time.sleep(1)
    
        bonus_points_input = random.choice([True, False])
        if bonus_points_input:
            random_amount = random.randint(10, 100)
            self.driver.find_element(*self.create_checkout_locators.BONUS_POINTS_INPUT_FIELD).click()
            self.driver.find_element(*self.create_checkout_locators.BONUS_POINTS_INPUT_FIELD).clear()
            self.driver.find_element(*self.create_checkout_locators.BONUS_POINTS_INPUT_FIELD).send_keys(str(random_amount))
        else:
            random_option = random.choice(self.create_checkout_locators.BONUS_POINTS_QUICK_SELECT_OPTIONS)
            self.driver.find_element(*random_option).click()
        
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.BONUS_POINTS_CONFIRM_BUTTON).click()
        return self
        
        
    def select_payment_method(self):
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.PAYMENT_METHOD).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.create_checkout_locators.CHECKOUT_BUTTON).click()
        self.driver.find_element(*self.create_checkout_locators.MOVE_TO_SIGNATURE_BUTTON).click()
        time.sleep(1)

    def sign_request(self):
        """Simulate signature"""
        try:
            signature_pad = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Image")
            location = signature_pad.location
            size = signature_pad.size
            
            center_x = location['x'] + size['width'] * 0.15
            center_y = location['y'] + size['height'] * 0.35
            
            range_x = size['width'] * 0.15
            range_y = size['height'] * 0.15

            def generate_oval_points():
                points = []
                for i in range(8):
                    angle = (i / 8.0) * 2 * 3.14
                    x = center_x + range_x * 1.2 * math.cos(angle)
                    y = center_y + range_y * 0.9 * math.sin(angle)
                    points.append((x, y))
                return points

            actions = ActionChains(self.driver)
            oval_points = generate_oval_points()
            actions.move_to_element_with_offset(signature_pad,
                                             oval_points[0][0] - location['x'],
                                             oval_points[0][1] - location['y'])
            actions.click_and_hold()
            for point in oval_points[1:]:
                actions.move_to_element_with_offset(signature_pad,
                                                 point[0] - location['x'],
                                                 point[1] - location['y'])
                time.sleep(0.1)
            actions.release()
            actions.perform()
            time.sleep(0.3)

            actions = ActionChains(self.driver)
            start_x = center_x - range_x * 0.2
            start_y = center_y
            actions.move_to_element_with_offset(signature_pad,
                                             start_x - location['x'],
                                             start_y - location['y'])
            actions.click_and_hold()
            
            for i in range(4):
                x = start_x + range_x * 0.3 * i
                y = start_y + (range_y * 0.3 * math.sin(i * 3.14))
                actions.move_to_element_with_offset(signature_pad,
                                                 x - location['x'],
                                                 y - location['y'])
                time.sleep(0.1)
            
            actions.release()
            actions.perform()

        except Exception as e:
            print(f"Error during signing: {str(e)}")
            raise

    def clear_signature(self):
        time.sleep(1)
        self.driver.find_element(*self.create_checkout_locators.CLEAR_SIGNATURE).click()


    def confirm_checkout(self):
        self.driver.find_element(*self.create_checkout_locators.CONFIRM_CHECKOUT).click()
        time.sleep(1)
        

# sell ticker use function 

    def select_ticket(self):
        
        time.sleep(1)
        # ticket 1:
        self.driver.find_element(*self.create_checkout_locators.TICKET_ELEMENTS['ticket1']['select']).click()
        time.sleep(0.5)
    
        self.driver.find_element(*self.create_checkout_locators.TICKET_ELEMENTS['ticket1']['input']).click()
        self.driver.find_element(*self.create_checkout_locators.TICKET_ELEMENTS['ticket1']['input']).clear()
        random_quantity = str(random.randint(2, 200))
        self.driver.find_element(*self.create_checkout_locators.TICKET_ELEMENTS['ticket1']['input']).send_keys(random_quantity)
        time.sleep(0.5)
        
        # ticket 2:
        self.driver.find_element(*self.create_checkout_locators.TICKET_ELEMENTS['ticket2']['select']).click()
        time.sleep(0.5)
    
        clicks = random.randint(1, 5)
        for _ in range(clicks):
            self.driver.find_element(*self.create_checkout_locators.TICKET_ELEMENTS['ticket2']['plus']).click()
            time.sleep(1)
            
        self.driver.find_element(*self.create_checkout_locators.TICKET_INFO).click()
        actual_text = ''.join(self.driver.find_element(*self.create_checkout_locators.TICKET_INFO_TITLE).text.split())
        expected_text = ''.join("自動化測試票券".split())
    
        assert actual_text == expected_text, f"預期標題為 '自動化測試票券'，但實際為 '{actual_text}'"
        
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.TICKET_INFO_BACK).click()
        
                
        self.driver.find_element(*self.create_checkout_locators.SELECT_TICKETS_SAVE_ICON).click()
        return self
                
    # deposit checkout use function
    
    def enter_deposit_amount(self):
        self.driver.find_element(*self.create_checkout_locators.DEPOSIT_AMOUNT_INPUT).click()
        random_amount = str(random.randint(1, 10000))
        self.driver.find_element(*self.create_checkout_locators.DEPOSIT_AMOUNT_INPUT).send_keys(random_amount)
        time.sleep(0.5)
        self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['clear']).click()
        self.driver.find_element(*self.create_checkout_locators.DEPOSIT_AMOUNT_INPUT).send_keys(random_amount)
        self.driver.find_element(*self.create_checkout_locators.COMMON_BUTTONS['confirm']).click()
        time.sleep(0.5)
        return self
        
    def edit_deposit_amount(self):
        self.driver.find_element(*self.create_checkout_locators.EDIT_DEPOSIT_AMOUNT_ICON).click()
        time.sleep(0.5)
        self.enter_deposit_amount()
        return self
    
    def edit_sales_amount(self):
        self.driver.find_element(*self.create_checkout_locators.EDIT_SALES_AMOUNT_ICON).click()
        time.sleep(0.5)
        self.enter_deposit_amount()
        return self
    