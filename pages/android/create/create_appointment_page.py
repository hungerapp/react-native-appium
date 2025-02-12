import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class CreateAppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        
    # Basic element locators
    PERSONAL_PAGE_BACK_TO_CALENDAR_BTN = (AppiumBy.ACCESSIBILITY_ID, '返回')
    CREATE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(11)')
    CREATE_APPOINTMENT_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(7)')
    CONTACT_INFO_SECTION = (AppiumBy.ACCESSIBILITY_ID, '匿名')
    SERVICE_PERSON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務人員")')
    SERVICE_TESTING_PERSON = (AppiumBy.ACCESSIBILITY_ID, 'QA測試人員')
    SERVICE_PAGE_TOGGLE_SWITCH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(31)')
    SERVICE_PAGE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(1)')
    SERVICE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("服務")')
    TAB_CONTAINER = (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
    SERVICE_TAB_CONTAINER = (AppiumBy.XPATH, "//android.widget.HorizontalScrollView/android.view.ViewGroup")
    AUTO_TEST_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自動化測試服物分類")')
    SERVICE_ITEMS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("測試服務")')
    SAVE_SERVICE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    SUB_SERVICE_SAVE_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    CONTACT_CANCEL_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)')
    SERVICE_CANCEL_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)')
    TIME = (AppiumBy.XPATH, '//android.widget.TextView[@text="預約時間"]')
    TIME_CONTAINER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(57)')
    TIME_SLOTS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains(":")')
    SAVE_TIME_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
    SELECT_BUSY_TIME = (AppiumBy.ACCESSIBILITY_ID, '確定')
    CONFIRM_CREATE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '新增預約')

    
    # Contact related elements
    PHONE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入電話")')
    NAME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("請輸入姓名")')
    PHONE_SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '電話搜尋')
    NAME_SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, '姓名搜尋')
    SAVE_CONTACT_BUTTON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    INVALID_PHONE_MSG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" 格式錯誤。")')
    PHONE_SEARCH_RESULTS = (AppiumBy.ANDROID_UIAUTOMATOR, '')
    NAME_SEARCH_RESULTS = (AppiumBy.ANDROID_UIAUTOMATOR, '')

    
    def personal_page_back_to_calendar(self):
        """Click back to calendar button"""
        self.driver.find_element(*self.PERSONAL_PAGE_BACK_TO_CALENDAR_BTN).click()
        time.sleep(3)
        return self
    
    
    def create_appointment(self):
        """Click create appointment button"""
        
        try:
          time.sleep(0.5)
          create_button = self.driver.find_element(*self.CREATE_BTN)
          if create_button.is_displayed() and create_button.is_enabled():
              create_button.click()
                    
        except NoSuchElementException:
          raise NoSuchElementException("Unable to find create appointment button after multiple attempts")
      
        self.driver.find_element(*self.CREATE_APPOINTMENT_OPTION).click()
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

    def fill_existing_contact(self, test_name):
        """Fill in contact info with existing contact"""
        self.driver.find_element(*self.CONTACT_INFO_SECTION).click()
        self.driver.find_element(*self.NAME_SEARCH_INPUT).send_keys(test_name)
        self.driver.find_element(*self.NAME_SEARCH_BUTTON).click()
        self.driver.find_element(*self.SEARCH_RESULTS).click()
        self.driver.find_element(*self.SAVE_CONTACT_BUTTON).click()
        time.sleep(2)
        return self

    def select_service_person(self):
        """Select first available service person"""
        self.driver.find_element(*self.SERVICE_PERSON).click()
        
        # click toggle switch 
        self.driver.find_element(*self.SERVICE_PAGE_TOGGLE_SWITCH).click()
        
        # select service testing person
        service_testing_person = self.driver.find_element(*self.SERVICE_TESTING_PERSON)
        if service_testing_person:
            service_testing_person.click()
            
        time.sleep(2)
        # click save button
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
            time.sleep(0.5)
            
            num_to_select = 2
            selected_options = random.sample(list(SUB_SERVICE_OPTIONS.values()), num_to_select)
            
            for description in selected_options:
                try:
                    option_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{description}")')
                    option_element = self.driver.find_element(*option_locator)
                    option_element.click()
                    time.sleep(0.5)
                except:
                    continue
            
            # Click save button for sub-service
            sub_save_button = self.driver.find_element(*self.SUB_SERVICE_SAVE_BTN)
            sub_save_button.click()
            time.sleep(0.5)
            return True
            
        except:
            return False

    def select_service(self):
        """
        1. Click service selection button
        2. Find AUTO_TEST_TAB
        3. Must select exactly 2 unique services
        4. Handle sub-services if modal appears
        """
        # Click service selection button and wait for page to load
        self.driver.find_element(*self.SERVICE).click()
        time.sleep(1)


        try:
            tab_container = self.driver.find_element(*self.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location
            

            start_x = location['x'] + int(size['width'] * 0.8)  
            end_x = location['x'] + int(size['width'] * 0.2) 
            y = location['y'] + int(size['height'] * 0.5)
            
            found_target = False
            max_attempts = 5
            
            while not found_target and max_attempts > 0:
                try:
                    auto_test_tab = self.driver.find_element(*self.AUTO_TEST_TAB)
                    auto_test_tab.click()
                    time.sleep(0.5)
                    found_target = True
                    break
                except:
                    self.driver.swipe(start_x, y, end_x, y, 100)  
                    time.sleep(0.5)
                    max_attempts -= 1
            
            if not found_target:
                print("Could not find AUTO_TEST_TAB after maximum attempts")
                return self
                
        except Exception as e:
            print(f"Error finding or swiping tabs: {str(e)}")
            return self

        # Must select 2-3 unique services under AUTO_TEST_TAB
        try:
            time.sleep(1)
            service_items = self.driver.find_elements(*self.SERVICE_ITEMS)
            selected_indices = set()  
            selected_texts = set() 
            
            if service_items:
                attempts = 0
                max_attempts = 5
                target_selections = random.randint(2, 3)  
                
                while len(selected_indices) < target_selections and attempts < max_attempts:
                    available_indices = set(range(len(service_items))) - selected_indices
                    if not available_indices:
                        break
                        
                    index = random.choice(list(available_indices))
                    service = service_items[index]
                    
                    try:
                       
                        service_text = service.text
                        if service_text in selected_texts:
                            attempts += 1
                            continue
                            
                        service.click()
                        time.sleep(0.5)
                        selected_indices.add(index)
                        selected_texts.add(service_text)  
                        # Check for sub-services
                        self.handle_sub_services()
                    except:
                        attempts += 1
                        continue
                
               
                if 1 <= len(selected_indices) <= 2 and len(selected_indices) == len(selected_texts):
                    save_button = self.driver.find_element(*self.SAVE_SERVICE_BTN)
                    save_button.click()
                    time.sleep(2)
                else:
                    print("Failed to select required number of unique services, retrying...")
                    return self
            
        except Exception as e:
            print(f"Error selecting services: {str(e)}")

        
        return self

    def select_appointment_time(self):
        """
        1. Must scroll to very bottom of screen first
        2. Only after reaching bottom, find and click time picker
        3. Select random time slot
        """
        try:
            time.sleep(1)
            window_size = self.driver.get_window_size()
            
            
            right_edge_x = window_size['width'] * 0.96
            
    
            start_y = window_size['height'] * 0.95  
            mid_y = window_size['height'] * 0.65    
            end_y = window_size['height'] * 0.35   
            
            
             # 目前使用手勢滑動，但有時會失敗且誤觸匿名、服務人員等區塊
            try:
              self.driver.find_element(*self.CONTACT_CANCEL_BTN).click()
            except:
              self.driver.find_element(*self.SERVICE_CANCEL_BTN).click()
            
            
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

    def click_create_button(self):
        """Click confirm create appointment button"""
        self.driver.find_element(*self.CONFIRM_CREATE_BUTTON).click()
        return self


    # Contact related methods
    def enter_phone_number(self, phone_number):
        """Enter phone number in contact info section"""
        phone_input = self.driver.find_element(*self.PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(phone_number)
        return self

    def verify_invalid_phone_error(self):
        """Verify invalid phone number error message is displayed"""
        return self.driver.find_element(*self.INVALID_PHONE_ERROR).is_displayed()

    def search_by_partial_phone(self, partial_number):
        """Search contact by partial phone number"""
        self.enter_phone_number(partial_number)
        self.driver.find_element(*self.PHONE_SEARCH_BUTTON).click()
        return self

    def search_by_name(self, name):
        """Search contact by name"""
        name_input = self.driver.find_element(*self.NAME_SEARCH_INPUT)
        name_input.clear()
        name_input.send_keys(name)
        self.driver.find_element(*self.NAME_SEARCH_BUTTON).click()
        return self

    def select_search_result_and_save(self):
        """Select first search result and save contact"""
        self.driver.find_element(*self.SEARCH_RESULTS).click()
        self.driver.find_element(*self.SAVE_CONTACT_BUTTON).click()
        return self
