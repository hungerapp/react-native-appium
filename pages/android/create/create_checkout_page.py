import random
import string
import time
import math


from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from pages.shared_components.common_use import CommonUseSection

class CreateCheckoutPage(CommonUseSection):
    CREATE_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[42]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/com.horcrux.svg.SvgView[6]/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    CREATE_CHECKOUT_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("結帳")')
    WINDOW_SECTION = {
        'sell_item_option': (AppiumBy.ACCESSIBILITY_ID, '販售商品'),
        'sell_ticket_option': (AppiumBy.ACCESSIBILITY_ID, '販售票券, (會員限定)'),
        'deposit_option': (AppiumBy.ACCESSIBILITY_ID, '客人儲值（入金）, (會員限定)')
    }
    DESIGNATED_APPOINTMENT_TOGGLE = (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")
    SALES_OWNER_SELECT = (AppiumBy.ACCESSIBILITY_ID, "QA測試人員")
    SALES_OWNER_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
    AUTO_TEST_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試商品")')
    TESTING1_ITEM_SELECT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試1")')
    TESTING_ITEM_INFO = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-info"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    ITEM_INFO_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試1")')
    ITEM_INFO_PRICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("NT$")')
    ITEM_INFO_REQUEST_PRICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("NT$")')
    ITEM_INFO_BACK_BUTTON = (AppiumBy.XPATH, '//com.horcrux.svg.GroupView')
    SAVE_PRODUCT_BTN = (AppiumBy.XPATH, '//com.horcrux.svg.GroupView')
    SAVE_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    NON_SELECTED_MEMBER_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("尚未選擇會員")')
    CLEAR_INPUT_SEARCH = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="circle-xmark"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    MEMBER_SEARCH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入手機號碼、姓名進行搜尋")')
    MEMBER_SEARCH_NOT_FOUND = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("查無資料")')
    PHONE_NUMBER_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入電話")')
    NICKNAME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入別名")')
    MEMBER_DESCRIPTION_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入內容")')
    MEMBER_DESCRIPTION_MODAL_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
    MEMBER_DESCRIPTION_MODAL_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    ADD_NEW_MEMBER_TOGGLE = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
    SAVE_NEW_MEMBER_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    DELETE_MEMBER_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="會員"]/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    PAYMENT_METHOD = (AppiumBy.ACCESSIBILITY_ID, '選擇支付方式')
    CASH_SECTION = {
        'edit_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
        'input_field': (AppiumBy.XPATH, '//android.widget.EditText')
    }
    CREDIT_CARD_SECTION = {
        'edit_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
        'input_field': (AppiumBy.XPATH, '//android.widget.EditText')
    }
    COMMON_BUTTONS = {
        'clear': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")'),
        'confirm': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    }
    PAYMENT_ERROR_MESSAGE = lambda self, is_above: (
        AppiumBy.ANDROID_UIAUTOMATOR, 
        f'new UiSelector().textContains("{("多" if is_above else "少")}收 NT$")'
    )
    ITEM_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("商品")')
    SELECT_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇商品")')
    SELECT_TICKETS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("選擇票券")')
    CLEAR_ITEMS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部清除")')
    TICKET_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("票券")')
    CLEAR_TICKETS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全部清除")')
    CHECKOUT_SECTION = {
      'record_content': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入內容")'),
      'content_input': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")'),
      'save_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'),
      'clear_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")'),
      'cancel_button': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'),
      'window_leave_button': (AppiumBy.ACCESSIBILITY_ID, '離開')
    }
    CANCEL_RECORD = (AppiumBy.XPATH, "//android.view.View[@content-desc='取消']")
    SALES_PERFORMANCE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("總業績")')
    POSTING_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("業績記入日期")')
    RIGHT_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(6)')
    PERFORMANCE_PERSONNEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("業績歸屬")')
    PERFORMANCE_CHANGE_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲')
    SALES_PERFORMANCE_EDIT_ICON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="pen-to-square"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    TOTAL_PERFORMANCE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    CALCULATE_ICON = (AppiumBy.XPATH, '//android.widget.TextView[@text="找零"]')
    CALCULATE_CHANGE_BACK_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView")')
    
    BONUS_POINTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("紅利點數")')
    BONUS_POINTS_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    CHECKOUT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("結帳 NT$")')
    MOVE_TO_SIGNATURE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '進行簽名')
    SIGNATURE_PAD = (AppiumBy.CLASS_NAME, "android.widget.Image")
    CLEAR_SIGNATURE = (AppiumBy.ACCESSIBILITY_ID, "清除簽名")
    CONFIRM_CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, '確認結帳')
    
    # Sell ticket use ID
    TICKET_ELEMENTS = {
        'ticket1': {
            'select': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試票券")'),
            'input': (AppiumBy.XPATH, '//android.widget.EditText')
        },
        'ticket2': {
            'select': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試票卷2")'),
            'plus': (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="plus"])[2]/com.horcrux.svg.SvgView')
        }
    }
    TICKET_INFO = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="circle-info"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    TICKET_INFO_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試票券")')
    TICKET_INFO_BACK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView")')
    SELECT_TICKETS_SAVE_ICON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="check"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    
    DEPOSIT_AMOUNT_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    EDIT_DEPOSIT_AMOUNT_ICON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    EDIT_SALES_AMOUNT_ICON = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="pen-to-square"])[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    
    def __init__(self, driver):
        self.driver = driver

    def click_create_checkout(self):
        try:
          time.sleep(1)
          create_button = self.driver.find_element(*self.CREATE_BTN)
          if create_button.is_displayed() and create_button.is_enabled():
              create_button.click()
          time.sleep(0.5)
          self.driver.find_element(*self.CREATE_CHECKOUT_OPTION).click()
                    
        except NoSuchElementException:
          raise NoSuchElementException("Unable to find create checkout button after multiple attempts")
      
        return self
      
    def select_sell_item(self):
        time.sleep(1)
        self.driver.find_element(*self.WINDOW_SECTION['sell_item_option']).click()
        
    def select_sell_ticket(self):
        time.sleep(1)
        self.driver.find_element(*self.WINDOW_SECTION['sell_ticket_option']).click()

    def select_deposit(self):
        time.sleep(1)
        self.driver.find_element(*self.WINDOW_SECTION['deposit_option']).click()

    def select_sales_owner(self, is_performance_change=False):
        time.sleep(0.5)
        if is_performance_change:
           # change performance personnel
           self.driver.find_element(*self.PERFORMANCE_PERSONNEL).click()
           time.sleep(1)
           self.driver.find_element(*self.PERFORMANCE_CHANGE_PERSONNEL).click()
           self.driver.find_element(*self.SALES_OWNER_SAVE_BUTTON).click()
        else:
           # select sales owner
           time.sleep(0.5)
           self.driver.find_element(*self.DESIGNATED_APPOINTMENT_TOGGLE).click()
           time.sleep(0.5)
           self.driver.find_element(*self.SALES_OWNER_SELECT).click()
           self.driver.find_element(*self.SALES_OWNER_SAVE_BUTTON).click()
    
        return self
    
    def non_selected_member_section(self):
        time.sleep(1)
        self.driver.find_element(*self.NON_SELECTED_MEMBER_SECTION).click()
        

    def select_item(self):
        try:
            tab_container = self.driver.find_element(*self.TAB_CONTAINER)
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
                    auto_test_tab = self.driver.find_element(*self.AUTO_TEST_TAB)
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
            test_product_options = [
              'new UiSelector().text("測試1")',
              'new UiSelector().text("測試2")',
              'new UiSelector().text("測試3")',
              'new UiSelector().text("測試4")',
            ]
            
            selected_options = random.sample(test_product_options, 2)
            
            for option in selected_options:
                service = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, option)
                service.click()
                time.sleep(0.5)
                
            self.view_item_details()
            
        except Exception as e:
            print(f"Error selecting services: {str(e)}")


    def view_item_details(self):
        self.driver.find_element(*self.TESTING_ITEM_INFO).click()
        time.sleep(1)
        assert self.driver.find_element(*self.ITEM_INFO_TITLE).text.strip() == "測試1"
        assert self.driver.find_element(*self.ITEM_INFO_PRICE).is_displayed()
        assert self.driver.find_element(*self.ITEM_INFO_REQUEST_PRICE).is_displayed()
        
        # click back button back to the item list
        self.driver.find_element(*self.ITEM_INFO_BACK_BUTTON).click()
        
        time.sleep(1)
        # click the save button to save the item
        self.driver.find_element(*self.SAVE_ITEM_BTN).click()

    def search_non_existing_member(self, phone_number):
        search_input = self.driver.find_element(*self.MEMBER_SEARCH)
        search_input.click()
        search_input.send_keys(phone_number)
        time.sleep(1)
        assert self.driver.find_element(*self.MEMBER_SEARCH_NOT_FOUND).text.strip() == "查無資料" , "Displayed member search not found"
        
        clear_input = self.driver.find_element(*self.CLEAR_INPUT_SEARCH)
        clear_input.click()
        
    def search_existing_member(self, phone_number):
        time.sleep(0.5)
        search_input = self.driver.find_element(*self.MEMBER_SEARCH)
        search_input.click()
        search_input.send_keys(phone_number)
        time.sleep(1)
        member_result = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 
            'new UiSelector().textContains("+886 972 205690")'
        )
        member_result.click()
        
    def click_search_result(self):
        time.sleep(1)
        member_result = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 
            'new UiSelector().textContains("+886 972 205690")'
        )
        member_result.click()

    def delete_selected_member(self):
        self.driver.find_element(*self.DELETE_MEMBER_BUTTON).click()
        time.sleep(1)
        # click the non-selected member again to enter the member list
        self.driver.find_element(*self.NON_SELECTED_MEMBER_SECTION).click()
        
    def clear_all_items(self):
        time.sleep(0.5)
        self.driver.find_element(*self.ITEM_SECTION).click()
        time.sleep(0.5)
        self.driver.find_element(*self.SELECT_ITEM_BTN).click()
        self.driver.find_element(*self.CLEAR_ITEMS_BTN).click()
        
    def clear_all_tickets(self):
        time.sleep(0.5)
        self.driver.find_element(*self.TICKET_SECTION).click()
        self.driver.find_element(*self.SELECT_TICKETS_BTN).click()
        time.sleep(0.5)
        self.driver.find_element(*self.CLEAR_TICKETS_BTN).click()
        
    def ticket_section(self):
        self.driver.find_element(*self.TICKET_SECTION).click()
        
    def adjust_item(self, add_new_member=False):
        self.update_items_amount()
        time.sleep(0.5)
        self.update_items_quantity()
        time.sleep(0.5)
        self.add_new_discount(add_new_member)
        time.sleep(0.5)
        self.remove_item()


    def select_payment_with_price_adjustment(self, is_above_price=False):
        """
        Args:
            is_above_price (bool): True if the payment amount is above the item price, False if it is below the item price
        """
        
        # click to enter payment page
        self.driver.find_element(*self.PAYMENT_METHOD).click()
        time.sleep(0.5)
        
        # use regex to match any number
        TOTAL_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("\\d{1,3}(,\\d{3})*").instance(0)')

        total_amount_text = self.driver.find_element(*TOTAL_AMOUNT).text
        total_amount = int(total_amount_text.replace(",", ""))
        
        min_amount = int(total_amount * 1.1) if is_above_price else 10
        max_amount = int(total_amount * 1.9) if is_above_price else int(total_amount * 0.9)


        cash_amount = random.randint(min_amount, max_amount)

        # adjust the cash amount
        self.driver.find_element(*self.CASH_SECTION['edit_btn']).click()
        self.driver.find_element(*self.COMMON_BUTTONS['clear']).click()
        self.driver.find_element(*self.CASH_SECTION['input_field']).send_keys(str(cash_amount))
        self.driver.find_element(*self.COMMON_BUTTONS['confirm']).click()


        error_element = self.driver.find_element(*self.PAYMENT_ERROR_MESSAGE(is_above_price))
        error_text = error_element.text.strip()
        diff = int(error_text.split("NT$")[1].strip().replace(",", ""))

        time.sleep(0.5)

        if is_above_price:
            self.driver.find_element(*self.CASH_SECTION['edit_btn']).click()
            self.driver.find_element(*self.COMMON_BUTTONS['clear']).click()
            self.driver.find_element(*self.CASH_SECTION['input_field']).send_keys(str(total_amount))
            self.driver.find_element(*self.COMMON_BUTTONS['confirm']).click()
        else:
            self.driver.find_element(*self.CREDIT_CARD_SECTION['edit_btn']).click()
            self.driver.find_element(*self.CREDIT_CARD_SECTION['input_field']).send_keys(str(diff))
            self.driver.find_element(*self.COMMON_BUTTONS['confirm']).click()

        return self

    def input_record_content(self):
        time.sleep(0.5)
        record_input = self.driver.find_element(*self.CHECKOUT_SECTION['record_content'])
        record_input.click()
        time.sleep(0.5)
        # checkout content modal input
        self.driver.find_element(*self.CHECKOUT_SECTION['content_input']).click()
        char = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?" + "QA測試文字在這裡qa_test"
        random_text = ''.join(random.choice(char) for _ in range(20))
        
        self.driver.find_element(*self.CHECKOUT_SECTION['content_input']).send_keys(random_text)
        time.sleep(0.5)
        self.driver.find_element(*self.CHECKOUT_SECTION['save_button']).click()
        

    def cancel_record_content(self):
        record_input = self.driver.find_element(*self.CHECKOUT_SECTION['record_content'])
        record_input.click()
        time.sleep(0.5)
        # checkout content modal input
        self.driver.find_element(*self.CHECKOUT_SECTION['content_input']).click()
        char = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?" + "QA測試文字在這裡qa_test"
        random_text = ''.join(random.choice(char) for _ in range(20))
        
        self.driver.find_element(*self.CHECKOUT_SECTION['content_input']).send_keys(random_text)
        time.sleep(0.5)
        self.driver.find_element(*self.CHECKOUT_SECTION['cancel_button']).click()
        time.sleep(0.5)
        
        self.driver.find_element(*self.CHECKOUT_SECTION['window_leave_button']).click()
    
    def calculate_change_amount(self):
        
        TOTAL_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("\\d{1,3}(,\\d{3})*").instance(0)')

        total_amount_text = self.driver.find_element(*TOTAL_AMOUNT).text
        total_amount = int(total_amount_text.replace(",", ""))
        
        self.driver.find_element(*self.CALCULATE_ICON).click()
        time.sleep(0.5)
        
        payment_amount = random.randint(total_amount + 1, total_amount * 2)
    
        self.driver.find_element(*self.CASH_SECTION['input_field']).send_keys(str(payment_amount))
    
        expected_change = payment_amount - total_amount
    
        CHANGE_AMOUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textMatches("\\d{1,3}(,\\d{3})*")')
        change_amount_text = self.driver.find_element(*CHANGE_AMOUNT).text
        actual_change = int(change_amount_text.replace(",", ""))
    
        assert actual_change == expected_change, f"Expected change amount {expected_change}, but got {actual_change}"
        
        self.driver.find_element(*self.CALCULATE_CHANGE_BACK_ICON).click()
        time.sleep(0.5)
        
    def adjust_sales_performance(self):
        self.driver.find_element(*self.SALES_PERFORMANCE).click()
        time.sleep(1)
        self.change_performance_posting_date()
        self.select_sales_owner(is_performance_change=True)
        self.change_total_sales_performance()
        time.sleep(1)
        self.driver.find_element(*self.TOTAL_PERFORMANCE_CONFIRM_BUTTON).click()
        
    def change_performance_posting_date(self):
        # randomly click left or right arrow icon to change the performance posting date
        self.driver.find_element(*self.POSTING_SECTION).click()
        time.sleep(2)
        
        # click right arrow multiple times
        clicks = random.randint(1, 5)
        for _ in range(clicks):
            self.driver.find_element(*self.RIGHT_ARROW).click()
            time.sleep(0.5)
        
        dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      
        random.choice(dates).click()
        
        # click outside to close the date window
        size = self.driver.get_window_size()
        self.driver.execute_script('mobile: clickGesture', {
            'x': int(size['width'] * 0.5),  
            'y': int(size['height'] * 0.9)   
        })
    
    def change_total_sales_performance(self):
        self.driver.find_element(*self.SALES_PERFORMANCE_EDIT_ICON).click()
        time.sleep(1)
        self.driver.find_element(*self.COMMON_BUTTONS['clear']).click()
        random_amount = random.randint(1, 1000)
        self.driver.find_element(*self.CASH_SECTION['input_field']).send_keys(str(random_amount))
        self.driver.find_element(*self.COMMON_BUTTONS['confirm']).click()
        

    def adjust_bonus_points(self):
        self.driver.find_element(*self.BONUS_POINTS).click()
        time.sleep(1)
        
        quick_select_options = [
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$1 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$10 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$50 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$100 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$200 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$250 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$500 : 1")'),
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NT$1,000 : 1")')
            ]
        
        random_option = random.choice(quick_select_options)
        self.driver.find_element(*random_option).click()
    
        self.driver.find_element(*self.BONUS_POINTS_CONFIRM_BUTTON).click()
        return self
        
        
    def select_payment_method(self):
        time.sleep(1)
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        self.driver.find_element(*self.MOVE_TO_SIGNATURE_BUTTON).click()
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
        self.driver.find_element(*self.CLEAR_SIGNATURE).click()


    def confirm_checkout(self):
        self.driver.find_element(*self.CONFIRM_CHECKOUT).click()
        time.sleep(1)
        

# sell ticker use function 

    def select_ticket(self):
        
        time.sleep(1)
        # ticket 1:
        self.driver.find_element(*self.TICKET_ELEMENTS['ticket1']['select']).click()
        time.sleep(0.5)
    
        self.driver.find_element(*self.TICKET_ELEMENTS['ticket1']['input']).click()
        self.driver.find_element(*self.TICKET_ELEMENTS['ticket1']['input']).clear()
        random_quantity = str(random.randint(2, 200))
        self.driver.find_element(*self.TICKET_ELEMENTS['ticket1']['input']).send_keys(random_quantity)
        time.sleep(0.5)
        
        # ticket 2:
        self.driver.find_element(*self.TICKET_ELEMENTS['ticket2']['select']).click()
        time.sleep(0.5)
    
        clicks = random.randint(1, 5)
        for _ in range(clicks):
            self.driver.find_element(*self.TICKET_ELEMENTS['ticket2']['plus']).click()
            time.sleep(1)
            
        self.driver.find_element(*self.TICKET_INFO).click()
        actual_text = ''.join(self.driver.find_element(*self.TICKET_INFO_TITLE).text.split())
        expected_text = ''.join("自動化測試票券".split())
    
        assert actual_text == expected_text, f"預期標題為 '自動化測試票券'，但實際為 '{actual_text}'"
        
        time.sleep(0.5)
        self.driver.find_element(*self.TICKET_INFO_BACK).click()
        
                
        self.driver.find_element(*self.SELECT_TICKETS_SAVE_ICON).click()
        return self
                
    # deposit checkout use function
    
    def enter_deposit_amount(self):
        self.driver.find_element(*self.DEPOSIT_AMOUNT_INPUT).click()
        random_amount = str(random.randint(1, 99998))
        self.driver.find_element(*self.DEPOSIT_AMOUNT_INPUT).send_keys(random_amount)
        time.sleep(0.5)
        self.driver.find_element(*self.COMMON_BUTTONS['clear']).click()
        self.driver.find_element(*self.DEPOSIT_AMOUNT_INPUT).send_keys(random_amount)
        self.driver.find_element(*self.COMMON_BUTTONS['confirm']).click()
        time.sleep(0.5)
        return self
        
    def edit_deposit_amount(self):
        self.driver.find_element(*self.EDIT_DEPOSIT_AMOUNT_ICON).click()
        time.sleep(0.5)
        self.enter_deposit_amount()
        return self
    
    def edit_sales_amount(self):
        self.driver.find_element(*self.EDIT_SALES_AMOUNT_ICON).click()
        time.sleep(0.5)
        self.enter_deposit_amount()
        return self
    