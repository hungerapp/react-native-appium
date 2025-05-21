import random
import time
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from datetime import datetime, timedelta

from pages.shared_components.common_action import CommonActions

class CommonUseSection(CommonActions):
    GENDER_OPTIONS = {
        "男": (AppiumBy.ACCESSIBILITY_ID, "男"),
        "女": (AppiumBy.ACCESSIBILITY_ID, "女"),
        "其他": (AppiumBy.ACCESSIBILITY_ID, "其他")
    }
    CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")')
    CALENDAR_WINDOW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/pickers")')

    COUNTRY_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down")')
    COUNTRY_CODE_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '+')]")
    CHANGED_COUNTRY_CODE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+")')
    COUNTRY_CODE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    CHANGED_COUNTRY_CODE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("+")')
    COUNTRY_CODE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)') 
    SEARCH_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入國家或號碼進行搜尋")')
    
    
    # select service
    TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
    SERVICE_TAB_CONTAINER = (AppiumBy.XPATH, "//android.widget.HorizontalScrollView/android.view.ViewGroup")
    AUTO_TEST_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試服物分類")')
    SERVICE_ITEMS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("測試服務")')
    SAVE_SERVICE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
    SERVICE_OPTION1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務1")')
    SERVICE_OPTION4 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務4")')
    SUB_SERVICE_SAVE_BTN = (AppiumBy.ACCESSIBILITY_ID, '選擇子服務-modal-right-button ')
    SUB_SERVICE_OPTIONS = {
        '附加服務1': (AppiumBy.ACCESSIBILITY_ID, 'checkbox-multiple-option-0'),
        '附加服務2': (AppiumBy.ACCESSIBILITY_ID, 'checkbox-multiple-option-1'),
        '附加服務3': (AppiumBy.ACCESSIBILITY_ID, 'checkbox-multiple-option-2'),
      }
    
    
    
    SERVICE_PERSON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    SERVICE_TESTING_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'checkbox-single-option-0')
    SERVICE_PAGE_TOGGLE_SWITCH = (AppiumBy.ACCESSIBILITY_ID, '該筆預約為指定預約-switch-button')
    SERVICE_PAGE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check")')
    
    SERVICE_PERSONNEL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    QA_TEST_PERSONNEL = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SELECT_ALL_OPTION = (AppiumBy.ACCESSIBILITY_ID, '全部選取')
    PERSONNEL_OPTIONS = [
        (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲'),
        (AppiumBy.ACCESSIBILITY_ID, 'Bella #美甲'),
        # Add more personnel options as needed
    ]
    PERSONNEL_SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check").instance(1)')
    
    
    # For checkout, request page
    AMOUNT_EDIT_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("pen-to-square").instance(0)')
    AMOUNT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    AMOUNT_CLEAR_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("清除")')
    AMOUNT_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    EDIT_ITEM_QUANTITY_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("caret-down").instance(1)')
    QUANTITY_PLUS_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="plus"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    QUANTITY_REVISE_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'undefined-number-field-input')
    QUANTITY_REVISE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    REMOVE_ITEM_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("circle-minus").instance(0)')
    REMOVE_CONFIRM_BTN = (AppiumBy.ACCESSIBILITY_ID, '移除')
    BACK_TO_PREVIOUS_PAGE_ICON = (AppiumBy.ACCESSIBILITY_ID, 'arrow-left')
    ADD_NEW_DISCOUNT_BTN = (AppiumBy.ACCESSIBILITY_ID, '新增')
    DISCOUNT_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
    CASH_QUICK_AMOUNTS = ["50", "100", "150", "200", "250", "300", "350", "400"]
    DISCOUNT_QUICK_RATES = ["95折", "92折", "9折", "88折", "85折", "8折", "75折", "7折"]
    DISCOUNT_INPUT_OPTIONS = [90, 85, 95, 80, 70, 85, 75]
    CASH_TAB = (AppiumBy.ACCESSIBILITY_ID, '現金')
    DISCOUNT_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("折數")')
    COUPON_TAB = (AppiumBy.ACCESSIBILITY_ID, '票券')
    # Input fields and buttons
    AMOUNT_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, '金額-text-input')
    DISCOUNT_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, '折數-text-input')
    QUICK_SELECT_AMOUNTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView")')
    AUTO_TEST_COUPON = (AppiumBy.ACCESSIBILITY_ID, '自動化測試票券')
    SELECT_TICKET_ICON = (AppiumBy.ACCESSIBILITY_ID, '1 張')
    QUANTITY_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'undefined-text-input')
    NO_COUPON_AVAILABLE_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("目前沒有資料")')
    
    # for add new member
    PHONE_NUMBER_INPUT = (AppiumBy.ACCESSIBILITY_ID, '電話-text-input')
    NICKNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, '別名-text-input')
    ADD_NEW_MEMBER_CHOOSE_DATE_FIELD = (AppiumBy.ACCESSIBILITY_ID, '生日, 選填, 請選擇')
    MEMBER_DESCRIPTION_INPUT = (AppiumBy.ACCESSIBILITY_ID, '會員描述-textarea-field')
    MEMBER_DESCRIPTION_MODAL_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
    MEMBER_DESCRIPTION_MODAL_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'circle-check')
    ADD_NEW_MEMBER_TOGGLE = (AppiumBy.ACCESSIBILITY_ID, '是否加入黑名單-switch-button')
   
    SAVE_NEW_MEMBER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'check')
    SAVE_NAV_NEW_MEMBER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'createMemberOnSubmit')
    RIGHT_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-right")')      
    LEFT_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("arrow-left")')
    
    def __init__(self, driver):
        super().__init__(driver)
        
    ############# Used Gestures for Common Use components #############
    def _perform_random_swipe(self, start_x, start_y, max_offset=50):
        """Execute random swipe"""
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
        
    def swipe_gesture(self, x, y, width, height, direction='up', percent=0.6, speed=1000):
        """
        通用滑動手勢
        Args:
         x (int): 起始 X 座標
         y (int): 起始 Y 座標
         width (int): 滑動區域寬度
         height (int): 滑動區域高度
         direction (str): 滑動方向 ('up', 'down', 'left', 'right')
         percent (float): 滑動百分比 (0.0-1.0)
         speed (int): 滑動速度（毫秒）
        """
        try:
          self.driver.execute_script('mobile: swipeGesture', {
            'left': x,
            'top': y,
            'width': width,
            'height': height,
            'direction': direction,
            'percent': percent,
            'speed': speed
          })
        except:
         print(f"Swipe gesture error")
    ###############################################    
    
    def swipe_calendar_component(self):
        # Get date picker window
        calendar_window = self.find_element(*self.CALENDAR_WINDOW)
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
        self.click_element(*self.CONFIRM_BUTTON)      
        
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
        
    def select_random_country_code(self):
        """Select random country code"""
        try:
            self.click_element(*self.COUNTRY_SELECTOR)
        
            self._random_scroll_and_select()
        
            return self.selected_country_code
            
        except Exception as e:
            print(f"Select country code error: {str(e)}")
            raise

    def _random_scroll_and_select(self):
        """Random scroll and select visible country code options"""
        try:
            # Get window size
            window_size = self.get_screen_size()
            start_x = window_size[0] * 0.5
        
            # Define scroll area
            scroll_start_y = window_size[1] * 0.7
            scroll_end_y = window_size[1] * 0.3
        
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
                    self.swipe(start_x, scroll_start_y, start_x, scroll_end_y, duration=500)
                else:
                    # Scroll down
                    self.swipe(start_x, scroll_end_y, start_x, scroll_start_y, duration=500)
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
                self.click_element(*self.COUNTRY_CODE_CONFIRM_BUTTON)
                time.sleep(0.5)
            else:
                raise NoSuchElementException("No country code options visible after scrolling")
            
        except Exception as e:
            print(f"Scroll and select country code error: {str(e)}")
            raise    
    
    
    def search_country_code(self):
        """Search and select a random country code"""
        self.click_element(*self.COUNTRY_SELECTOR)
    
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
        
            self.click_element(*self.SEARCH_INPUT)
            self.driver.find_element(*self.SEARCH_INPUT).send_keys(search_term["keyword"])
        
            result = self.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{search_term["expected"]}")')
        
            self.selected_country_code = result.text
            result.click()
        
            self.click_element(*self.COUNTRY_CODE_CONFIRM_BUTTON)
        
        except Exception as e:
            print(f"Search country code error: {str(e)}")
            raise
        
    def is_country_code_changed(self):
        """Verify country code is changed"""
        try:
            time.sleep(1) 
        
            current_element = self.find_element(*self.CHANGED_COUNTRY_CODE)
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
        time.sleep(1)
        self.is_element_visible(*self.SERVICE_PERSON)
        self.click_element(*self.SERVICE_PERSON)
        
        # click toggle switch 
        self.click_element(*self.SERVICE_PAGE_TOGGLE_SWITCH)
        
        # select service testing person
        self.click_element(*self.SERVICE_TESTING_PERSON)
            
        # click save button
        self.click_element(*self.SERVICE_PAGE_SAVE_BTN)
        
        return self
    
    # select multiple service person
    def select_service_multiple_personnel(self, single_choice):
        self.click_if_exists(*self.SERVICE_PERSONNEL)
        # Choose single or multiple selection as needed
        if single_choice:
            self.click_element(*self.QA_TEST_PERSONNEL)
        else:
            selected_options = random.sample(self.PERSONNEL_OPTIONS, 2)
            for option in selected_options:
                self.click_element(*option)
                
        self.click_element(*self.PERSONNEL_SAVE_BUTTON)
        time.sleep(0.5)
        return self
    
    def select_service(self):
        self.swipe_and_find_tab()
        # Select specific services under AUTO_TEST_TAB
        try:
            service1 = self.find_element(*self.SERVICE_OPTION1)
            service4 = self.find_element(*self.SERVICE_OPTION4)

            service4.click()
            time.sleep(0.5)
            self.handle_sub_services()
            
            time.sleep(2)
            service1.click()

            # Click save button
            self.click_element(*self.SAVE_SERVICE_BTN)

        except Exception as e:
            print(f"Error selecting services: {str(e)}")

        return self
    
    def swipe_and_find_tab(self, target_tab_locator=AUTO_TEST_TAB, max_attempts=5):
        """args: target_tab_locator is the locator of the tab to be found
           ex. self.swipe_and_find_tab(CreateRequestLocators.AUTO_TEST_TAB)
           instead of using *CreateRequestLocators.AUTO_TEST_TAB
        """
        try:
            tab_container = self.find_element(*self.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location

            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
            y = location['y'] + int(size['height'] * 0.5)

            max_attempts = 5
            found_target = False

            for _ in range(max_attempts):
                self.swipe(start_x, y, end_x, y, 100)
                time.sleep(0.5)
                try:
                    self.click_element(*target_tab_locator)
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
    
    
    def handle_sub_services(self):
        """
        Handle sub-services modal if it appears:
        1. Always select 2 options from predefined options
        2. Click selected options using description
        3. Click save button
        """
        
        try:
            # Randomly select two options
            selected_keys = random.sample(list(self.SUB_SERVICE_OPTIONS.keys()), 2)
            
            # Click selected options
            for key in selected_keys:
                option_locator = self.SUB_SERVICE_OPTIONS[key]
                try:
                    self.click_element(*option_locator)
                except NoSuchElementException:
                    continue
            
            # Click save button for sub-service
            self.click_element(*self.SUB_SERVICE_SAVE_BTN)
            
        except Exception as e:
            return False

    def update_items_amount(self):
        self.click_element(*self.AMOUNT_EDIT_ICON)
        time.sleep(0.5)
        self.driver.find_element(*self.AMOUNT_INPUT).send_keys(str(random.randint(10, 99)))
        self.click_element(*self.AMOUNT_CLEAR_BTN)
        time.sleep(0.5)
        self.driver.find_element(*self.AMOUNT_INPUT).send_keys(str(random.randint(10, 99)))
        time.sleep(0.5)
        self.driver.find_element(*self.AMOUNT_SAVE_BTN).click()
        
    def update_items_quantity(self):
        self.driver.find_element(*self.EDIT_ITEM_QUANTITY_ICON).click()
        try:
          if random.choice([True, False]):
             plus_button = self.driver.find_element(*self.QUANTITY_PLUS_BUTTON)
             click_times = random.randint(5,8)
             for _ in range(click_times):
                plus_button.click()
                time.sleep(0.5)
          else: 
             random_quantity = str(random.randint(5, 99))
             self.driver.find_element(*self.QUANTITY_REVISE_INPUT).click()
             self.driver.find_element(*self.QUANTITY_REVISE_INPUT).send_keys(random_quantity)
          
          self.driver.find_element(*self.QUANTITY_REVISE_SAVE_BTN).click()
        
        except Exception as e:
            print(f"Error updating items quantity: {str(e)}")
            raise
    
    def remove_item(self):
        self.click_element(*self.REMOVE_ITEM_BTN)
        self.is_element_visible(*self.REMOVE_CONFIRM_BTN)
        self.click_element(*self.REMOVE_CONFIRM_BTN)
        self.click_element(*self.BACK_TO_PREVIOUS_PAGE_ICON)
    
    def add_new_discount(self, existing_member=False):
        self.is_element_visible(*self.ADD_NEW_DISCOUNT_BTN)
        self.click_element(*self.ADD_NEW_DISCOUNT_BTN)
        
        #randomly select tab
        tabs = [self.CASH_TAB, self.DISCOUNT_TAB]
        if existing_member == True:
            tabs.append(self.COUPON_TAB)
            
        selected_tab = random.choice(tabs)
        self.driver.find_element(*selected_tab).click()
        
        if selected_tab == self.CASH_TAB:
            self._handle_cash_tab()
        elif selected_tab == self.DISCOUNT_TAB:
            self._handle_discount_tab()
        else:
            self._handle_coupon_tab()
            
        self.click_element(*self.DISCOUNT_SAVE_BUTTON)
    
    def _handle_cash_tab(self):
        if random.choice([True, False]):
            self.click_element(*self.AMOUNT_INPUT_FIELD)
            random_amount = str(random.randint(10, 99))
            self.driver.find_element(*self.AMOUNT_INPUT_FIELD).send_keys(random_amount)
        else:
            amount = random.choice(self.CASH_QUICK_AMOUNTS)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{amount}")').click()
            
    def _handle_discount_tab(self):
        if random.choice([True, False]):
            self.click_element(*self.DISCOUNT_INPUT_FIELD)
            random_discount = str(random.choice(self.DISCOUNT_INPUT_OPTIONS))
            self.driver.find_element(*self.DISCOUNT_INPUT_FIELD).send_keys(random_discount)
        else:
            discount = random.choice(self.DISCOUNT_QUICK_RATES)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{discount}")').click()
            
    def _handle_coupon_tab(self):
        self.click_element(*self.AUTO_TEST_COUPON)
        
        try:
            self.click_element(*self.SELECT_TICKET_ICON)

            time.sleep(1.5)
        
            # Get window size for swipe calculation
            window_size = self.get_screen_size()
            start_x = window_size[0] * 0.5
            start_y = window_size[1] * 0.7
            end_y = window_size[1] * 0.6
        
            # Select random quantity (1-17)
            random_quantity = random.randint(1, 17)
        
            # Perform small swipe gesture
            self.swipe(start_x, start_y, start_x, end_y, duration=500)
            time.sleep(1)
        
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{random_quantity}")').click()
            time.sleep(0.5)
        
            # Input amount
            self.driver.find_element(*self.QUANTITY_INPUT).click()
            random_amount = str(random.randint(1, 100))
            self.driver.find_element(*self.QUANTITY_INPUT).clear()
            self.driver.find_element(*self.QUANTITY_INPUT).send_keys(random_amount)
            
        except Exception as e:
            print(f"Error handling coupon tab: {str(e)}")
            raise
    
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
        # click birthday field to open date picker
        self.click_element(*self.ADD_NEW_MEMBER_CHOOSE_DATE_FIELD)
        self.swipe_calendar_component()
        
        # Generate random member description -> Due to id cannot be found, so we won't use it anymore
        description = ''.join(random.choice(nickname_chars) for _ in range(20))
        self.click_element(*self.MEMBER_DESCRIPTION_INPUT)
        time.sleep(0.5)
        self.driver.find_element(*self.MEMBER_DESCRIPTION_MODAL_INPUT).send_keys(description)
        self.click_element(*self.MEMBER_DESCRIPTION_MODAL_SAVE_BUTTON)
        
        self.click_element(*self.ADD_NEW_MEMBER_TOGGLE)
        
        # Click save button
        time.sleep(0.5)
        try:
            self.click_element(*self.SAVE_NEW_MEMBER_BUTTON)
        except:
            self.click_element(*self.SAVE_NAV_NEW_MEMBER_BUTTON)
        
    def choose_date(self, clicks=3):
        for _ in range(clicks):
            self.is_element_visible(*self.RIGHT_ARROW)
            self.click_element(*self.RIGHT_ARROW)
            time.sleep(1)
          
        dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
        
        random.choice(dates).click()
        
        # click outside to close the date window
        self.tap(0.5, 0.9)
        
    def sign_request(self):
        """simulate the signature, draw the "王" in the left top corner"""
        try:
            signature_pad = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Image")
            size = signature_pad.size

            left = 0.02
            right = 0.2
            top = 0.03
            mid = 0.1
            bottom = 0.2

            strokes = [
                # first stroke: top horizontal line
                [(left, top), (right, top)],
                # second stroke: middle horizontal line
                [(left, mid), (right, mid)],
                # third stroke: bottom horizontal line
                [(left, bottom), (right, bottom)],
                # fourth stroke: middle vertical line
                [((left+right)/2, top), ((left+right)/2, bottom+0.03)]
            ]

            for stroke in strokes:
                actions = ActionChains(self.driver)
                start_x = size['width'] * stroke[0][0]
                start_y = size['height'] * stroke[0][1]
                end_x = size['width'] * stroke[1][0]
                end_y = size['height'] * stroke[1][1]

                actions.move_to_element_with_offset(signature_pad, start_x, start_y)
                actions.click_and_hold()
                actions.move_to_element_with_offset(signature_pad, end_x, end_y)
                actions.release()
                actions.perform()
                time.sleep(0.2)
        except Exception as e:
            print(f"Error during signing: {str(e)}")
            raise
        
    @staticmethod
    def get_current_timestamp():
        """
        Generates the current timestamp in YYYYMMDDHHMMSSmmm format
        """
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S") + f"{int(now.microsecond / 1000):03d}"
        return timestamp

    @staticmethod
    def replace_current_datetime(input_string):
        if "<current_datetime>" in input_string:
            current_datetime = datetime.now().strftime("%Y/%m/%d")
            return input_string.replace("<current_datetime>", current_datetime)
        return input_string

    @staticmethod
    def add_days_to_date(today, days):
        today_date = datetime.now()  # 抓取今天的日期
        new_date = today_date + timedelta(days=days)
        return new_date.strftime("%Y/%m/%d")  # 格式化為 "YYYY/MM/DD"
