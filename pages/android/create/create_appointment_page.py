import time
import random
import string

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from pages.shared_components.common_use import CommonUseSection
from pages.shared_components.common_action import CommonActions
from pages.locators.android.create.create_appointment_locators import CreateAppointmentLocators

class CreateAppointmentPage(CommonUseSection):
    def __init__(self, driver):
        super().__init__(driver)
        self.common_actions = CommonActions(driver)
    
    
    def personal_page_back_to_calendar(self):
        self.common_actions.click_element(*CreateAppointmentLocators.PERSONAL_PAGE_BACK_TO_CALENDAR_BTN)
        return self
    
    def create_appointment(self):
        """Click create appointment button"""
        self.common_actions.is_element_visible(*CreateAppointmentLocators.CREATE_BTN)
        self.common_actions.click_element(*CreateAppointmentLocators.CREATE_BTN)
        self.common_actions.click_element(*CreateAppointmentLocators.CREATE_APPOINTMENT_OPTION)
        return self
      
    def click_contact_info_section(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.CONTACT_INFO_SECTION)
        self.common_actions.click_element(*CreateAppointmentLocators.CONTACT_INFO_SECTION)
        return self

    def fill_anonymous_contact(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.CONTACT_INFO_SECTION)
        self.common_actions.click_element(*CreateAppointmentLocators.CONTACT_INFO_SECTION)
        try: 
           self.common_actions.click_element(*CreateAppointmentLocators.SAVE_DEFAULT_CONTACT_BUTTON)
        except NoSuchElementException:
            raise NoSuchElementException("Unable to find save contact button after multiple attempts")
        
        return self

    def fill_existing_contact(self, name, phone):
        self.common_actions.click_if_exists(*CreateAppointmentLocators.CONTACT_INFO_SECTION)
        phone_input = self.common_actions.find_element(*CreateAppointmentLocators.PHONE_INPUT)
        phone_input.send_keys(phone)
        name_input = self.common_actions.find_element(*CreateAppointmentLocators.NAME_INPUT)
        name_input.send_keys(name)
        self.select_random_gender()
        self.common_actions.click_element(*CreateAppointmentLocators.SAVE_CONTACT_BUTTON)
        return self
      
    def check_member_passport(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.MEMBER_PASSPORT_BTN)
        self.common_actions.click_element(*CreateAppointmentLocators.MEMBER_PASSPORT_BTN)
        assert self.common_actions.is_element_present(*CreateAppointmentLocators.MEMBER_PASSPORT_TITLE)
        self.common_actions.is_element_present(*CreateAppointmentLocators.MEMBER_PASSPORT_BACK_BTN)
        time.sleep(1)
        self.driver.find_element(*CreateAppointmentLocators.MEMBER_PASSPORT_BACK_BTN).click()
        return self
      
    def select_service2_person(self):
        """Select second service2 person"""
        self.common_actions.click_if_exists(*CreateAppointmentLocators.SERVICE2_PERSON)
        self.common_actions.click_element(*CreateAppointmentLocators.SERVICE_PAGE_TOGGLE_SWITCH)
        self.common_actions.click_element(*CreateAppointmentLocators.SERVICE_OTHER_PERSON)
        self.common_actions.click_element(*CreateAppointmentLocators.SERVICE_PAGE_SAVE_BTN)
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
            selected_keys = random.sample(list(CreateAppointmentLocators.SUB_SERVICE_OPTIONS.keys()), 2)
            
            # Click selected options
            for key in selected_keys:
                option_locator = CreateAppointmentLocators.SUB_SERVICE_OPTIONS[key]
                try:
                    self.common_actions.click_element(*option_locator)
                except NoSuchElementException:
                    continue
            
            # Click save button for sub-service
            self.common_actions.click_element(*CreateAppointmentLocators.SUB_SERVICE_SAVE_BTN)
            
        except Exception as e:
            return False

    def save_service1_button(self):
        self.common_actions.click_element(*CreateAppointmentLocators.SAVE_SERVICE1_BTN)
        return self
    
    def save_service2_button(self):
        self.common_actions.click_element(*CreateAppointmentLocators.SAVE_SERVICE2_BTN)
        return self
  
    def change_service_time_and_service_person(self):
        """Randomly change service time and quantity"""
        
        # Randomly click service time plus or minus button
        time_clicks = random.randint(1, 5)
        for _ in range(time_clicks):
            if random.choice([True, False]):
                self.common_actions.click_element(*CreateAppointmentLocators.SERVICE_TIME_PLUS_BTN)
            else:
                self.common_actions.click_element(*CreateAppointmentLocators.SERVICE_TIME_MINUS_BTN)

        # Randomly click quantity plus or minus buttonick quantity plus or minus button
        quantity_clicks = random.randint(1, 5)
        for _ in range(quantity_clicks):
            if random.choice([True, False]):
                self.common_actions.click_element(*CreateAppointmentLocators.QUANTITY_PLUS_BTN)
            else:
                self.common_actions.click_element(*CreateAppointmentLocators.QUANTITY_MINUS_BTN)
        return self
        
    def note_input(self):
        """Input random note with mixed characters"""
        self.common_actions.click_element(*CreateAppointmentLocators.NOTE_INPUT)
        
        time.sleep(0.5)
        # randomly click quick select 2 options
        options = list(CreateAppointmentLocators.QUICK_SELECT_NOTE_CONTENT.keys())
        for option in random.sample(options, 2):
            self.driver.find_element(*CreateAppointmentLocators.QUICK_SELECT_NOTE_CONTENT[option]).click()
        
        characters = string.ascii_letters + string.digits + string.punctuation + "夯客測試開發"
        random_note = ''.join(random.choices(characters, k=10))
        self.common_actions.click_element(*CreateAppointmentLocators.NOTE_CONTENT_INPUT)
        self.common_actions.click_element(*CreateAppointmentLocators.MODAL_NOTE_CONTENT_INPUT)
        
        self.driver.find_element(*CreateAppointmentLocators.MODAL_NOTE_CONTENT_INPUT).send_keys(random_note)
        self.hide_keyboard()
        
        self.common_actions.click_element(*CreateAppointmentLocators.MODAL_NOTE_SAVE_BTN)
        self.common_actions.click_element(*CreateAppointmentLocators.NOTE_CONTENT_SAVE_BTN)
        
        return self  
    
    def click_one_more_service(self):
        self.common_actions.click_if_exists(*CreateAppointmentLocators.ADD_ONE_MORE_SERVICE)
        
    def one_more_service(self):
        self.select_service2_person()
        self.select_service2()
        return self
    
    def click_service(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.SERVICE)
        self.common_actions.click_element(*CreateAppointmentLocators.SERVICE)
        
    def click_service2(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.SERVICE2)
        self.common_actions.click_element(*CreateAppointmentLocators.SERVICE2)
        
    def select_service2(self):
        self.click_service2()
        self.common_actions.click_if_exists(*CreateAppointmentLocators.SERVICE)

        try:
            tab_container = self.common_actions.find_element(*CreateAppointmentLocators.TAB_CONTAINER)
            size = tab_container.size
            location = tab_container.location

            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
            y = location['y'] + int(size['height'] * 0.5)

            max_attempts = 5
            found_target = False

            for _ in range(max_attempts):
                self.common_actions.swipe(start_x, y, end_x, y, 100)
                try:
                    self.common_actions.click_element(*CreateAppointmentLocators.AUTO_TEST_TAB)
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
            service1 = self.common_actions.find_element(*CreateAppointmentLocators.SERVICE_OPTION1)
            service4 = self.common_actions.find_element(*CreateAppointmentLocators.SERVICE_OPTION4)
            
            service4.click()
            time.sleep(1)
            self.handle_sub_services()
            
            time.sleep(1)
            service1.click()
            
        except Exception as e:
            print(f"Error selecting services: {str(e)}")

        self.save_service2_button()

    def delete_service(self):
        self.common_actions.click_element(*CreateAppointmentLocators.DELETE_SERVICE_BTN)
        return self
      
    def select_appointment_time(self):
        """
        1. Must scroll to very bottom of screen first
        2. Only after reaching bottom, find and click time picker
        3. Select random time slot
        """
        try:
            window_size = self.common_actions.get_screen_size()
            right_edge_x = window_size[0] * 0.95
            start_y = window_size[1] * 0.95
            mid_y = window_size[1] * 0.65
            end_y = window_size[1] * 0.35

            self.common_actions.swipe(
                right_edge_x,
                start_y,
                right_edge_x,
                mid_y,
                2000
            )

            self.common_actions.swipe(
                right_edge_x,
                mid_y,
                right_edge_x,
                end_y,
                2000
            )

            self.common_actions.swipe(
                right_edge_x,
                end_y * 1.2,
                right_edge_x,
                end_y,
                500
            )
            
            self.common_actions.click_element(AppiumBy.ACCESSIBILITY_ID, '預約時間')
            
            self.common_actions.wait_for_element_visible(*CreateAppointmentLocators.DATE_BLOCK)
            # click date block
            self.common_actions.click_element(*CreateAppointmentLocators.DATE_BLOCK)
            
            # select random date
            direction = random.choice(['left', 'right'])
            if direction == 'left':
                self.common_actions.click_element(*CreateAppointmentLocators.LEFT_DATE_ARROW)
            else:
                self.common_actions.click_element(*CreateAppointmentLocators.RIGHT_DATE_ARROW)
            
            
            dates = self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="一, 二, 三, 四, 五, 六, 日"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
            random.choice(dates).click()
            
            # Control page (left, right, today button)

            today_button = self.common_actions.find_element(*CreateAppointmentLocators.TODAY_TIME_BUTTON)
            left_arrow = self.common_actions.find_element(*CreateAppointmentLocators.LEFT_TIME_ARROW)
            right_arrow = self.common_actions.find_element(*CreateAppointmentLocators.RIGHT_TIME_ARROW)

            buttons = [today_button, left_arrow, right_arrow]


            random_buttons = random.sample(buttons, 2)
            for button in random_buttons:
                button.click()
                time.sleep(0.5)
            
            
            time_slots = self.driver.find_elements(*CreateAppointmentLocators.TIME_SLOTS)
            if time_slots:
                random_slot = random.choice(time_slots)
                random_slot.click()
                self.common_actions.click_element(*CreateAppointmentLocators.SAVE_TIME_BTN)
                try:
                    self.common_actions.click_element(*CreateAppointmentLocators.SELECT_BUSY_TIME)
                except:
                    print("Unable to select time slot")
            else:
                print("No available time slots found")
        except Exception as e:
            print(f"Error selecting appointment time: {str(e)}")
        
        return self

    def select_deposit_options(self):
        """
        Randomly toggle two specific deposit options and save.
        """
        self.common_actions.click_element(*CreateAppointmentLocators.DEPOSIT_BTN)
        
        try:
  
            toggle1 = self.common_actions.find_element(*CreateAppointmentLocators.DEPOSIT_TOGGLE_1)
            toggle2 = self.common_actions.find_element(*CreateAppointmentLocators.DEPOSIT_TOGGLE_2)

            # randomly click two specific deposit options
            for toggle in [toggle1, toggle2]:
                if random.choice([True, False]):
                    toggle.click()
                    time.sleep(1)

            # Click save button
            self.common_actions.click_element(*CreateAppointmentLocators.DEPOSIT_SAVE_BTN)

        except Exception as e:
            print(f"Error selecting deposit options: {str(e)}")
    
    def click_create_button(self):
        self.common_actions.click_element(*CreateAppointmentLocators.CONFIRM_CREATE_BUTTON)
        return self

    # Contact related methods
    def enter_phone_number(self, phone_number):
        phone_input = self.common_actions.find_element(*CreateAppointmentLocators.PHONE_INPUT)
        self.common_actions.send_keys_to_element(phone_input, phone_number)
        return self
    
    def enter_name(self, name):
        name_input = self.common_actions.find_element(*CreateAppointmentLocators.NAME_INPUT)
        self.common_actions.send_keys_to_element(name_input, name)
        return self
      
    def verify_invalid_phone_error_message(self):
        error_element = self.common_actions.get_element_text(*CreateAppointmentLocators.INVALID_PHONE_MSG)
        assert error_element == " 格式錯誤。", "Invalid phone error message is not correct"
        return error_element
      
    def click_contact_back_btn_to_appointment(self):
        self.common_actions.click_element(*CreateAppointmentLocators.CONTACT_BACK_BTN)
        return self

    def search_by_phone(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.PHONE_SEARCH_BUTTON)
        time.sleep(1)
        self.driver.find_element(*CreateAppointmentLocators.PHONE_SEARCH_BUTTON).click()
        return self

    def search_by_name(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.NAME_SEARCH_BUTTON)
        time.sleep(1)
        self.driver.find_element(*CreateAppointmentLocators.NAME_SEARCH_BUTTON).click()
        return self

    def select_search_result_and_save(self):
        try:
            time.sleep(1.5)
            self.common_actions.is_element_visible(*CreateAppointmentLocators.SPECIFIC_SEARCH_RESULT)
            self.common_actions.click_element(*CreateAppointmentLocators.SPECIFIC_SEARCH_RESULT)
                    
            time.sleep(0.5)
            self.driver.find_element(*CreateAppointmentLocators.SAVE_CONTACT_BUTTON).click()
                       
        except Exception as e:
            print(f"Error selecting specific search result: {str(e)}")
            
        return self
      
    def contact_has_chosen(self):
        assert self.common_actions.is_element_present(*CreateAppointmentLocators.CONTACT_HAS_CHOSEN), "Contact has not chosen"
        return self
      
    def change_contact_info(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.CONTACT_HAS_CHOSEN)
        self.common_actions.click_element(*CreateAppointmentLocators.CONTACT_HAS_CHOSEN)
        self.common_actions.clear_text(*CreateAppointmentLocators.CONTACT_PHONE_CHANGE)
        self.enter_phone_number("911111116")
        time.sleep(2)
        self.search_by_phone()
        try:
            specific_result = self.common_actions.find_element(*CreateAppointmentLocators.CHANGE_SPECIFIC_SEARCH_RESULT)
            
            specific_result.click()               
            self.common_actions.click_element(*CreateAppointmentLocators.SAVE_CONTACT_BUTTON)
        except Exception as e:
            print(f"Error selecting specific search result: {str(e)}")
            
        return self
    
    def left_before_complete_appointment(self):
        self.common_actions.click_element(*CreateAppointmentLocators.BACK_TO_CALENDAR_BTN)
        self.common_actions.click_if_exists(*CreateAppointmentLocators.SERVICE_CANCEL_BTN)
        return self
        
    def work_as_expected_then_back_to_calendar(self):
        self.common_actions.is_element_visible(*CreateAppointmentLocators.BACK_TO_CALENDAR_BTN)
        self.common_actions.click_element(*CreateAppointmentLocators.BACK_TO_CALENDAR_BTN)
        return self

   
   