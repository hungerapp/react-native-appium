import random
import time
import string
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class CommonUseSection:
    GENDER_OPTIONS = {
        "男": (AppiumBy.ACCESSIBILITY_ID, "男"),
        "女": (AppiumBy.ACCESSIBILITY_ID, "女"),
        "其他": (AppiumBy.ACCESSIBILITY_ID, "其他")
    }
    CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")')
    BIRTHDAY_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("生日")')
    CALENDAR_WINDOW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/pickers")')

    COUNTRY_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(3)')
    COUNTRY_CODE_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '+')]")
    CHANGED_COUNTRY_CODE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+")')
    COUNTRY_CODE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    COUNTRY_CODE_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '+')]")
    CHANGED_COUNTRY_CODE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+")')
    COUNTRY_CODE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)') 
    SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入國家或號碼進行搜尋")')
    
    
    
    
    
    SERVICE_PERSON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    SERVICE_TESTING_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SERVICE_PAGE_TOGGLE_SWITCH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(31)')
    SERVICE_PAGE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)')
    
    SERVICE_PERSONNEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    QA_TEST_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SELECT_ALL_OPTION = (AppiumBy.ACCESSIBILITY_ID, '全部選取')
    PERSONNEL_OPTIONS = [
        (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲'),
        (AppiumBy.ACCESSIBILITY_ID, 'Bella #美甲'),
        # Add more personnel options as needed
    ]
    PERSONNEL_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    
    
    # For checkout, request page
    AMOUNT_EDIT_ICON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="pen-to-square"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    AMOUNT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    AMOUNT_CLEAR_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")')
    AMOUNT_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    EDIT_ITEM_QUANTITY_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(3)')
    QUANTITLY_PLUS_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="plus"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    QUANTITY_REVISE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("^[1-9][0-9]{0,2}$")')
    QUANTITY_REVISE_INPUT2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    QUANTITY_REVISE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    REMOVE_ITEM_BTN = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    REMOVE_CONFIRM_BTN = (AppiumBy.ACCESSIBILITY_ID, '移除')
    BACK_TO_PREVIOUS_PAGE_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    ADD_NEW_DISCOUNT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("新增").instance(0)')
    DISCOUNT_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    CASH_QUICK_AMOUNTS = ["50", "100", "150", "200", "250", "300", "350", "400"]
    DISCOUNT_QUICK_RATES = ["95折", "92折", "9折", "88折", "85折", "8折", "75折", "7折"]
    DISCOUNT_INPUT_OPTIONS = [90, 85, 95, 80, 70, 85, 75]
    CASH_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("現金")')
    DISCOUNT_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("折數")')
    COUPON_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("票券")')
    # Input fields and buttons
    AMOUNT_INPUT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入金額")')
    DISCOUNT_INPUT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入折數")')
    QUICK_SELECT_AMOUNTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView")')
    AUTO_TEST_COUPON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試票券")')
    SELECT_TICKET_ICON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="caret-down"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    QUANTITY_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    NO_COUPON_AVAILABLE_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("目前沒有資料")')
    
    # for add new member
    PHONE_NUMBER_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入電話")')
    NICKNAME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入別名")')
    MEMBER_DESCRIPTION_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入內容")')
    MEMBER_DESCRIPTION_MODAL_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
    MEMBER_DESCRIPTION_MODAL_SAVE_BUTTON = (AppiumBy.XPATH, '(//com.horcrux.svg.SvgView)[2]')
    ADD_NEW_MEMBER_TOGGLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("user-plus")')
    # you cab change the id: new UiSelector().className("com.horcrux.svg.PathView").instance(1)
    SAVE_NEW_MEMBER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
    def __init__(self, driver):
        self.driver = driver
        
    def wait_briefly(self, seconds=0.5):
        time.sleep(seconds)

    def select_random_gender(self):
        """Select random gender"""
        try:
            gender = random.choice(list(self.GENDER_OPTIONS.keys()))
            self.driver.find_element(*self.GENDER_OPTIONS[gender]).click()
            time.sleep(0.5)
            return gender
        except Exception as e:
            print(f"Select gender error: {str(e)}")
            raise
        
    def select_random_date(self):
        """Random scroll to select date"""
        try:
            # Click birthday field to open date picker
            self.driver.find_element(*self.BIRTHDAY_FIELD).click()
        
            # Get date picker window
            calendar_window = self.driver.find_element(*self.CALENDAR_WINDOW)
            window_rect = calendar_window.rect
        
            # calculate year, month, day x coordinates
            year_x = window_rect['x'] + (window_rect['width'] * 0.17)  # left side year field
            month_x = window_rect['x'] + (window_rect['width'] * 0.5)  # middle month field
            day_x = window_rect['x'] + (window_rect['width'] * 0.83)   # right side day field
        
            # calculate y coordinate center point
            center_y = window_rect['y'] + window_rect['height'] / 2
        
            # random scroll each field
            date_columns = [
            {"name": "年", "x": year_x},
            {"name": "月", "x": month_x},
            {"name": "日", "x": day_x}
            ]
        
            for column in date_columns:
                swipe_times = random.randint(3, 6)
                for _ in range(swipe_times):
                    self._perform_random_swipe(
                    start_x=column["x"],
                    start_y=center_y,
                    max_offset=50, # limit horizontal random offset
                    )
                    time.sleep(0.5)
        
            # click confirm
            self.driver.find_element(*self.CONFIRM_BUTTON).click()
        
            # Return updated date text
            return self.driver.find_element(*self.BIRTHDAY_FIELD).text
        
        except Exception as e:
            print(f"Select date error: {str(e)}")
            raise
        
    def _perform_random_swipe(self, start_x, start_y, max_offset=50):
        """執行隨機滑動"""
        try:
            actions = ActionChains(self.driver)
            pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
        
        
            end_x = start_x + random.randint(-max_offset, max_offset)
            end_y = start_y + random.randint(-800, 800)  
        
            actions.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
            actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        
        except Exception as e:
            print(f"Random swipe error: {str(e)}")
            raise
        
    def select_random_country_code(self):
        """Select random country code"""
        try:
            self.driver.find_element(*self.COUNTRY_SELECTOR).click()
            time.sleep(1)
        
            self._random_scroll_and_select()
        
            return self.selected_country_code
            
        except Exception as e:
            print(f"Select country code error: {str(e)}")
            raise

    def _random_scroll_and_select(self):
        """Random scroll and select visible country code options"""
        try:
            # Get window size
            window_size = self.driver.get_window_size()
            start_x = window_size['width'] * 0.5
        
            # Define scroll area
            scroll_start_y = window_size['height'] * 0.7
            scroll_end_y = window_size['height'] * 0.3
        
            # Random scroll 2-4 times
            num_scrolls = random.randint(2, 4)
        
            # Record seen options to avoid duplicates
            seen_options = set()
        
            for _ in range(num_scrolls):
                # Get current visible options
                visible_options = self.driver.find_elements(*self.COUNTRY_CODE_OPTIONS)
            
                # Record current visible options
                for option in visible_options:
                    seen_options.add(option.text)
            
                # Randomly decide scroll direction
                if random.choice([True, False]):
                    # Scroll up
                    self.driver.swipe(start_x, scroll_start_y, start_x, scroll_end_y, duration=500)
                else:
                    # Scroll down
                    self.driver.swipe(start_x, scroll_end_y, start_x, scroll_start_y, duration=500)
                time.sleep(0.5)
        
            # Get final visible options
            final_visible_options = self.driver.find_elements(*self.COUNTRY_CODE_OPTIONS)
        
            if final_visible_options:
                # Randomly select a visible option
                selected_option = random.choice(final_visible_options)
                self.selected_country_code = selected_option.text
                selected_option.click()
                time.sleep(0.5)
            
                # Click confirm button
                self.driver.find_element(*self.COUNTRY_CODE_CONFIRM_BUTTON).click()
                time.sleep(0.5)
            else:
                raise NoSuchElementException("No country code options visible after scrolling")
            
        except Exception as e:
            print(f"Scroll and select country code error: {str(e)}")
            raise    
    
    
    def search_country_code(self):
        """Search and select a random country code"""
        self.driver.find_element(*self.COUNTRY_SELECTOR).click()
    
        try:
            # Common country code search terms
            COMMON_SEARCH_TERMS = [
            {"keyword": "台", "expected": "+886"},
            {"keyword": "香", "expected": "+852"},
            {"keyword": "日", "expected": "+81"},
            {"keyword": "美", "expected": "+1"},
            {"keyword": "英", "expected": "+44"},
            {"keyword": "新", "expected": "+65"},
            {"keyword": "澳", "expected": "+61"},
            {"keyword": "中", "expected": "+86"}
            ]
        
    
            search_term = random.choice(COMMON_SEARCH_TERMS)
        
            search_input = self.driver.find_element(*self.SEARCH_INPUT)
            search_input.click()
            search_input.send_keys(search_term["keyword"])
            time.sleep(1)
        
            result = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{search_term["expected"]}")')
        
            self.selected_country_code = result.text
            result.click()
        
            self.driver.find_element(*self.COUNTRY_CODE_CONFIRM_BUTTON).click()
            time.sleep(0.5)
        
        except Exception as e:
            print(f"Search country code error: {str(e)}")
            raise
        
    def is_country_code_changed(self):
        """Verify country code is changed"""
        try:
            time.sleep(1) 
        
            current_element = self.driver.find_element(*self.CHANGED_COUNTRY_CODE)
            current_code = current_element.text #get country code only
        
            # Extract country code from full text (e.g. from "Russia +7" extract "+7")
            selected_code = "+" + self.selected_country_code.split("+")[-1].strip().split()[0]

            # Compare country code
            is_matched = current_code == selected_code
        
            if is_matched:
                print(f"Country code is successfully updated to: {current_code}")
            else:
                print(f"Country code update failed - Expected: {selected_code}, Actual: {current_code}")
            
            return is_matched
        
        except Exception as e:
            print(f"Verify country code error: {str(e)}")
            return False
    
    # only select one service person
    def select_service_person(self):
        self.driver.find_element(*self.SERVICE_PERSON).click()
        
        # click toggle switch 
        time.sleep(1.5)
        self.driver.find_element(*self.SERVICE_PAGE_TOGGLE_SWITCH).click()
        
        # select service testing person
        service_testing_person = self.driver.find_element(*self.SERVICE_TESTING_PERSON)
        if service_testing_person:
            service_testing_person.click()
            
        # click save button
        self.driver.find_element(*self.SERVICE_PAGE_SAVE_BTN).click()
        
        return self
    
    # select multiple service person
    def select_service_multiple_personnel(self, single_choice):
        self.driver.find_element(*self.SERVICE_PERSONNEL).click()
        # Choose single or multiple selection as needed
        if single_choice:
            self.driver.find_element(*self.QA_TEST_PERSONNEL).click()
        else:
            selected_options = random.sample(self.PERSONNEL_OPTIONS, 2)
            for option in selected_options:
                self.driver.find_element(*option).click()
                
        self.driver.find_element(*self.PERSONNEL_SAVE_BUTTON).click()
        time.sleep(0.5)
        return self
    
    
    def update_items_amount(self):
        amount_edit_icon = self.driver.find_element(*self.AMOUNT_EDIT_ICON)
        amount_edit_icon.click()
        amount_input = self.driver.find_element(*self.AMOUNT_INPUT)
        random_amount = str(random.randint(10, 99))
        amount_input.send_keys(random_amount)
        self.driver.find_element(*self.AMOUNT_CLEAR_BTN).click()

        amount_input.send_keys(random_amount)
        time.sleep(0.5)
        self.driver.find_element(*self.AMOUNT_SAVE_BTN).click()
        

    def update_items_quantity(self):
        time.sleep(1)
        self.driver.find_element(*self.EDIT_ITEM_QUANTITY_ICON).click()
        try:
          if random.choice([True, False]):
             plus_button = self.driver.find_element(*self.QUANTITLY_PLUS_BUTTON)
             click_times = random.randint(5,8)
             for _ in range(click_times):
                plus_button.click()
                time.sleep(0.5)
          else:
             quantity_input = self.driver.find_element(*self.QUANTITY_REVISE_INPUT)
             time.sleep(1)
             quantity_input.click()
             random_quantity = str(random.randint(5, 99))
             quantity_input2 = self.driver.find_element(*self.QUANTITY_REVISE_INPUT2)
             quantity_input2.click()
             quantity_input2.send_keys(random_quantity)
          
          self.driver.find_element(*self.QUANTITY_REVISE_SAVE_BTN).click()
        
        except Exception as e:
            print(f"Error updating items quantity: {str(e)}")
            raise
    
    def remove_item(self):
        time.sleep(1)
        self.driver.find_element(*self.REMOVE_ITEM_BTN).click()
        remove_confirm_btn = self.driver.find_element(*self.REMOVE_CONFIRM_BTN)
        if remove_confirm_btn.is_displayed() and remove_confirm_btn.is_enabled():
            remove_confirm_btn.click()
        
        time.sleep(0.5)
        back_to_previous_page_icon = self.driver.find_element(*self.BACK_TO_PREVIOUS_PAGE_ICON)
        back_to_previous_page_icon.click() 
    
    def add_new_discount(self, add_new_member=False):
        self.driver.find_element(*self.ADD_NEW_DISCOUNT_BTN).click()
        time.sleep(1)
        
        #randomly select tab
        tabs = [self.CASH_TAB, self.DISCOUNT_TAB]
        if not add_new_member:
            tabs.append(self.COUPON_TAB)
            
        selected_tab = random.choice(tabs)
        self.driver.find_element(*selected_tab).click()
        time.sleep(1)
        
        if selected_tab == self.CASH_TAB:
            self._handle_cash_tab()
        elif selected_tab == self.DISCOUNT_TAB:
            self._handle_discount_tab()
        else:
            self._handle_coupon_tab()
            
        self.driver.find_element(*self.DISCOUNT_SAVE_BUTTON).click()
    
    def _handle_cash_tab(self):
        if random.choice([True, False]):
            input_field = self.driver.find_element(*self.AMOUNT_INPUT_FIELD)
            input_field.click()
            random_amount = str(random.randint(10, 99))
            input_field.send_keys(random_amount)
        else:
            amount = random.choice(self.CASH_QUICK_AMOUNTS)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{amount}")').click()
            
    def _handle_discount_tab(self):
        if random.choice([True, False]):
            input_field = self.driver.find_element(*self.DISCOUNT_INPUT_FIELD)
            input_field.click()
            random_discount = str(random.choice(self.DISCOUNT_INPUT_OPTIONS))
            input_field.send_keys(random_discount)
        else:
            discount = random.choice(self.DISCOUNT_QUICK_RATES)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{discount}")').click()
            
    def _handle_coupon_tab(self):
        self.driver.find_element(*self.AUTO_TEST_COUPON).click()
        time.sleep(1)
        
        self.driver.find_element(*self.SELECT_TICKET_ICON).click()
        time.sleep(1.5)
        
        # Get window size for swipe calculation
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.5
        start_y = window_size['height'] * 0.7
        end_y = window_size['height'] * 0.6
        
        
        # Select random quantity (1-11)
        random_quantity = str(random.randint(1, 11))
        
        # Perform small swipe gesture
        self.driver.swipe(start_x, start_y, start_x, end_y, duration=500)
        time.sleep(1)
        
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{random_quantity}")').click()
        time.sleep(0.5)
        
        # Input amount
        amount_input = self.driver.find_element(*self.QUANTITY_INPUT)
        amount_input.click()
        random_amount = str(random.randint(1, 100))
        amount_input.clear()
        amount_input.send_keys(random_amount)
            
    
    def new_member(self):
        
        # generate random phone number
        first_digit = '9' # first digit cannot be 1
        rest_digits = ''.join(random.choice('0123456789') for _ in range(8))
        phone_number = first_digit + rest_digits
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone_number)
        
        time.sleep(0.5)
        # Generate random name
        nickname_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?" + "QA測試文字在這裡qa_test"
        nickname = ''.join(random.choice(nickname_chars) for _ in range(5))
        self.driver.find_element(*self.NICKNAME_INPUT).send_keys(nickname)
        
        # select random gender
        self.select_random_gender()
        time.sleep(0.5)
        # select random date
        self.select_random_date()
        
        # Generate random member description -> Due to id cannot be found, so we won't use it anymore
        description = ''.join(random.choice(nickname_chars) for _ in range(20))
        self.driver.find_element(*self.MEMBER_DESCRIPTION_INPUT).click()
        time.sleep(0.5)
        self.driver.find_element(*self.MEMBER_DESCRIPTION_MODAL_INPUT).send_keys(description)
        self.driver.find_element(*self.MEMBER_DESCRIPTION_MODAL_SAVE_BUTTON).click()
        
        #self.driver.find_element(*self.ADD_NEW_MEMBER_TOGGLE).click()
        
        # Click save button
        time.sleep(0.5)
        try:
            self.driver.find_element(*self.SAVE_NEW_MEMBER_BUTTON).click()
        except:
            pass
        
        
        
        