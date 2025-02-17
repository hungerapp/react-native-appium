import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


from pages.shared_components.common_use import CommonUseSection

class CreateAppointmentPage(CommonUseSection):
    def __init__(self, driver):
        self.driver = driver
        
    # Basic element locators
    PERSONAL_PAGE_BACK_TO_CALENDAR_BTN = (AppiumBy.ACCESSIBILITY_ID, '返回')
    CREATE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(14)')
    CREATE_APPOINTMENT_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(7)')
    CONTACT_INFO_SECTION = (AppiumBy.ACCESSIBILITY_ID, '匿名')
    SERVICE_PERSON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    SERVICE_TESTING_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SERVICE2_PERSON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("請選擇").instance(0)')
    SERVICE_OTHER_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'Sally #美睫 #美甲')
    SERVICE_PAGE_TOGGLE_SWITCH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(31)')
    SERVICE_PAGE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)')
    SERVICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務")')
    TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
    SERVICE_TAB_CONTAINER = (AppiumBy.XPATH, "//android.widget.HorizontalScrollView/android.view.ViewGroup")
    AUTO_TEST_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試服物分類")')
    SERVICE_ITEMS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("測試服務")')
    SAVE_SERVICE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    SUB_SERVICE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    CHANGE_SERVICE_TIME_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    CHANGE_SERVICE_PERSON_COUNT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    BACK_TO_CALENDAR_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    
    MEMBER_PASSPORT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("查看會員護照")')
    MEMBER_PASSPORT_BACK_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    
    
    # Locators for service time and quantity
    SERVICE_TIME_MINUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(9)')
    SERVICE_TIME_PLUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(10)')
    QUANTITY_MINUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(12)')
    QUANTITY_PLUS_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(13)')

    
    # Note only for business
    NOTE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("筆記 (僅商家可見)")')
    NOTE_CONTENT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入內容")')
    MODAL_NOTE_CONTENT_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("輸入內容")')
    
    MODAL_NOTE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    NOTE_CONTENT_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    
    ADD_ONE_MORE_SERVICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("再新增一筆預約")')
    DELETE_SERVICE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(12)')
    
    #  Unexpected Cancel  related elements
    CONTACT_CANCEL_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    SERVICE_CANCEL_BTN = (AppiumBy.ACCESSIBILITY_ID, '離開')
    
    # Time section related elements
    TIME = (AppiumBy.XPATH, '//android.widget.TextView[@text="預約時間"]')
    TIME_CONTAINER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(57)')
    TIME_SLOTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(":")')
    DATE_BLOCK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(3)')
    LEFT_DATE_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    RIGHT_DATE_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    TODAY_TIME_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("今天")')
    LEFT_TIME_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(4)')
    RIGHT_TIME_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(5)')
    SAVE_TIME_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    SELECT_BUSY_TIME = (AppiumBy.ACCESSIBILITY_ID, '確定')
    DEPOSIT_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(18)')
    CONFIRM_CREATE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增預約')

    
    # Contact related elements
    PHONE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入電話")')
    NAME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入姓名")')
    PHONE_SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '電話搜尋')
    NAME_SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '姓名搜尋')
    SPECIFIC_SEARCH_RESULT = (AppiumBy.ACCESSIBILITY_ID, '+886 972 205690, 王貝克 先生 (Beck), 上次預約姓名： 王貝克')
    CHANGE_SPECIFIC_SEARCH_RESULT = (AppiumBy.ACCESSIBILITY_ID, '+886 911 111116, Wei 先生, 上次預約姓名： Wei')
    SAVE_CONTACT_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    INVALID_PHONE_MSG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 格式錯誤。")')
    CONTACT_BACK_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    CONTACT_HAS_CHOSEN = (AppiumBy.ACCESSIBILITY_ID, '+886 972 205690, 王貝克 先生 (Beck)')
    CONTACT_PHONE_CHANGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("972205690")')
     

    
    def personal_page_back_to_calendar(self):
        """Click back to calendar button"""
        self.driver.find_element(*self.PERSONAL_PAGE_BACK_TO_CALENDAR_BTN).click()
        time.sleep(3)
        return self
    
    
    def create_appointment(self):
        """Click create appointment button"""
        
        try:
          time.sleep(1)
          create_button = self.driver.find_element(*self.CREATE_BTN)
          if create_button.is_displayed() and create_button.is_enabled():
              create_button.click()
                    
        except NoSuchElementException:
          raise NoSuchElementException("Unable to find create appointment button after multiple attempts")
      
        self.driver.find_element(*self.CREATE_APPOINTMENT_OPTION).click()
        return self
      
    def click_contact_info_section(self):
        """Click contact info section"""
        self.driver.find_element(*self.CONTACT_INFO_SECTION).click()
        return self

    def fill_anonymous_contact(self):
        """Fill in contact info as anonymous"""
        self.driver.find_element(*self.CONTACT_INFO_SECTION).click()
        try: 
           name_save_btn = self.driver.find_element(*self.SAVE_CONTACT_BUTTON)
           if name_save_btn.is_displayed() and name_save_btn.is_enabled():
               name_save_btn.click()
        except NoSuchElementException:
            raise NoSuchElementException("Unable to find save contact button after multiple attempts")
        
        time.sleep(2)
        return self

    def fill_existing_contact(self, test_name, test_phone):
        """Fill in contact info with existing contact"""
        self.driver.find_element(*self.CONTACT_INFO_SECTION).click()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(test_phone)
        self.driver.find_element(*self.NAME_INPUT).send_keys(test_name)
        time.sleep(1)
        self.select_random_gender()
        self.driver.find_element(*self.SAVE_CONTACT_BUTTON).click()
        return self
      
    def check_member_passport(self):
        """Check member passport"""
        self.driver.find_element(*self.MEMBER_PASSPORT_BTN).click()
        assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("會員護照")').is_displayed()
        self.driver.find_element(*self.MEMBER_PASSPORT_BACK_BTN).click()
        return self

    def select_service_person(self):
        """Select first available service person"""
        self.driver.find_element(*self.SERVICE_PERSON).click()
        
        # click toggle switch 
        time.sleep(3)
        self.driver.find_element(*self.SERVICE_PAGE_TOGGLE_SWITCH).click()
        
        # select service testing person
        service_testing_person = self.driver.find_element(*self.SERVICE_TESTING_PERSON)
        if service_testing_person:
            service_testing_person.click()
            
        # click save button
        self.driver.find_element(*self.SERVICE_PAGE_SAVE_BTN).click()
        
        return self
      
    def select_service2_person(self):
        """Select second service person"""
        self.driver.find_element(*self.SERVICE2_PERSON).click()
        self.driver.find_element(*self.SERVICE_PAGE_TOGGLE_SWITCH).click()
        self.driver.find_element(*self.SERVICE_OTHER_PERSON).click()
        self.driver.find_element(*self.SERVICE_PAGE_SAVE_BTN).click()
        return self

    def handle_sub_services(self):
        """
        Handle sub-services modal if it appears:
        1. Always select 2 options from predefined options
        2. Click selected options using description
        3. Click save button
        """
        SUB_SERVICE_OPTIONS = {
            "option1": "附加服務1, +30 分鐘 / +NT$500",
            "option2": "附加服務2, +30 分鐘 / +NT$500",
            "option3": "附加服務3, +30 分鐘 / +NT$500"
        }
        
        try:
            num_to_select = 2
            selected_options = random.sample(list(SUB_SERVICE_OPTIONS.values()), num_to_select)
            
            for description in selected_options:
                try:
                    option_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{description}")')
                    option_element = self.driver.find_element(*option_locator)
                    option_element.click()
                except NoSuchElementException:
                    continue
            
            # Click save button for sub-service
            sub_save_button = self.driver.find_element(*self.SUB_SERVICE_SAVE_BTN)
            if sub_save_button.is_displayed():
                sub_save_button.click()
            else:
                print("Sub-service save button is not visible or enabled")
            return True
            
        except Exception as e:
            print(f"Error handling sub-services: {str(e)}")
            return False

    def select_service(self):
        """
        1. Click service selection button
        2. Immediately swipe through tabs
        3. Find and click AUTO_TEST_TAB
        4. Select specific services
        5. Handle sub-services if modal appears
        """
        # Click service selection button and wait for page to load
        self.driver.find_element(*self.SERVICE).click()

        try:
            tab_container = self.driver.find_element(*self.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location

            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
            y = location['y'] + int(size['height'] * 0.5)

            max_attempts = 5
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

        # Select specific services under AUTO_TEST_TAB
        try:
            service1 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務1")')
            service4 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("測試服務4")')

            service4.click()
            time.sleep(0.5)
            self.handle_sub_services()
            
            service1.click()

            # Click save button
            save_button = self.driver.find_element(*self.SAVE_SERVICE_BTN)
            save_button.click()

        except Exception as e:
            print(f"Error selecting services: {str(e)}")

        return self
      
  
    def change_service_time_and_service_person(self):
        """Randomly change service time and quantity"""
        
        # Randomly click service time plus or minus button
        time_clicks = random.randint(1, 5)
        for _ in range(time_clicks):
            if random.choice([True, False]):
                self.driver.find_element(*self.SERVICE_TIME_PLUS_BTN).click()
            else:
                self.driver.find_element(*self.SERVICE_TIME_MINUS_BTN).click()
            time.sleep(0.5)

        # Randomly click quantity plus or minus buttonick quantity plus or minus button
        quantity_clicks = random.randint(1, 5)
        for _ in range(quantity_clicks):
            if random.choice([True, False]):
                self.driver.find_element(*self.QUANTITY_PLUS_BTN).click()
            else:
                self.driver.find_element(*self.QUANTITY_MINUS_BTN).click()
            time.sleep(0.5)

        return self
        
    def note_input(self):
        """Input random note with mixed characters"""
        time.sleep(2)
        self.driver.find_element(*self.NOTE_INPUT).click()
        
       
        characters = string.ascii_letters + string.digits + string.punctuation + "夯客測試開發"
        random_note = ''.join(random.choices(characters, k=30))
      
        note_input_field = self.driver.find_element(*self.NOTE_CONTENT_INPUT)
        note_input_field.click()
        time.sleep(0.5)
        note_modal_input_field = self.driver.find_element(*self.MODAL_NOTE_CONTENT_INPUT)
        note_modal_input_field.click()
        note_modal_input_field.send_keys(random_note)
        
        time.sleep(0.5)
        self.driver.find_element(*self.MODAL_NOTE_SAVE_BTN).click()
        self.driver.find_element(*self.NOTE_CONTENT_SAVE_BTN).click()
        
        return self
      
    def add_service(self):
        """Add one more service"""
        self.driver.find_element(*self.ADD_ONE_MORE_SERVICE).click()
        return self
      
    
    def click_one_more_service(self):
        add_service_element = self.driver.find_element(*self.ADD_ONE_MORE_SERVICE)
        if add_service_element.is_displayed():
                add_service_element.click()
        
        time.sleep(2)
    
    def one_more_service(self):
        """Add one more service"""
        
        self.select_service2_person()
        self.select_service()
        return self

    def delete_service(self):
        """Delete one service"""
        self.driver.find_element(*self.DELETE_SERVICE_BTN).click()
        return self
      

    def select_appointment_time(self):
        """
        1. Must scroll to very bottom of screen first
        2. Only after reaching bottom, find and click time picker
        3. Select random time slot
        """
        try:
            window_size = self.driver.get_window_size()
            
            
            right_edge_x = window_size['width'] * 0.95
            
    
            start_y = window_size['height'] * 0.95  
            mid_y = window_size['height'] * 0.65    
            end_y = window_size['height'] * 0.35   
            
            
        
            self.driver.swipe(
                right_edge_x,
                start_y,
                right_edge_x,
                mid_y,
                2000
            )
            
          
            self.driver.swipe(
                right_edge_x,
                mid_y,
                right_edge_x,
                end_y,
                2000
            )
            
         
            self.driver.swipe(
                right_edge_x,
                end_y * 1.2,
                right_edge_x,
                end_y,
                500
            )
            
          
            time_xpath = '//android.widget.TextView[@text="預約時間"]'
            time_element = self.driver.find_element(AppiumBy.XPATH, time_xpath)
            
            if time_element and time_element.is_displayed():
                location = time_element.location
                size = time_element.size
                click_x = location['x'] + (size['width'] // 2)
                click_y = location['y'] + (size['height'] // 2)
                
                self.driver.tap([(click_x, click_y)], 500)
                time.sleep(2)
                
                # click date block
                date_block = self.driver.find_element(*self.DATE_BLOCK)  
                date_block.click()
                time.sleep(1)
                
                # select random date
                direction = random.choice(['left', 'right'])
                if direction == 'left':
                    arrow = self.driver.find_element(*self.LEFT_DATE_ARROW)
                else:
                    arrow = self.driver.find_element(*self.RIGHT_DATE_ARROW)
                arrow.click()
                
                dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
      
                random.choice(dates).click()
                
                # Control page (left, right, today button)

                today_button = self.driver.find_element(*self.TODAY_TIME_BUTTON)
                left_arrow = self.driver.find_element(*self.LEFT_TIME_ARROW)
                right_arrow = self.driver.find_element(*self.RIGHT_TIME_ARROW)

                buttons = [today_button, left_arrow, right_arrow]


                random_buttons = random.sample(buttons, 2)
                for button in random_buttons:
                    button.click()
                    time.sleep(0.5)
                
                
                
                time_slots = self.driver.find_elements(*self.TIME_SLOTS)
                if time_slots:
                    random_slot = random.choice(time_slots)
                    random_slot.click()
                    time.sleep(1)
                    
                    save_btn = self.driver.find_element(*self.SAVE_TIME_BTN)
                    if save_btn.is_displayed():
                        save_btn.click()
                        try:
                            self.driver.find_element(*self.SELECT_BUSY_TIME).click()
                        except:
                            print("Unable to select time slot")
                else:
                    print("No available time slots found")
            else:
                print("Time picker element is not visible")
        
        except Exception as e:
            print(f"Error selecting appointment time: {str(e)}")
        
        return self

    
    def select_deposit_options(self):
        """
        Randomly toggle two specific deposit options and save.
        """
        time.sleep(2)
        deposit_btn = self.driver.find_element(*self.DEPOSIT_BTN)
        deposit_btn.click()
        
        try:
  
            toggle1 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(16)')
            toggle2 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(23)')

            # randomly click two specific deposit options
            for toggle in [toggle1, toggle2]:
                if random.choice([True, False]):
                    toggle.click()
                    time.sleep(0.5)

            # Click save button
            save_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
            if save_button.is_displayed():
                save_button.click()
            else:
                print("Save button is not visible or enabled")

        except Exception as e:
            print(f"Error selecting deposit options: {str(e)}")
    
    
    def click_create_button(self):
        """Click confirm create appointment button"""
        self.driver.find_element(*self.CONFIRM_CREATE_BUTTON).click()
        return self


    # Contact related methods
    def enter_phone_number(self, phone_number):
        """Enter phone number in contact info section"""
        phone_input = self.driver.find_element(*self.PHONE_INPUT)
        phone_input.send_keys(phone_number)
        return self
    
    def enter_name(self, name):
        """Enter name in contact info section"""
        name_input = self.driver.find_element(*self.NAME_INPUT)
        name_input.send_keys(name)
        return self
      
    def verify_invalid_phone_error_message(self):
        """Verify invalid phone number error message is displayed"""
        error_element = self.driver.find_element(*self.INVALID_PHONE_MSG)
        assert error_element.text == " 格式錯誤。", "Invalid phone error message is not correct"
        return error_element.text
      
    
    def click_contact_back_btn_to_appointment(self):
        """Click contact back button to appointment page"""
        self.driver.find_element(*self.CONTACT_BACK_BTN).click()
        return self


    def search_by_phone(self):
        """Search contact by partial phone number"""
        self.driver.find_element(*self.PHONE_SEARCH_BUTTON).click()
        return self

    def search_by_name(self):
        """Search contact by name"""
        self.driver.find_element(*self.NAME_SEARCH_BUTTON).click()
        return self

    def select_search_result_and_save(self):
        """Randomly select search result and save contact"""
        try:

            specific_result = self.driver.find_element(*self.SPECIFIC_SEARCH_RESULT)
            
            if specific_result:
                specific_result.click()
                time.sleep(1)
                
                save_button = self.driver.find_element(*self.SAVE_CONTACT_BUTTON)
                save_button.click()
            else:
                print("No specific search result found")
                
            
        except Exception as e:
            print(f"Error selecting specific search result: {str(e)}")
            
        return self
      
    def contact_has_chosen(self):
        """Contact has chosen"""
        assert self.driver.find_element(*self.CONTACT_HAS_CHOSEN).is_displayed(), "Contact has not chosen"
        return self
      
    def change_contact_info(self):
        """Change contact info"""
        self.driver.find_element(*self.CONTACT_HAS_CHOSEN).click()
        self.driver.find_element(*self.CONTACT_PHONE_CHANGE).clear()
        self.enter_phone_number("911111116")
        self.search_by_phone()
        try:

            specific_result = self.driver.find_element(*self.CHANGE_SPECIFIC_SEARCH_RESULT)
            
            if specific_result:
                specific_result.click()
                time.sleep(0.5)
                
                save_button = self.driver.find_element(*self.SAVE_CONTACT_BUTTON)
                save_button.click()
            else:
                print("No specific search result found")
                
            
        except Exception as e:
            print(f"Error selecting specific search result: {str(e)}")
            
        return self
        

    def work_as_expected_then_back_to_calendar(self):
        """Work as expected then back to calendar to calendar"""
        time.sleep(2)
        self.driver.find_element(*self.BACK_TO_CALENDAR_BTN).click()
        try:
            self.driver.find_element(*self.SERVICE_CANCEL_BTN).click()
        except:
            pass
        return self

   